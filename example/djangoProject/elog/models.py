from django.db import models

# Create your models here.

class Log(models.Model):
    run_number = models.IntegerField(null=True)
    start_time = models.DateTimeField(null=True)
    stop_time = models.DateTimeField(null=True)
    fc73_begin = models.FloatField(default=0)
    fc74_begin = models.FloatField(default=0)
    fc75_begin = models.FloatField(default=0)
    d1_begin = models.FloatField(default=0)
    d2_begin = models.FloatField(default=0)
    ic_gas_pressure_begin = models.FloatField(default=0)
    fc73_end = models.FloatField(default=0)
    fc74_end = models.FloatField(default=0)
    fc75_end = models.FloatField(default=0)
    d1_end = models.FloatField(default=0)
    d2_end = models.FloatField(default=0)
    ic_gas_pressure_end = models.FloatField(default=0)
    scribe = models.CharField(max_length=50, default='')
    run_type = models.IntegerField(default=-1)
    trigger_type = models.IntegerField(default=-1)
    scaler1 = models.IntegerField(default=0) # OBJ Scint
    scaler2 = models.IntegerField(default=0) # XFP Scint
    scaler3 = models.IntegerField(default=0) # RED&BLUE
    title = models.CharField(max_length=200, default='')
    note = models.TextField(null=True, default='')

    runTypeText = ["Data", "Beam", "Calibration", "Trigger", "Note", "Junk"]

    triggerTypeText = ["Coincidence", "DS10", "Coinci.+DS50", "Secondary", "S800 singles", "CsI singles"]
    
    def getRunType(self):
        if (int(self.run_type) < len(self.runTypeText) and int(self.run_type) >= 0):
            return self.runTypeText[self.run_type]
        else:
            return "----"

    def getTriggerType(self):
        if (int(self.trigger_type) < len(self.triggerTypeText) and int(self.trigger_type) >= 0):
            return self.triggerTypeText[self.trigger_type]
        else:
            return "----"

    def getDuration(self):
        if self.start_time and self.stop_time:
            duration = self.stop_time - self.start_time
            values = divmod(duration.days * 86400 + duration.seconds, 3600)
            MnS = divmod(values[1], 60)
            if values[0] is not 0:
                return "%02d:%02d:%02d" % (values[0], MnS[0], MnS[1])
            else:
                MnS = divmod(values[1], 60)
                return "%02d:%02d" % (MnS[0], MnS[1])
        else:
            return ""

    def __str__(self):
        return "%d %s %s" % (self.run_number, self.getRunType(), self.title)
