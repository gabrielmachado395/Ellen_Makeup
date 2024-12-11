# settings.py

import os
from pathlib import Path

# Caminho do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta para criptografia (mantenha-a em segredo em produção)
SECRET_KEY = 'django-insecure-!2b4ddbvv0q7872iumdnq%q^=hv2t8e$n2ewcj^*ux^=im@zo&'

# Debug mode (desabilite isso em produção)
DEBUG = True

# Permitir acesso local
ALLOWED_HOSTS = []

# Apps instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produtos',  # Adicione seu app aqui
]

# Middleware (geralmente não precisa de muitas mudanças)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'produtos.middleware.AtualizarCarrinhoMiddleware',
]

# Configuração das URLs e WSGI
ROOT_URLCONF = 'ellen_makeup.urls'

WSGI_APPLICATION = 'ellen_makeup.wsgi.application'

# Configurações de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Pasta para templates HTML
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

# Banco de dados (SQLite por padrão, mas você pode usar outro)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuração de autenticação e senhas
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

# Configuração de internacionalização
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# URL e configuração de arquivos estáticos
STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/static')]

# Configuração de uploads de arquivos e imagens
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuração do caminho para arquivos estáticos em produção
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Padrão para o campo chave primária
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'login'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'