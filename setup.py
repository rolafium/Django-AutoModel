import os
from setuptools import find_packages, setup
from django_auto_model.info import PROJECT_TAG, VERSION

with open(os.path.join(os.path.dirname(__file__), "README.md")) as fp:
    README = fp.read()

setup(
    name=PROJECT_TAG,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="Auto create instances of your model in your tests",
    long_description=README,
    url="https://github.com/rolafium/Django-AutoModel",
    author="William Di Pasquale",
    author_email="rolafium@protonmail.com",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
