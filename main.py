import hashlib
import re
from itertools import chain, product
import multiprocessing as mp


def generateOutputs(charset, maxlength):
    print (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

    
    # example = ""
    # char_a = "a"
    # char_b = "a"
    # char_c = "a"
    # char_d = "a"
    # char_e = "a"
    # char_f = "a"

    # # if(char_a > 97 and char_a < 122):
    # #     chr(ord(char_a) + 1)
    
    # charArray = char_a + char_b + char_c + char_d + char_e + char_f
    # return
    

def findEnd(password):
    temp = ""
    binaryPassword = bin(len(password))
    reverse = binaryPassword[:1:-1]
    for i in range(len(reverse)):
        if reverse[i] == "0": temp += password[0]
        else: temp += "0"
    return temp

def main():
    temp = ""
    intermediate_0 = ""
    alternate_sum = ""
    magic = "$1$"
    salt = "hfT7jp2q"
    password = "test"
    goalState = "u3zPkglU5aB4J3suCZ3yA/"
    p = mp.Pool(30)

    # outputList = list(generateOutputs('abcdefghijklmnopqrstuvwxyz', 6))
   
    # ------------------------------------------------------------------------
    temp = password + salt + password
    alternate_sum = hashlib.md5(temp.encode('utf-8')).digest()
    sliceAlternate = str(alternate_sum[0:len(password)])
    intermediate_0 = password  + magic + salt + sliceAlternate + findEnd(password) 
    print(intermediate_0)
    intermediate_temp = hashlib.md5(intermediate_0).digest()
    test=hashlib.md5("dqdgiasnjgdiqdwj".encode("utf-8")).digest()
    print("test:")
    print(len(test))
    print(len(intermediate_temp))
    print(type(intermediate_temp))
    # intermediate_temp = solution
    for i in range(1000):
        solution = ""
        if i%2 == 0: solution += intermediate_temp
        if i%2 == 1: solution += password
        if i%3 != 0: solution += salt
        if i%7 != 0: solution += password
        if i%2 == 0: solution += password
        if i%2 == 1: solution += intermediate_temp
        solution = hashlib.md5(solution).digest()
        intermediate_temp = solution
        # print(i)

    # print(solution)
    # ------------------------------------------------------------------------
    p.close()
    p.join()
    #syntax
    # str(len(hashlib.md5(temp.encode('utf-8')).digest())) + "3"



if __name__ == "__main__":
    main()