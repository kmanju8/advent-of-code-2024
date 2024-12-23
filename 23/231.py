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


# print(conn)
def contains_t(l):
    for s in l:
        if s[0] == "t":
            return True
    return False


groups = set()
for node, connections in conn.items():
    for c in connections:
        for d in conn[c]:
            if node in conn[d]:
                temp = [node, c, d]
                temp.sort()
                groups.add(tuple(temp))

print(len(groups))

print(len([x for x in groups if contains_t(x)]))
