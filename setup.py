# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="SuperAlignment",  # Required
    version="0.0.2",    # Required
    description="Utils for SuperAlignment api",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email="dingo0927@126.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="AGI,SuperAlignment,SuperIntelligence",
    packages=find_packages(where="src"),  # Required
    package_dir={'': 'src'},
    python_requires=">=3.4",
    project_urls={
        "homepage": "http://www.deepnlp.org",
        "repository": "https://github.com/rockingdingo/SuperAlignment"
    },
)
