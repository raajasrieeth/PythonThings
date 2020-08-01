"""
Iterable:A python object on whom __iter__or __getitem__ method is defined
Iterator:A python object where __next__() is defined
Iteration:Method to iterate
"""
#generators:types of iterators which can be  traversed only once Ex:range() th
#once iterated, can't be iterated once again
#our own generator
def gen(n):
    for i in range(n):
        yield i#yield is a generator
#can use function. not used in code.
#iteration using__next__():
h='names'
ier=iter(h)
print(ier.__next__())#prints 'n'
print(ier.__next__())#a
print(ier.__next__())#m
print(ier.__next__())#e
print(ier.__next__())#s


