def checking_tuple(tup):
    return all(tup)

tup = tuple(map(int,input().split()))

print(checking_tuple(tup))