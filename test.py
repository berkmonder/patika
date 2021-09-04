def decorator_func(func):
    def wrapper_func(*args):
        print(f"name of the function is {func.__name__}")
        return func(*args)

    return wrapper_func


@decorator_func
def func(name, number):
    print(f"Name: {name}, Number: {number}")


func("jack", 123)

########################################################


def wrapper(f):
    def fun(l):
        return f('+91 ' + i[-10:-5] + ' ' + i[-5:] for i in l)
    return fun


@ wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


l = ['07895462130', '919875641230', '9195969878']
sort_phone(l)


########################################################


def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
