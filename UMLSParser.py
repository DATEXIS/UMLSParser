import collections
import os


class UMLSParser:

    def __init__(self, path: str):
        self.paths = {
            'MRCONSO': path + os.sep + 'META' + os.sep + 'MRCONSO.RRF'
        }
        self.languages = ['GER', 'ENG']  # languages to extract
        self.concepts = {}
        self.__parse_concepts__()

    def __parse_concepts__(self):
        # https://www.ncbi.nlm.nih.gov/books/NBK9685/table/ch03.T.concept_names_and_sources_file_mr/
        for line in open(self.paths['MRCONSO']):
            line = line.split('|')
            lat = line[1]  # language of term
            if lat not in self.languages:
                continue
            cui = line[0]  # concept identifier
            if cui in self.concepts.keys():
                concept = self.concepts.get(cui)
            else:
                concept = Concept(cui)
                self.concepts[cui] = concept

            concept.add_data({
                'lat': lat,
                'str': line[14],
                'ts': line[2]  # term status see https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html
            })


class SemanticType:
    def __init__(self, id: str):
        self.id = id


class Concept:
    def __init__(self, cui: str):
        self.cui = cui
        self.descriptions = collections.defaultdict(set)

    def add_data(self, data: dict):
        """
        Adds data to a concept, mostly used during the parsing of an MRCONSO.RRF file.
        :param data: certain fields out of an MRCONSO.RRF file (lat, str)
        :return:
        """
        self.descriptions[data['lat']].add(data['str'])

