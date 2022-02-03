from dataclasses import dataclass
from typing import Dict


@dataclass(init=False, repr=True, eq=True)
class SemanticType:
    """TUI (field UI of SRDEF)"""
    __tui: str
    """Type of SemanticType STY / RL (field RT of SRDEF)"""
    __type: str
    """Definition (field DEF or SRDEF)"""
    __definition: str
    """Name of SemanticType (field STY_RL of SRDEF)"""
    __name: str

    def __init__(self, tui: str):
        self.__tui: str = tui
        self.__type: str = ''
        self.__definition: str = ''
        self.__name: str = ''

    def __add_srdef_data__(self, data: Dict):
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

    def __hash__(self):
        return hash(self.__tui)
