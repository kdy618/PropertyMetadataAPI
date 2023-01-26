# -*- coding: utf-8 -*-
"""API."""

from functools import wraps

from flask import request

from hometapapi.settings import HOME_TAP_API_KEY


def api_key_required(f):
    """Quick API Key Auth."""
    # TODO Should use oAuth? Bearer? Key/Secret?
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.args.get("api_key") != HOME_TAP_API_KEY:
            return ("Forbidden", 401)
        return f(*args, **kwargs)

    return decorated_function
