

def remove_dups(a):
    seen = 0
    new_list = []
    for ind, val in enumerate(a):
        if val != seen:
            new_list.append(val)
            seen = val
    print(new_list)
            






a = [2, 3, 5, 5, 7, 11, 11, 11, 13]
print(a)
remove_dups(a)

