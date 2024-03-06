"""
Django settings for ply project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os,socket
from pathlib import Path
from decouple import Config,Csv,RepositoryEnv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Enable loading configuration files from ./config: (which can be mounted as an overlay!)
if (os.path.isdir(os.getcwd()+"/config")):
    config = Config(RepositoryEnv(os.getcwd()+"/config/settings.ini"))
else:
    from decouple import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY") 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('PLY_DEBUG') == 'TRUE'

#TODO: MAKE IT SO ALLOWED HOSTS ARE OPTIONAL!
#ALLOWED_HOSTS = [config("ALLOWED_HOST_1"),config("ALLOWED_HOST_2"),config("ALLOWED_HOST_3")] 
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

STATIC_ROOT = config("STATIC_ROOT")

# Application definition
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_bootstrap5',
    'jsignature',
    'django_registration',
    'storages',
    'martor',
    'mathfilters',
    'phonenumber_field',
    'colorful',
    'communities.preferences',
    'content_manager.emoji',
    'content_manager.categories',
    'communities.notifications',
    'dashboard',
    'core.dynapages',
    'communities.profiles',
    'roleplaying.comms',
    'communities.stream',
    'communities.group',
    'content_manager.keywords',
    'communities.community',
    'core.plyscript',
    'core.authentication',
    'core.authentication.ui',
    'media.gallery.core',
    'media.gallery.photos',
    'core.metrics',
    'roleplaying.stats',
    'roleplaying.combat',
    'roleplaying.skills',
    'roleplaying.equipment',
    'roleplaying.spells',
    'roleplaying.items',
    'core.forge',
    'content_manager.almanac',
    'roleplaying.exp',
    'roleplaying.SLHUD',
    'roleplaying.plydice',
    'ply',
    'ufls.themes.neon_nights',
    'ufls.furry',
    'ufls.event',
    'ufls.registrar'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ply.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ply.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('db_table'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PW'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = config('PLY_TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


USE_S3 = config('USE_S3') == 'TRUE'

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    AWS_LOCATION = config('AWS_LOCATION')
    STATIC_URL = '%s/%s' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
    MEDIA_ROOT = "media_root/"
    MEDIA_URL = "/media/"
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    if (config("ALWAYS_LOAD_S3") == "TRUE"):
        # aws settings
        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
        AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
        AWS_DEFAULT_ACL = 'public-read'
        AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
        MEDIA_ROOT = "media_root/"
        MEDIA_URL = "/media/"
    STATIC_URL = '/static/'
    STATIC_ROOT = config('STATIC_ROOT')
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
    MEDIA_ROOT = "/var/www/html/media/"
    MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MARTOR:
# Choices are: "semantic", "bootstrap"
MARTOR_THEME = 'bootstrap'


# Global martor settings
# Input: string boolean, `true/false`
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',        # to enable/disable emoji icons.
    'imgur': 'true',        # to enable/disable imgur/custom uploader.
    'mention': 'false',     # to enable/disable mention
    'jquery': 'true',       # to include/revoke jquery (require for admin default django)
    'living': 'true',      # to enable/disable live updates in preview
    'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',         # to enable/disable hljs highlighting in preview
}

# To show the toolbar buttons
MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'image-upload', 'emoji',
    'direct-mention', 'toggle-maximize', 'help'
]

# Django Bootstrap 5 settings:
BOOTSTRAP5= {
    "javascript_in_head": True,
    "css_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css",
        "integrity": "sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap JavaScript file
    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm",
        "crossorigin": "anonymous",
    }
}


# To setup the martor editor with title label or not (default is False)
MARTOR_ENABLE_LABEL = False

# Imgur API Keys
MARTOR_IMGUR_CLIENT_ID = 'your-client-id'
MARTOR_IMGUR_API_KEY   = 'your-api-key'

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify' # default
MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/' # default

# Markdown extensions (default)
MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins',      # ~~strikethrough~~ and ++underscores++
    'martor.extensions.mention',      # to parse markdown mention
    'martor.extensions.emoji',        # to parse markdown emoji
    'martor.extensions.mdx_video',    # to parse embed/iframe video
    'martor.extensions.escape_html',  # to handle the XSS vulnerabilities
]

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown urls
MARTOR_UPLOAD_URL = '/martor/uploader/' # default
MARTOR_SEARCH_USERS_URL = '/martor/search-user/' # default

# Markdown Extensions
# MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://www.webfx.com/tools/emoji-cheat-sheet/graphics/emojis/'     # from webfx
MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://github.githubassets.com/images/icons/emoji/'                  # default from github
MARTOR_MARKDOWN_BASE_MENTION_URL = 'https://python.web.id/author/'                                      # please change this to your domain

# If you need to use your own themed "bootstrap" or "semantic ui" dependency
# replace the values with the file in your static files dir
MARTOR_ALTERNATIVE_JS_FILE_THEME = "semantic-themed/semantic.min.js"   # default None
MARTOR_ALTERNATIVE_CSS_FILE_THEME = "semantic-themed/semantic.min.css" # default None
MARTOR_ALTERNATIVE_JQUERY_JS_FILE = "jquery/dist/jquery.min.js"        # default None

# URL schemes that are allowed within links
ALLOWED_URL_SCHEMES = [
    "file", "ftp", "ftps", "http", "https", "irc", "mailto",
    "sftp", "ssh", "tel", "telnet", "tftp", "vnc", "xmpp",
]
CSRF_COOKIE_HTTPONLY = False

# EMAIL CONFIG:
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = config("EMAIL_PORT")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
EMAIL_USE_TLS = config('EMAIL_USE_TLS') == 'TRUE'
EMAIL_USE_SSL = config('EMAIL_USE_SSL') == 'TRUE'

# AUTH
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True
REGISTRATION_SALT = 'ae3Phoge'

# PLY:
PLY_USER_DASHBOARD_MODULES = [
    "communities.profiles",
    "communities.community",
    "roleplaying.stats",
    "roleplaying.skills",
    "communities.stream",
    "communities.notifications",
    "communities.preferences",
    "ufls.registrar"

    
]

PLY_WORLDFORGE_DASHBOARD_MODULES = [
    "communities.community",
    "ufls.event",
    "ufls.registrar",
    "communities.stream",
    "media.gallery.core"
]
PLY_STAFF_DASHBOARD_MODULES = [
    "ufls.registrar"
]
PLY_GALLERY_PLUGINS = [
    "media.gallery.photos"
    ]
PLY_AVATAR_FORMATS = ["jpg","jpeg","gif","png","webp","svg"]
PLY_AVATAR_MAX_PX = [1024,1024]

try:
    PLY_HOSTNAME = socket.gethostname()
except:
    PLY_HOSTNAME = "localhost"
    
PHONENUMBER_DEFAULT_REGION = "US"
PLY_GALLERY_STORAGE_USE_S3 = config('PLY_GALLERY_STORAGE_USE_S3')
PLY_TEMP_FILE_BASE_PATH =  config("PLY_TEMP_FILE_BASE_PATH")
PLY_TEMP_FILE_URL_BASE_URL = config("PLY_TEMP_FILE_URL_BASE_URL")
PLY_GALLERY_ORIGINAL_FILE_BASE_PATH = config("PLY_GALLERY_ORIGINAL_FILE_BASE_PATH")
PLY_GALLERY_FILE_BASE_PATH = config("PLY_GALLERY_FILE_BASE_PATH")
PLY_AVATAR_FILE_BASE_PATH = config("PLY_AVATAR_FILE_BASE_PATH")
PLY_AVATAR_FILE_URL_BASE_URL=config("PLY_AVATAR_FILE_URL_BASE_URL")
PLY_GALLERY_FILE_URL_BASE_URL=config("PLY_GALLERY_FILE_URL_BASE_URL")
PLY_GALLERY_HASH_BUF_SIZE  = int(config("PLY_GALLERY_HASH_BUF_SIZE"))
PLY_GALLERY_SHARE_URL_BASE_URL = config("PLY_GALLERY_SHARE_URL_BASE_URL")
PLY_MSG_BROKER_URL=config("PLY_MSG_BROKER_URL")
GALLERY_PHOTOS_THUMBNAIL_SIZE = int(config("GALLERY_PHOTOS_THUMBNAIL_SIZE"))
PLY_GALLERY_MIN_DPI = int(config("PLY_GALLERY_MIN_DPI"))
PLY_GALLERY_MAX_ORIGINAL_SIZE = int(config("PLY_GALLERY_MAX_ORIGINAL_SIZE"))
CELERY_BROKER_URL=config("CELERY_BROKER_URL")
PLY_AVATAR_MAX_KB = int(config("PLY_AVATAR_MAX_KB"))
PLY_AVATAR_STORAGE_USE_S3 = config('PLY_AVATAR_STORAGE_USE_S3')
PLY_DYNAPAGES_PROFILE_TEMPLATE=config("PLY_DYNAPAGES_PROFILE_TEMPLATE")
PLY_DYNAPAGES_PROFILE_TEMPLATE_BANNER_WIDGET = config("PLY_DYNAPAGES_PROFILE_TEMPLATE_BANNER_WIDGET")
PLY_DYNAPAGES_DASHBOARD_TEMPLATE=config("PLY_DYNAPAGES_DASHBOARD_TEMPLATE")
PLY_DYNAPAGES_DASHBOARD_TEMPLATE_BANNER_WIDGET = config("PLY_DYNAPAGES_DASHBOARD_TEMPLATE_BANNER_WIDGET")
PLY_DYNAPAGES_INSTALL_COMPLETE_TEMPLATE=config("PLY_DYNAPAGES_INSTALL_COMPLETE_TEMPLATE",default="communities-community-installComplete-cover")
GRAPPELLI_ADMIN_TITLE="PLY Admin @ "+PLY_HOSTNAME
# PAYMENT PROCESSING:
PAYMENT_HOST = config('UFLS_PAYMENT_HOST', default="http://localhost:8000/")
PAYMENT_USES_SSL = config("UFLS_PAYMENTS_USES_SSL", default=False)
PAYMENT_STRIPE_WEBHOOK_SECRET = config("UFLS_STRIPE_WEBHOOK_SECRET",default="")
PAYMENT_STRIPE_TEST = config('UFLS_STRIPE_TEST', cast=bool, default=True)
if (PAYMENT_STRIPE_TEST == True):
    PAYMENT_STRIPE_PUBLIC_KEY = config('UFLS_PAYMENT_PUBKEY_TEST', default=False)
    PAYMENT_STRIPE_SECRET_KEY = config('UFLS_PAYMENT_SECKEY_TEST', default=False)
    PAYMENT_STRIPE_DONATION_ITEM = config('UFLS_PAYMENT_DONATION_ITEM_TEST', default=False)
else:
    PAYMENT_STRIPE_PUBLIC_KEY = config('UFLS_PAYMENT_PUBKEY', default=False)
    PAYMENT_STRIPE_SECRET_KEY = config('UFLS_PAYMENT_SECKEY', default=False)
    PAYMENT_STRIPE_DONATION_ITEM = config('UFLS_PAYMENT_DONATION_ITEM', default=False)

PLY_DEFAULT_THEME = config('PLY_DEFAULT_THEME',default="core.ui.themes.default")