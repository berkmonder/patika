l = '%Bak çuvalı-kaşık*bot,çim..'
no = [*'*.,- %']  # içinde olmasını istemediğimiz özel karakterler


def ayir(*lst):
    bok = []
    kelime = 0
    for i in lst[0]:
        if i not in no:
            if kelime == 1:
                i = i.upper()
                kelime = 0
            bok.append(i)
        else:
            kelime = 1
    bok[0] = bok[0].lower()
    return ''.join(bok)


print(ayir(l))
