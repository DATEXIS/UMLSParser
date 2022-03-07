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
mv 2019AA-full/2019AA/NET/SRSTRE1 umls-extract/NET/

rm -rf 2019AA-full/

```

## Usage

*TODO WRITE ME*
### Examples

#### Getting all concepts that have a ICD10CM identifier

```python
from umlsparser import UMLSParser

umls = UMLSParser('/home/toberhauser/DEV/Data/UMLS/2017AA-full/2017AA')

for cui, concept in umls.get_concepts().items():
    if 'ICD10CM' in concept.get_source_ids().keys():
        icd10ids = concept.get_source_ids().get('ICD10CM')
        print(icd10ids, concept.get_preferred_names_for_language('ENG')[0])
```

#### Generate a table for the distribution of all english UMLS sources

```python
from umlsparser import UMLSParser
import collections

umls = UMLSParser('/home/toberhauser/DEV/Data/UMLS/2017AA-full/2017AA')
sources_counter = collections.defaultdict(int)
for cui, concept in umls.get_concepts().items():
    sources = concept.get_source_ids().keys()
    for source in sources:
        sources_counter[source] += 1
print('|SOURCE|COUNT|\n|------|-----|')
for source, count in sorted(sources_counter.items(), key=lambda t: t[1], reverse=True):
    print('|{}|{}|'.format(source, count))

```

#### Generate a list of all english concept names and their semantic category

```python
from umlsparser import UMLSParser

umls = UMLSParser('/home/toberhauser/DEV/Data/UMLS/2017AA-full/2017AA')

for cui, concept in umls.get_concepts().items():
    tui = concept.get_tui()
    name_of_semantic_type = umls.get_semantic_types()[concept.get_tui()].get_name()
    for name in concept.get_names_for_language('ENG'):
        print(cui, name, tui, name_of_semantic_type)
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/DATEXIS/UMLSParser/tags).

## Authors

-   **Tom Oberhauser** - _Initial work_ - [GitHub](https://github.com/devfoo-one/)
