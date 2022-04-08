from .base import *

#env파일이 아닌 Docker secrets에서 가져오는 함수
def read_secret(secret_name):

    file = open("/run/secrets/" + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()   #정제
    file.close()

    return secret

environ.Env.read_env(
    env_file = os.path.join(BASE_DIR,'.env')
)

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# pymysql.install_as_MySQLdb()
#20210305 SECRET_KEY바꿈
#함수 이용
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

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
        'PASSWORD': read_secret("MYSQL_PASSWORD"),
        'HOST': 'mariadb',  #mariadb의 container이름
        'PORT': '3306',
    }
}
