from umlsparser import UMLSParser
import matplotlib.pyplot as plt
import networkx as nx


foo = UMLSParser("/home/toberhauser/DEV/Data/UMLS/2019AA-full/2019AA", language_filter=['ENG'])

semnet = foo.get_semantic_network()
nx.draw(semnet)
plt.show()
print("foo")