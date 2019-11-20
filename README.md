# UMLSParser

Parses the UMLS source files.

## Getting Started

### Acquiring UMLS Data

In order to use the UMLS you have to be licensed.
For more information please refer to https://uts.nlm.nih.gov/home.html -> *Request a License*.

This tool requires the full UMLS release, so please download the [Full UMLS Release Files](https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html).

### Prerequisites

### Installing

#### Extracting Relevant Data out of the UMLS Full Release

*TODO: MAKE SCRIPT AND CHANGE PATHS IN PARSER ACCORDINGLY*

```bash
mkdir umls-extract
mkdir umls-extract/META
mkdir umls-extract/NET
unzip umls-2019AA-full.zip
rm umls-2019AA-full.zip
unzip 2019AA-full/2019aa-1-meta.nlm
unzip 2019AA-full/2019aa-otherks.nlm
gunzip 2019AA-full/2019AA/META/MRCONSO.RRF.aa.gz
gunzip 2019AA-full/2019AA/META/MRCONSO.RRF.ab.gz
cat 2019AA-full/2019AA/META/MRCONSO.RRF.aa 2019AA-full/2019AA/META/MRCONSO.RRF.ab > umls-extract/META/MRCONSO.RRF
gunzip 2019AA-full/2019AA/META/MRDEF.RRF.gz
mv 2019AA-full/2019AA/META/MRDEF.RRF umls-extract/META/
gunzip 2019AA-full/2019AA/META/MRSTY.RRF.gz
mv 2019AA-full/2019AA/META/MRSTY.RRF umls-extract/META/
mv 2019AA-full/2019AA/NET/SRDEF umls-extract/NET/

rm -rf 2019AA-full/

```

## Usage

*TODO WRITE ME*

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/T0biWan/bachelor-frontend-prototype/tags).

## Authors

-   **Tom Oberhauser** - _Initial work_ - [GitHub](https://github.com/devfoo-one/)
