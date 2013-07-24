from read import main
import os
import sys
import itertools

rows, columns = os.popen('stty size', 'r').read().split()

source = main()

previous = None
def next_():
    global previous
    if len(sys.argv) != 2:
        raw_input()
        print "%c[2J" % (27)
    try:
        print source.next()
    except StopIteration:
        return
    print "\n%s\n" % ("-" * int(columns))

next_()
# START

# getting help

help(set)

next_()

# built-ins

# sets

set1 = set([1, 2, 3, 3])
set2 = set([2, 3, 4])

print set1 == set2
print set1 - set2
print set1.union(set2)
print set1.symmetric_difference(set2)


next_()
# batteries included

import heapq, random
elements = range(10)
print elements
random.shuffle(elements)
print elements
heapq.heapify(elements)
print elements


next_()

# collections
import collections
# defaultdict
dd = collections.defaultdict(list)
dd['matt'].append('so cool')
dd['matt'].append('so smooth')
dd['matt'].append('so fresh')
print dd['matt']
print dd['tom']

next_()

# namedtuple

People = collections.namedtuple('People', ['fields', 'of', 'people'])
new_person = People('people', 'of', 'fields')
print new_person.fields


next_()

# deque (say 'deck')
# efficient, double-ended queue
d = collections.deque('ghi')
d.append('j')
d.appendleft('f')
print d


next_()
# ABC - abstract base class

next_()

elements = ['one', 'two', 'three']

idx = 0
for i in elements:
    print "%s(%d)" % (i, idx)
    idx += 1

next_()

for idx, i in enumerate(elements):
    print "%s(%d)" % (i, idx)


next_()
# generator doesn't expand the list

print range(10)
print xrange(10)

next_()

# list comprehension

print ["%s(%d)" % (i, idx) for idx, i in enumerate(elements)]

next_()

# generator comprehension

gen = ("%s(%d)" % (i, idx) for idx, i in enumerate(elements))

print gen
print list(gen)

next_()

# generators

def mygenerator():
    yield "before"
    for i in xrange(3):
        yield i
    yield "after"

for i in mygenerator():
    print i

print list(mygenerator())

next_()

# itertools

print list(itertools.islice(mygenerator(), 1, 4))

next_()

def myfilter(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

print list(itertools.ifilter(myfilter, mygenerator()))
print list(itertools.ifilterfalse(myfilter, mygenerator()))


# generators are a form of continuation. they facilitate coroutines.

next_()

# protocols

# iterator

# __dunder__ "magic methods"

class MyIterator(object):

    def __init__(self, high):
        self.current = 0
        self.high = high

    def __iter__(self):
        return self

    def next(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for i in MyIterator(3):
    print i

next_()

# decorators

def mydecorator(f):
    def inside():
        print "before dec"
        f()
        print "after_dec"

    return inside

@mydecorator
def test():
    print "inside"

test()

next_()

# descriptors
# http://docs.python.org/2/reference/datamodel.html#descriptors

class ReadOnly(object):

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __set__(self, obj, val):
        raise AttributeError('%s is read only.' % self.name)

class MyClass(object):
    x = ReadOnly(10, 'var "x"')
    y = 5


test = MyClass()
test.y = "z"
try:
    test.x = "y"
except AttributeError, e:
    print "%s(%s)" % (e.__class__.__name__, e)


next_()

# context managers

class Ctx(object):
    def __enter__(self):
        print "entering"

    def __exit__(self,  type, value, traceback):
        print "exiting"

with Ctx():
    print "inside!"

next_()

# contextlib
from contextlib import contextmanager

@contextmanager
def ctx():
    print "before"
    yield
    print "after"

with ctx():
    print "also inside."


next_()


# attributes

class Attr1(object):
    pass

x = Attr1()
x.y = 1 
print x.y
next_()

class Attr2(object):

    # caled only when attribute lookup fails
    def __getattr__(self, attr):
        return "%s not found" % attr


x = Attr2()
x.y = 1
print x.y
print x.z

# we'll come back to this
print x.__dict__
next_()


class DangerAttr(object):

    # caled always to look up attribute.
    def __getattribute__(self, attr):
        return "%s not found" % attr

x = DangerAttr()
x.y = 1
print x.y
print x.z

next_()

# everything is an object.

def testf():
    pass

testf.permavalue = 1

print testf.__dict__

class X(object):
    y = 2

X.classattr = 1
print X.__dict__

x = X()
# __getattr__ has a lookup list. first the instance and then the class tree
print x.__dict__
print x.y

# functions, classes, instances, all objects, behaving alike

next_()
# metaclasses

next_()
