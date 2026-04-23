#1
def common_elements(a, b):
    return list(set(a) & set(b))


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(common_elements(a, b))


#2
def remove_duplicates(s): 
    seen = set()
    result = []

    for x in s: 
        if x not in seen:
            seen.add(x)
            result.append(x)

    return result

#3
def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)