from umlsparser import UMLSParser
import matplotlib.pyplot as plt
import networkx as nx
from umlsparser.tools import networkx_utils

foo = UMLSParser("/home/toberhauser/DEV/Data/UMLS/2019AA-full/2019AA", language_filter=['ENG'])

semnet = foo.get_semantic_network()

root_nodes = networkx_utils.get_root_nodes(semnet)


for blub in semnet.predecessors(root_nodes[0]):
    print('{} - {}'.format(blub, foo.get_semantic_types().get(blub).get_name()))

print(foo)

