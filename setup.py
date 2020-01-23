# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:03:53 2020

@author: naman
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis_101883055-Naman_Goyal", # Replace with your own username
    version="0.0.2",
    author="Naman Goyal",
    author_email="ngoyal_be17@thapar.edu",
    description="Topsis package for MCDM(Multiple Criteria Decision Making)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)