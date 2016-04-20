"""
Examples of decorated functions to use for testing.

- Function with decorator with no parameters
- Function with decorator with ordered parameters
- Function with decorator with keyword parameters

"""

from .decorators import no_params, with_params, add_one, add_two


@no_params
def dictionary(*args, **kwargs):
    return {}


@with_params("hello!")
def world(*args, **kwargs):
    return "world"


@with_params(text="foo!")
def bar(*args, **kwargs):
    return "bar"


@add_one
@add_two
def no_addition(x=0):
    return x
