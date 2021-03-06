"""
Examples of decorated functions to use for testing.

Function with decorator with no parameters

Function with decorator with ordered parameters

Function with decorator with keyword parameters
"""


def no_params(function):
    def wrapper(*args, **kwargs):
        return []
    return wrapper


def with_params(*ordered, **keyword):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper
    return real_decorator


def add_one(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) + 1
    return wrapper


def add_two(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) + 2
    return wrapper
