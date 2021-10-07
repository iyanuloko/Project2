import re
from . import login_redirect as Log
from django.conf import settings
from django.shortcuts import redirect


EXEMPT_URLS = [re.compile(Log.LOGIN_URL.lstrip('/'))]
if hasattr(Log, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS+=[re.compile(url) for url in Log.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')

        if not request.user.is_authenticated:
            if not any(url.match(path) for url in EXEMPT_URLS):
                return redirect(Log.LOGIN_URL)
