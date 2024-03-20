def inva(d):
    r = {}
    for key, value in zip(d.keys(), d.values()):
        print("ola r ", r)
        if value in r:
            print("oi",r)
            r[value].append(key)
        else:
            r[value] = [key]
    return r

teste1 = {1:2, 3:1, 4:1}
teste2 = {2:1, 1:2}

print(inva(teste1))
# print(inva(teste2))
