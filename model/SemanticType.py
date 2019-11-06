class SemanticType:
    def __init__(self, tui: str):
        self.__tui = tui

    def __add_srdef_data__(self, data: dict):
        self.__type = data.get('RT')
        self.__name = data.get('STY_RL')
        self.__definition = data.get('DEF')

    def get_name(self) -> str:
        """
        :return: Name of Semantic Type
        """
        return self.__name

    def get_definition(self) -> str:
        """
        :return: Textual defintion of Semantic Type
        """
        return self.__definition