import re
import setuptools

import dll_finder

with open('README.md', 'r') as fh:
    long_description = fh.read()
    long_description_content_type = 'text/markdown'

def python_classifiers(min_python_version):
    base = 'Programming Language :: Python'
    c = [base]
    pvt = tuple([int(n) for n in min_python_version.split('.')])
    for i in range(1, len(pvt)+1):
        c.append(base + " :: " + '.'.join([str(p) for p in pvt[:i]]))
    return c

classifiers = (python_classifiers(dll_finder.__min_python_version__) +
               [
                   'Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Operating System :: OS Independent',
                   'Topic :: Software Development :: Assemblers',
               ])

setuptools.setup(
    name = 'dll_finder',
    version = dll_finder.__version__,
    author = dll_finder.__author__,
    author_email = dll_finder.__email__,
    description = dll_finder.__description__,
    long_description = long_description,
    long_description_content_type = long_description_content_type,
    url = dll_finder.__url__,
    py_modules = ['dll_finder'],
    install_requires = ['pyparser', 'm5pre'],
    python_requires='>=' + dll_finder.__min_python_version__,
    classifiers = classifiers,
)
