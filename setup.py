"""Setup for the umlsparser package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Tom Oberhauser",
    author_email="tom.oberhauser@beuth-hochschule.de",
    name='umlsparser',
    license='',
    description='Parser for UMLS data',
    version='v0.2.2',
    long_description=README,
    url='https://github.com/DATEXIS/UMLSParser',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=['tqdm'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
