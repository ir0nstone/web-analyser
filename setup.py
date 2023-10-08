from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="web_ctf_analyser",
    version='{{VERSION_PLACEHOLDER}}',
    author="Andrej Ljubic",
    author_email="andrej.ljubic05@hotmail.com",
    description="A website analyser for CTF challenges",
    url="https://github.com/ir0nstone/web-analyser",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['colorama', 'beautifulsoup4', 'requests', 'argparse'],
    keywords=['pypi', 'cicd', 'python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
    entry_points={
        'console_scripts': [
            'web-analyser=web_analyser.web_analyser:main',
        ],
    },
)
