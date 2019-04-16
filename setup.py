#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=6.0",
    "zope.interface",
    "guillotina>=4.7.0",
    # important! STU3
    "fhir.resources==3.0.1",
]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest", "guillotina_elasticsearch"]

setup(
    author="Md Nazrul Islam",
    author_email="email2nazrul@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="FHIRPath implementation in Python.",
    entry_points={"console_scripts": ["fhirpath=fhirpath.cli:main"]},
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="fhirpath",
    name="fhirpath",
    packages=find_packages("src", include=["fhirpath"]),
    package_dir={"": "src"},
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    extras_require={"test": test_requirements + setup_requirements},
    url="https://github.com/nazrulworld/fhirpath",
    version="0.1.0a1.dev0",
    zip_safe=False,
)
