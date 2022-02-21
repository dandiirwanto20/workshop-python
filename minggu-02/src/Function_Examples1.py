def foo(name, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
# Traceback (most recent call last): (Output Error)
#  File "<stdin>", line 1, in <module> (Output Error)
# TypeError: foo() got multiple values for argument 'name' (Output Error)


def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})
# True (Output)