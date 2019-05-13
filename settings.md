<!-- settings.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:46:49 2019 (+0800)
;; Last-Updated: 一 5月 13 09:50:47 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 1
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
# STATIC_URL---给外界用户直接访问静态文件的路径
STATIC_URL = '/static/'
```



```python
# STATICFILES_DIRS --- 全局变量定义了存储静态文件集合
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'abc'),
    os.path.join(BASE_DIR, 'app01', 'static')
]
```




<!-- settings.md ends here -->
