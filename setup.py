from setuptools import setup

setup(
    # Application name:
    name="fireBreather",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="dukeman",
    author_email="gabeduke@gmail.com",

    # Packages
    packages=["app"],

    # Include additional files into the package
    include_package_data=True,

    # Details
     url="http://pypi.python.org/pypi/fireBreather_v001/",

    #
    # license="LICENSE.txt",
    description="Useful towel-related stuff.",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "enum34", "ISStreamer", "httplib2", 'requests'

    ],
)
