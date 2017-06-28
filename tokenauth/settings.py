from django.conf import settings

# How long a token should be valid for, in seconds.
TOKEN_DURATION = getattr(settings, "TOKENAUTH_TOKEN_DURATION", 5 * 60)

# Where to redirect after link operations.
LOGIN_URL = getattr(settings, "TOKENAUTH_LOGIN_URL", settings.LOGIN_URL)

# Where to redirect after login or logout.
LOGIN_REDIRECT = getattr(settings, "TOKENAUTH_LOGIN_REDIRECT", settings.LOGIN_REDIRECT_URL)
LOGOUT_REDIRECT = getattr(settings, "TOKENAUTH_LOGOUT_REDIRECT", settings.LOGOUT_REDIRECT_URL or settings.LOGIN_REDIRECT_URL)


DEFAULT_FROM_EMAIL = getattr(settings, "TOKENAUTH_DEFAULT_FROM_EMAIL", settings.DEFAULT_FROM_EMAIL)
