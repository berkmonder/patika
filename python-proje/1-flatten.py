l=[]
def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            flatten(i)
        else:
            l.append(i)
    return l

print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))

""" output:
[1, 'a', 'cat', 2, 3, 'dog', 4, 5]
[Finished in 0.102s]
"""
