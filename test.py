def funck(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    follow_redirection = kwargs.get('follow_redirection', False)

import functools

functools.partial

funck("CHrrr", *[1, 2], **{'a': 1, 'b': 2})

d = {}
c = {'a': 1, 'c': 3}
d.update(**c)

def cache(f):


    def _f(*a, **kw):
        print('xextraxx')
        return f(*a, **kw)
    


    return _f

# cache(a)(1, 2)
# cache(a) -> _f
# cache(a)(1, 2) -> _f(1, 2) -> a(1, 2)

# cache(cache(cache(a)))
@cache
@cache
@cache
def a(a, b, c=1, d=2):
    return a + b

print(cache)
print(cache(a))

print(cache(a)(1, 2))