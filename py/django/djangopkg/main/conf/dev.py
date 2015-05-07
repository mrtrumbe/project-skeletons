from os import path

DEBUG=True

PROJECT_ROOT = path.normpath(
    path.join(
        path.dirname(path.realpath(__file__)), '..', '..', '..', '..')
)

SECRET_KEY = 'BJ_C_Uj)=B+I!MI,bJuU|Ko=3~RRoaeq5[dscgv.>sOj|[VVk~'

STATIC_URL = '/static/'


INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # our apps
    'djangopkg.widget',
]


MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'common.tspapi.TspApiMiddleware',
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_DIRS = [
    path.normpath(path.join(PROJECT_ROOT, 'templates')),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'common.context_processors.site_info',
]
