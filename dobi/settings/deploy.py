from .base import *


environ.Env.read_env(
    env_file = os.path.join(BASE_DIR,'.env')
)

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# pymysql.install_as_MySQLdb()
#20210305 SECRET_KEY바꿈
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#-------DATABASE-------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',  #mariadb의 container이름
        'PORT': '3306',
    }
}
