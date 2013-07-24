from util import next_

# START

elements = ['one', 'two', 'three']

idx = 1
for i in elements:
    idx += 1
    print "%s(%d)" % (i, idx)

next_()

for idx, i in enumerate(elements):
    print "%s(%d)" % (i, idx)

print ["%s(%d)" % (i, idx) for idx, i in enumerate(elements)]
gen = ("%s(%d)" % (i, idx) for idx, i in enumerate(elements))
print gen
print list(gen)

print range(10)
print xrange(10)
# generator. doesn't expand the list



# context managers
