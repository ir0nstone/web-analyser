import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="web-ctf-analyser",
    version="0.0.1",
    author="ir0nstone",
    author_email="bobbiusbobety@gmail.com",
    description="A tool to analyse websites for CTF challenges",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ir0nstone/web-analyser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)