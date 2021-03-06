import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paxful-api",
    version="1.0",
    author="tholness",
    author_email="support.ec1818@tryninja.io",
    description="A python wrapper for Paxful REST API v1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tholness/Paxful-API-Wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.23.0',
        'simplejson>=3.17.0'
    ]
)
