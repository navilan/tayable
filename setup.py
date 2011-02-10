# -*- coding: utf-8 -*-
import tayable
from distutils.core import setup

setup(
    name='tayable',
    version=tayable.__version__,
    author='Lakshmi Vyas',
    author_email='lakshmi.vyas@gmail.com',
    url='http://github.com/lakshmivyas/tayable',
    description='Convert html table to yaml',
    long_description = 'A simple helper script to use in Textmate and other editors',
    license='MIT',
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
