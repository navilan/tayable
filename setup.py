# -*- coding: utf-8 -*-
from distutils.core import setup
from tayable import __version__

setup(
    name='tayable',
    version=__version__,
    author='Lakshmi Vyas',
    author_email='lakshmi.vyas@gmail.com',
    url='http://github.com/lakshmivyas/tayable',
    description='Convert html table to yaml',
    long_description = 'A simple helper script to use in Textmate and other editors',
    license='MIT',
    install_requires=(
        'pyYAML',
        'pyquery',
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    py_modules=['tayable'],
)
