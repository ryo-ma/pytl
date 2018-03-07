import os
from setuptools import setup, find_packages

def readfile(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name='pytl',
    version='0.2.1',
    description='Command line tool that parses python file, enumerates classes and methods as a tree structure.',
    long_description=readfile('README.md'),
    ext_modules=[],
    packages=find_packages(),
    author='ryo-ma',
    author_email='saka_ro@yahoo.co.jp',
    url='https://github.com/ryo-ma/pytl',
    download_url='https://github.com/ryo-ma/pytl',
    keywords='Python file structure tree line',
    license='MIT',
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
    setup_requires=[],
    install_requires=[],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pytl= pytl.pytl:main"
        ]
    },
)
