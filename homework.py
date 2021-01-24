"""
Task 1
Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function
"""


def with_index(iterable, start=0):
    for i in iterable:
        yield start, i
        start += 1


if __name__ == "__main__":
    my_list = ["a", 2, "d", "gg"]
    print(list(with_index(my_list)))
#


"""
Task 2
Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
 `start`, `end`, and optional step. Tips: See the documentation for `range` function
"""


def in_range(start, end, step=1):
    i = start
    if step > 0:
        while i < end:
            yield i
            i += step
    else:
        while i > end:
            yield i
            i += step


if __name__ == "__main__":
    print(list(in_range(10, 1, -2)))

"""
Task 3
Create your own implementation of an iterable, which could be used inside for-in loop.
 Also, add logic for retrieving elements using square brackets syntax.
"""
b = (i ** 2 for i in in_range(1, 100))
for i in b:
    print(i)
c = [i ** 2 for i in in_range(1, 10)]
print(c)
