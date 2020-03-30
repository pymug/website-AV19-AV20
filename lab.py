import site_api
import string
import inspect
from inspect import getmembers, isfunction

functions_list = [o for o in getmembers(site_api) if isfunction(o[1])]
for f in functions_list:

    print('''
**{}({})**

```
{}
```
'''.format(
    f[0], 
    inspect.getargspec(f[1]),
    f[1].__doc__
    ))