import collections


class Concept:
    def __init__(self, cui: str):
        self.__cui = cui
        self.__tui = None
        self.__preferred_names = collections.defaultdict(set)
        self.__all_names = collections.defaultdict(set)
        self.__definitions = set()

    def __add_mrconso_data__(self, data: dict):
        """
        Adds data to a concept, mostly used during the parsing of an MRCONSO.RRF file.
        :param data: certain fields out of an MRCONSO.RRF file (lat, str)
        :return:
        """
        self.__all_names[data['LAT']].add(data['STR'])
        if data['TS'] == 'P':
            self.__preferred_names[data['LAT']].add(data['STR'])

    def __add_mrdef_data__(self, data: dict):
        self.__definitions.add((data.get('DEF'), data.get('SAB')))

    def __add_mrsty_data__(self, data: dict):
        self.__tui = data.get('TUI')

    def get_preferred_names_for_language(self, lang: str) -> list:
        """
        Returns a set of every concept name that was marked as preferred in MRCONSO.RRF.
       :param lang: Language
       :return: Set of names
       """
        return list(self.__preferred_names.get(lang, []))

    def get_definitions(self) -> set:
        """
        Returns all found definitions for this concept.
        :return: Set of tuples (definition, source)
        """
        return self.__definitions

    def get_cui(self) -> str:
        """
        :return: CUI
        """
        return self.__cui

    def get_tui(self) -> str:
        """
        :return: Semantic Type Identifier
        """
        return self.__tui

    def __str__(self):
        preferred_english_name = ''
        try:
            preferred_english_name = self.get_preferred_names_for_language('ENG')[0]
        except IndexError:
            pass
        return "{} ({})".format(preferred_english_name, self.get_cui())
