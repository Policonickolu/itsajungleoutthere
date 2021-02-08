from setuptools import setup, find_packages

setup(
    name='itsajungleoutthere',
    version='1.0.0',
    description='',
    url='https://github.com/Policonickolu/itsajungleoutthere.git',
    author='Heidy Ben Yahia',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    keywords='python flask flask-restplus rest restful api swagger openapi',
    packages=find_packages(),
    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1'],
)
