from functools import wraps

from flask import g, redirect, request, url_for

from hometapapi.settings import HOME_TAP_API_KEY


def api_key_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.args.get("api_key") != HOME_TAP_API_KEY:
            return redirect(url_for("public.home", next=request.url))
        return f(*args, **kwargs)

    return decorated_function
