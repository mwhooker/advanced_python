from read import main
import os

rows, columns = os.popen('stty size', 'r').read().split()

source = main()

def next_():
    raw_input()
    print "%c[2J" % (27)
    print source.next()
    print "\n%s\n" % ("-" * int(columns))


next_()
# START

elements = ['one', 'two', 'three']

idx = 1
for i in elements:
    idx += 1
    print "%s(%d)" % (i, idx)


for idx, i in enumerate(elements):
    print "%s(%d)" % (i, idx)


next_()
# generator doesn't expand the list

print range(10)
print xrange(10)

next_()

print ["%s(%d)" % (i, idx) for idx, i in enumerate(elements)]
gen = ("%s(%d)" % (i, idx) for idx, i in enumerate(elements))
print gen
print list(gen)

next_()

# context managers
