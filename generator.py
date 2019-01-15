from itertools import chain, product
import multiprocessing as mp

def generateOutputs(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

# print(list(generateOutputs('abcdefghijklmnopqrstuvwxyz', 3)))
p = mp.Pool(30)

with open('genText.txt', 'w') as f:
    for item in list(generateOutputs('abcdefghijklmnopqrstuvwxyz', 6)):
        f.write("%s\n" % item)

p.close()
p.join()