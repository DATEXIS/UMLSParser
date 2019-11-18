import networkx as nx


def get_root_nodes(network: nx.MultiDiGraph) -> list:
    return [node for node in network.nodes if len(list(network.successors(node))) == 0]
