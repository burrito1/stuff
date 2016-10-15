#!/home/burrito/Desktop/Sobra/el-rejunte/venv/bin/python
# EASY-INSTALL-DEV-SCRIPT: 'Django==1.11.dev20161015141902','django-admin.py'
__requires__ = 'Django==1.11.dev20161015141902'
import sys
from pkg_resources import require
require('Django==1.11.dev20161015141902')
del require
__file__ = '/home/burrito/Desktop/Sobra/el-rejunte/django/django/bin/django-admin.py'
if sys.version_info < (3, 0):
    execfile(__file__)
else:
    exec(compile(open(__file__).read(), __file__, 'exec'))
