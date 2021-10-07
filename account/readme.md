Move Login Folder into Django Static Folder.

Add into middleware in base settings.py:
    'account.middleware.LoginRequiredMiddleware',
    

Add Underneath WSGI_APPLICATION:
    AUTH_USER_MODEL = "account.Account"


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media")
]

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")


if DEBUG:
    EMAIL_BACKEND = (
        "django.core.mail.backends.console.EmailBackend"
    )
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = " " #The sender email
    EMAIL_HOST_PASSWORD = " " #The sender email password
    DEFAULT_FROM_EMAIL=" " #The sender email


Add to base urls.py:
    from django.conf import settings
    from django.conf.urls.static import static

    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
