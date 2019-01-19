from itertools import chain, product
import multiprocessing as mp
import re

def generateOutputs(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

# print(list(generateOutputs('abcdefghijklmnopqrstuvwxyz', 3)))

def main():
        p = mp.Pool(4)
        with open('genTextBonus.txt', 'w') as f:   
                for item in list(generateOutputs('abcdefghijklmnopqrstuvwxyz', 6)):
                        # if item[0] == "h":
                        f.write("%s\n" % item)
        p.close()
        p.join()

if __name__ == "__main__":
    main()