=================================
garland: Python decorator mocking
=================================

.. image:: https://secure.travis-ci.org/bennylope/garland.svg?branch=master
    :alt: Build Status
    :target: http://travis-ci.org/bennylope/garland

.. image:: https://img.shields.io/pypi/v/garland.svg
    :alt: Current PyPI release
    :target: https://crate.io/packages/garland

.. image:: https://img.shields.io/pypi/dm/garland.svg
    :alt: Download count
    :target: https://crate.io/packages/garland

Garland is simple, repeatable decorator mocking.

Why?
====

Decorators are applied at the time the decorated function is first imported, which
makes `mocking them a bit more challenging <http://alexmarandon.com/articles/python_mock_gotchas/#patching-decorators>`_.

I want to be able to be simply patch decorators - typically making them just pass-throughs to
ignore their functionality - without modifying the underlying codebase. And I don't want
to worry about whether a module has already been loaded and is now unpatchable, or it needs
to be patched for every test... and I don't want to write the patching/loading/reloading
code for every test.

Usage
=====

Provided you have a function that you want to test, like so:

.. code:: python

    @my_decorator
    def something_cool(*args, **kwargs):
        ...
        return some_var

With your `my_decoroator` decorator defined in another module, you can mock
`my_decorator` so that you can test just the end decorated function.

In your test, apply the `tinsel` decorator function to the test method where
you want the decorator mocked.

.. code:: python

    @garland.tinsel('utils.decorators.my_decorator', 'very_cool.module')
    def test_something_cool(self):
        self.assertEqual(very_cool.module.something_cool(), "undecorated value")

Now `test_something` can test the return values from `something_cool` without
the decorator potentially returning a different value, or providing a different
function interface.

The `tinsel` decorator takes two arguments:

1. A dotted path to the decorator function you want to mock
2. A dotted path to the module in which your function - the one you're testing -
   is declared. If you're not importing the module like this in your tests then
   this will do you little good (see limits, below).

Limits
======

1. You need to import modules, not named functions, to work with garland.
2. For now this is only tested with decorator functions and function decorators
3. The mock turns your decorator into a pass-through, assuming that this is the
   way you want to mock it.
4. Only Python 3.4 and Python 2.7 are supported at this time.


License
=======

Copyright Ben Lopatin. BSD licensed (see `LICENSE`).
