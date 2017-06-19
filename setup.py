#!/usr/bin/env python
"""
Advento
===================
A spaceship game
"""
from setuptools import setup, find_packages

install_requires = [
    'FGAme==0.6.3',
    'pygame==1.9.3',,
]


setup(
    name="Advento",
    version='0.1.1',
    author='Halê Valente, Vinicius Oliveira',
    author_email='halevalente@gmail.com, vinifladf@gmail.com',
    url='git@github.com:Advento/advento.git',
    entry_points={
        'console_scripts': [
            'advento = AdventoMenu:main',
        ]},
    description='A game',
    long_description=__doc__,
    license='GPLv3',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={'src':
                  [
                      'sfx/*',
                      'images/*',
                  ]},
    zip_safe=True,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Environment :: FGAme',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3',
        'Topic :: Utilities',
    ],
)