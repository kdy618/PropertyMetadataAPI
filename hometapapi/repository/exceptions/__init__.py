# -*- coding: utf-8 -*-
"""Exception."""


class InvalidAddress(Exception):
    pass


class RateLimitException(Exception):
    pass


class AuthenticationException(Exception):
    pass


class MissingRequiredParamException(Exception):
    pass
