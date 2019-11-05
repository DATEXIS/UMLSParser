import collections
import logging
import os

from tqdm import tqdm

UMLS_sources_by_language = {
    'ENG': ['MSH', 'CSP', 'NCI', 'PDQ', 'NCI_NCI-GLOSS', 'CHV', 'NCI_CRCH', 'NCI_CareLex', 'UWDA', 'FMA',
            'NCI_CDISC-GLOSS', 'NCI_NICHD', 'NCI_CTCAE', 'HPO', 'MEDLINEPLUS', 'NCI_CDISC', 'NCI_FDA', 'NCI_GAIA',
            'HL7V3.0', 'PSY', 'SPN', 'AIR', 'GO', 'CCC', 'SNOMEDCT_US', 'UMD', 'NIC', 'ALT', 'NCI_EDQM-HC', 'JABL',
            'NUCCPT', 'LNC', 'ICF-CY', 'NCI_BRIDG', 'ICF', 'NDFRT', 'NANDA-I', 'PNDS', 'NOC', 'OMS', 'NCI_CTEP-SDC',
            'NCI_DICOM', 'NCI_KEGG', 'NCI_BioC', 'MCM', 'AOT', 'NCI_CTCAE_5', 'NCI_CTCAE_3', 'MDR', 'NCI_INC'],
    'SPA': ['MDRSPA', 'SCTSPA', 'MSHSPA'],
    'FRE': ['MDRFRE', 'MSHFRE'],
    'JPN': ['MDRJPN'],
    'CZE': ['MDRCZE', 'MSHCZE'],
    'ITA': ['MDRITA'],
    'GER': ['MDRGER'],
    'POR': ['MDRPOR', 'MSHPOR'],
    'DUT': ['MDRDUT'],
    'HUN': ['MDRHUN'],
    'NOR': ['MSHNOR'],
    'HRV': ['MSHSCR']  # not sure
}


class UMLSParser:
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, path: str, language_filter: list = []):
        """
        :param path: Basepath to UMLS data files
        :param languages: List of languages with three-letter style language codes (if empty, no filtering will be applied)
        """
        logging.info("Initialising UMLSParser for basepath {}".format(path))
        if language_filter:
            logging.info("Language filtering for {}".format(",".join(language_filter)))
        else:
            logging.info("No language filtering applied.")
        self.paths = {
            'MRCONSO': path + os.sep + 'META' + os.sep + 'MRCONSO.RRF',
            'MRDEF': path + os.sep + 'META' + os.sep + 'MRDEF.RRF'
        }
        self.language_filter = language_filter
        self.concepts = {}
        self.__parse_mrconso__()
        self.__parse_mrdef__()

    def __parse_mrconso__(self):
        # https://www.ncbi.nlm.nih.gov/books/NBK9685/table/ch03.T.concept_names_and_sources_file_mr/
        logging.info('Parsing UMLS concepts...')
        for line in tqdm(open(self.paths['MRCONSO'])):
            line = line.split('|')
            data = {
                'cui': line[0],  # concept identifier
                'lat': line[1],  # language of term
                'str': line[14],
                'ts': line[2]
                # term status https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/abbreviations.html
            }

            if len(self.language_filter) != 0 and data.get('lat') not in self.language_filter:
                continue
            concept = self.concepts.get(data.get('cui'), Concept(data.get('cui')))
            concept.__add_mrconso_data__(data)
            self.concepts[data.get('cui')] = concept
        logging.info('Found {} unique CUI´s'.format(len(self.concepts.keys())))

    def __parse_mrdef__(self):
        logging.info('Parsing UMLS definitions...')

        source_filter = []
        for language in self.language_filter:
            for source in UMLS_sources_by_language.get(language):
                source_filter.append(source)

        for line in tqdm(open(self.paths['MRDEF'])):
            line = line.split('|')
            data = {
                'cui': line[0],
                'source': line[4],
                'definition': line[5]
            }
            if len(self.language_filter) != 0 and data.get('source') not in source_filter:
                continue
            concept = self.concepts.get(data['cui'], Concept(data['cui']))
            concept.__add_mrdef_data__(data)
            self.concepts[data.get('cui')] = concept

    def get_concepts(self):
        return self.concepts

    def get_languages(self):
        return self.language_filter


class SemanticType:
    def __init__(self, id: str):
        self.id = id


class Concept:
    def __init__(self, cui: str):
        self.cui = cui
        self.preferred_names = collections.defaultdict(set)
        self.all_names = collections.defaultdict(set)
        self.descriptions = set()

    def __add_mrconso_data__(self, data: dict):
        """
        Adds data to a concept, mostly used during the parsing of an MRCONSO.RRF file.
        :param data: certain fields out of an MRCONSO.RRF file (lat, str)
        :return:
        """
        self.all_names[data['lat']].add(data['str'])
        if data['ts'] == 'P':
            self.preferred_names[data['lat']].add(data['str'])

    def __add_mrdef_data__(self, data: dict):
        self.descriptions.add((data.get('definition'), data.get('source')))

    def get_preferred_names_for_language(self, lang: str) -> set:
        """

       :param lang:
       :return:
       """
        return self.preferred_names.get(lang)

    def get_definitions(self) -> set:
        """

        :return:
        """
        return self.descriptions
