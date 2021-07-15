from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("database",  ["database/dict.py"]),
    # Extension("mymodule2",  ["mymodule2.py"]),
]
for e in ext_modules:
    e.cython_directives = {'language_level': "3"} #all are Python-3

setup(
    name = 'simstring-fast',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)