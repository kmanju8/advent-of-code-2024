def inc_dic(d, key, v):
    if key in d:
        d[key].add(v)
    else:
        d[key] = set([v])


conn = {}


with open("input.txt", "r") as f:
    for line in f:
        connection = line.strip().split("-")
        inc_dic(conn, connection[0], connection[1])
        inc_dic(conn, connection[1], connection[0])


groups = {(k,): v for k, v in conn.items()}

while len(groups) > 1:
    print(len(groups))
    tempgroup = {}
    for nodetuple, connections in groups.items():
        for node2, connections2 in conn.items():
            if node2 not in nodetuple:
                if all([node2 in conn[c] for c in nodetuple]):
                    tempgroup[tuple(sorted(nodetuple + tuple([node2])))] = (
                        connections.intersection(connections2)
                    )

    groups = tempgroup

# print(groups)
for i in groups:
    print(",".join(list(i)))
