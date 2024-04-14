#!/usr/bin/python3
from setuptools import find_packages, setup

install_requires = open('requirements.txt').readlines()

setup(
    name='mytest',
    version='1.0.0',
    description='Testing __all__',
    license='BSD',
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    cmdclass={},
    url='https://github.com/caronc',
    keywords='',
    author='Chris Caron',
    author_email='lead2gold@gmail.com',
    packages=find_packages(),
    package_data={
        'mytest': [],
    },
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    python_requires='>=3.6',
    setup_requires=[],
)
