<!-- settings.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:46:49 2019 (+0800)
;; Last-Updated: 一 5月 13 21:22:10 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 5
;; URL: http://wuhongyi.cn -->

# settings

```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR其实就是项目的根文件夹
```


```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```

```python
# 允许访问的主机
ALLOWED_HOSTS = []
```


```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        # 项目根文件夹下的templates子文件夹
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


```python
LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'zh-hans'
```



```python
#0时区
TIME_ZONE = 'UTC'

#中国时区
TIME_ZONE = 'Asia/Shanghai'



#Django如果开启了Time Zone功能，则所有的存储和内部处理，甚至包括直接print显示全都是UTC的。只有通过模板进行表单输入/渲染输出的时候，才会执行UTC本地时间的转换。
#所以建议后台处理时间的时候，最好完全使用UTC，不要考虑本地时间的存在。而显示时间的时候，也避免手动转换，尽量使用Django模板系统代劳。
#启用 USE_TZ = True 后，处理时间方面，有两条 “黄金法则”：
#    保证存储到数据库中的是 UTC 时间；
#    在函数之间传递时间参数时，确保时间已经转换成 UTC 时间；

#比如，通常获取当前时间用的是：
import datetime
now = datetime.datetime.now()

#启用 USE_TZ = True 后，需要写成：
import datetime 
from django.utils.timezone import utc
utcnow = datetime.datetime.utcnow().replace(tzinfo=utc)

#除非应用支持用户设置自己所在的时区，通常我们不需要关心模板的时区问题。模板在展示时间的时候，会使用 settings.TIME_ZONE 中的设置自动把 UTC 时间转成 settings.TIME_ZONE 所在时区的时间渲染。
TIME_ZONE = 'Asia/Shanghai'
```





```python
# STATIC_URL---给外界用户直接访问静态文件的路径
STATIC_URL = '/static/'
```



```python
# 在文件的最后面添加以下内容，添加文件路径
# STATICFILES_DIRS --- 全局变量定义了存储静态文件集合
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'abc'),
    os.path.join(BASE_DIR, 'app01', 'static')
]
```




<!-- settings.md ends here -->
