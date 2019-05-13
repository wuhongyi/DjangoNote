from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings

from elog.models import Log
#import logging

import pytz
import csv

#logger = logger.getLogger(__name__)

class Command(BaseCommand):
    est = pytz.timezone(settings.TIME_ZONE)

    def add_arguments(self, parser):
        parser.add_argument('runnumber', type=int)
        parser.add_argument('toggletype')
        parser.add_argument('date')
        parser.add_argument('time')
        parser.add_argument('title', type=str, nargs='?', default='')
        parser.add_argument('epicChannels')
        parser.add_argument('gasLog', type=str)

    def handle(self, *args, **options):
        date = options['date'].split('/')
        time = options['time'].split(':')
        writetime = self.est.localize(timezone.datetime(int(date[2]), int(date[0]), int(date[1]), int(time[0]), int(time[1]), int(time[2])))

        fc73 = 0
        fc74 = 0
        fc75 = 0
        d1 = 0
        d2 = 0
        gasPressure = 0

        epicChannelFile = open(options['epicChannels'], 'r')
        for line in epicChannelFile:
            column = line.split()
            if column[0] == 'FLTCHAN73':
                try:
                  fc73 = float(column[1])
                except ValueError:
                  fc73 = -9999
            elif column[0] == 'FLTCHAN74':
                try:
                  fc74 = float(column[1])
                except ValueError:
                  fc74 = -9999
            elif column[0] == 'FLTCHAN75':
                try:
                  fc75 = float(column[1])
                except ValueError:
                  fc75 = -9999
            elif column[0] == 'I265DS_MAG.FELD':
                try:
                  d1 = float(column[1])
                except ValueError:
                  d1 = -9999
            elif column[0] == 'I269DS_MAG.FELD':
                try:
                  d2 = float(column[1])
                except ValueError:
                  d2 = -9999

        gasLogFile = open(options['gasLog'], 'r')
        for line in gasLogFile:
            pass
        line = line.replace('\t', ' ')
        line = line.split(' ')
        try:
          gasPressure = float(line[3])
        except ValueError:
          gasPressure = -9999
        
        if options['toggletype'] == "begin":
            newEntry = Log(run_number=options['runnumber'], start_time=writetime, title=options['title'], fc73_begin=fc73, fc74_begin=fc74, fc75_begin=fc75, d1_begin=d1, d2_begin=d2, ic_gas_pressure_begin=gasPressure)
            newEntry.save()
        elif options['toggletype'] == "end":
            modifyEntry = Log.objects.filter(run_number=options['runnumber']).filter(stop_time__isnull=True).order_by('-start_time')[0]
            modifyEntry.stop_time = writetime
            modifyEntry.fc73_end = fc73
            modifyEntry.fc74_end = fc74
            modifyEntry.fc75_end = fc75
            modifyEntry.d1_end = d1
            modifyEntry.d2_end = d2
            modifyEntry.ic_gas_pressure_end = gasPressure

            try:
               with open('/user/e18015/scalers/run%04d.csv' % options['runnumber']) as file_:
                   reader = csv.reader(file_, delimiter=',')
                   run_data = {rows[0]:rows[2] for rows in reader}
                   modifyEntry.scaler1 = int(float(run_data['OBJ']))
                   modifyEntry.scaler2 = int(float(run_data['XFP']))
                   modifyEntry.scaler3 = int(float(run_data['Red_AND_Blue']))
            except Exception as e:
               try:
                   print(e.traceback)
               except Exception:
                   try:
                       # there are exceptions with no traceback... weird
                       print(e)
                   except Exception:
                       pass
            #logger.exception('Cannot read scalers information. Please enter manually'
            modifyEntry.save()
