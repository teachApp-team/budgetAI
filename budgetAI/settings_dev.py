from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,

  'loggers': {
    'django': {
      'handlers': ['console'],
      'level': 'INFO',
    },
    'budgetAI': {
      'handlers' : ['console'],
      'level' : 'DEBUG',
    },
  },

  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class' : 'logging.StreamHandler',
      'formatter' : 'dev'
    },
  },

  'formatters': {
    'dev': {
      'format': '\t'.join([
        '%(asctime)s',
        '[%(levelname)s]',
        '%(pathname)s(Line:%(lineno)d)',
        '%(message)s'
      ])
    },
  }
}