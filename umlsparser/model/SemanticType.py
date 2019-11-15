class SemanticType:
    def __init__(self, tui: str):
        """TUI (field UI of SRDEF)"""
        self.__tui: str = tui

        """Type of SemanticType STY / RL (field RT of SRDEF)"""
        self.__type: str = ''

        """Definition (field DEF or SRDEF)"""
        self.__definition: str = ''

        """Name of SemanticType (field STY_RL of SRDEF)"""
        self.__name: str = ''

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
