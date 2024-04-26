from Algorithm.Bernstein import *

algo = Bernstein()

fds = FDList()
""" 
# P -> {G, S}
fds.add_fd(FD(frozenset(['P']), frozenset(['G', 'S'])))

# {G, S} -> P
fds.add_fd(FD(frozenset(['G', 'S']), frozenset(['P'])))

# {P, I} -> O
fds.add_fd(FD(frozenset(['P', 'I']), frozenset(['O'])))

# {G, I} -> P
fds.add_fd(FD(frozenset(['G', 'I']), frozenset(['P'])))

# {G, I} -> S
fds.add_fd(FD(frozenset(['G', 'I']), frozenset(['S'])))

# {P, G, S} -> E
fds.add_fd(FD(frozenset(['P', 'G', 'S']), frozenset(['E'])))

# {G, S, I} -> O
fds.add_fd(FD(frozenset(['G', 'S', 'I']), frozenset(['O'])))
 """

fds.add_fd(FD(frozenset('P'), frozenset(['G'])))
fds.add_fd(FD(frozenset('P'), frozenset(['S'])))
fds.add_fd(FD(frozenset('GS'), frozenset(['P'])))
fds.add_fd(FD(frozenset('PI'), frozenset(['O'])))
fds.add_fd(FD(frozenset('GI'), frozenset(['S'])))
fds.add_fd(FD(frozenset('GI'), frozenset(['O'])))
fds.add_fd(FD(frozenset('P'), frozenset(['E'])))

algo.compute(fds)

relations = algo.get_relations()
print(Bernstein.get_print_relations_info(relations))