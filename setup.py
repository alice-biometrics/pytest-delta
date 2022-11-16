import os

from setuptools import setup

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = "pytest-delta"
VERSION = open("pytest_delta/VERSION").read()

with open("requirements/requirements.txt") as f:
    install_requires = f.read().splitlines()

# The text of the README file
with open(os.path.join(CURRENT_DIR, "README.md")) as fid:
    README = fid.read()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description="`pytest-delta` is a plugin to run your tests only when selected files are changed.",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=["Result", "Monad", "Typed", "Typing"],
    url="https://github.com/alice-biometrics/pytest-delta",
    author="Alice Biometrics",
    author_email="support@alicebiometrics.com",
    license="MIT",
    install_requires=install_requires,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=["pytest_delta"],
    include_package_data=True,
    zip_safe=False,
)
