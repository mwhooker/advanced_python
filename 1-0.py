from read import main
import os
import sys

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

# context managers

next_()
