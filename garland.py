# -*- coding: utf-8 -*-

"""
Garland: for unwrapping decorators.
"""

__author__ = 'Ben Lopatin'
__email__ = 'ben@wellfire.co'
__version__ = '0.3.0'

import sys
import importlib

if sys.version_info.major == 3:
    from importlib import reload  # Common interface
    from unittest.mock import patch
else:
    from mock import patch


def mock_decorator(*a, **k):
    """
    An pass-through decorator that returns the underlying function.

    This is used as the default for replacing decorators.
    """
    # This is a decorator without parameters, e.g.
    #
    # @login_required
    # def some_view(request):
    #     ...
    #
    if a:
        # This could fail in the instance where a callable argument is passed
        # as a parameter to the decorator!
        if callable(a[0]):
            def wrapper(*args, **kwargs):
                return a[0](*args, **kwargs)
            return wrapper

    # This is a decorator with parameters, e.g.
    #
    # @render_template("index.html")
    # def some_view(request):
    #     ...
    #
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper
    return real_decorator


def tinsel(to_patch, module_name, decorator=mock_decorator):
    """
    Decorator for simple in-place decorator mocking for tests

    Args:
        to_patch: the string path of the function to patch
        module_name: complete string path of the module to reload
        decorator (optional): replacement decorator. By default a pass-through
            will be used.

    Returns:
        A wrapped test function, during the context of execution the specified
        path is patched.

    """
    def fn_decorator(function):
        def wrapper(*args, **kwargs):
            with patch(to_patch, decorator):
                m = importlib.import_module(module_name)
                reload(m)
                function(*args, **kwargs)

            reload(m)
        return wrapper
    return fn_decorator
