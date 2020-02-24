"""Byter setup."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="byter",
    version="0.0.2",
    author="Sergey Shilin",
    author_email="shilinshtein@gmail.com",
    description="Python binary object reader/writer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sergeyshilin/byter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
