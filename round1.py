import networkx as nx
import matplotlib.pyplot as plt


def plot(x, y, xlabel, ylabel):
    ymax = max(y)
    ymin = min(y)
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def inspect_graph(dataset):
    g = nx.read_edgelist(dataset, create_using=nx.Graph(), nodetype=int)
    directed_g = nx.read_edgelist(
        dataset, create_using=nx.DiGraph(), nodetype=int)

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('GRAPH INFORMATION for \n'+dataset)
    print(nx.info(g))
    n = g.number_of_nodes()
    # print(g.edges())

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('DEGREE CENTRALITY\n')
    print(nx.degree_centrality(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('EIGEN VECTOR CENTRALITY\n')
    print(nx.eigenvector_centrality(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('KATZ CENTRALITY\n')
    print(nx.katz_centrality(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('PAGERANK\n')
    print(nx.pagerank(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('BETWEENNESS CENTRALITY\n')
    print(nx.betweenness_centrality(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('CLOSENESS CENTRALITY\n')
    print(nx.closeness_centrality(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('LOCAL CLUSTERING COEFFICIENT\n')
    print(nx.clustering(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('AVERAGE CLUSTERING COEFFICIENT\n')
    print(nx.average_clustering(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('GLOBAL CLUSTERING COEFFICIENT\n')
    # triangles = sum(nx.triangles(g).values())
    traingles_set = {'210', '300', '120C', '030C', '120U', '030T', '120D'}
    open_traids_set = {'111D', '201', '021D', '111U', '021U', '021C'}
    traids_dict = nx.triadic_census(directed_g)
    open_traids = 0
    triangles = 0
    for key in traids_dict:
        if key in open_traids_set:
            open_traids += traids_dict[key]
        if key in traingles_set:
            triangles += traids_dict[key]

    GCC = (3 * triangles) / ((3 * triangles) + open_traids)
    print(GCC)

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('RECIPROCITY\n')
    print(nx.overall_reciprocity(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('TRANSITIVITY\n')
    print(nx.transitivity(g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('GIANT COMPONENT\n')
    n_g = 0
    for component in nx.connected_components(g):
        n_g = max(n_g, len(component))
    print('Size of the giant component - ' + str(n_g))

    print('\n----------------------------------------------------------------------------------------------------------------------\n')
    print('PLOT\n')
    x = []
    y = []
    k = 0
    while(k <= 5):
        x.append(k)
        p = k / n
        g_random = nx.gnp_random_graph(n, p)
        random_n = g_random.number_of_nodes()
        random_n_g = 0
        for component in nx.connected_components(g_random):
            random_n_g = max(random_n_g, len(component))
        y.append(random_n_g / random_n)

        k += 0.1

    # print(x)
    # print(y)

    plot(x, y, "Average Degree", "N_G/N ratio")
    print('\n----------------------------------------------------------------------------------------------------------------------\n')


inspect_graph("dataset1.txt")
inspect_graph("dataset2.txt")
