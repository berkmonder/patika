str = '%Bak çuvalı-kaşık*bot,çim..'
no = [*'*.,- %']  # içinde olmasını istemediğimiz özel karakterler


def ayir(*args):
    lst = []
    kelime = 0
    for i in args[0]:
        if i not in no:
            if kelime == 1:
                i = i.upper()
                kelime = 0
            lst.append(i)
        else:
            kelime = 1
    if len(args[0]) != 0:
        lst[0] = lst[0].lower()
    return ''.join(lst)


print(ayir(str))
