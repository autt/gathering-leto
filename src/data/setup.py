import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data",
    version="0.0.1",
    description="Get some public data from GitHub issues",
    long_description=long_description,
    url="https://github.com/equinor/gathering-leto",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
