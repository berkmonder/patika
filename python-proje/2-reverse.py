def reverse(lst):
    lst.reverse()
    for i in lst:
        if isinstance(i, list):
            reverse(i)
        else:
            continue
    return lst

print(reverse([[1, 2], [3, 4], [5, 6, 7]]))

""" output
[[7, 6, 5], [4, 3], [2, 1]]
[Finished in 0.132s]
"""
