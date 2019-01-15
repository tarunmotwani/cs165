import hashlib
import re
from itertools import chain, product


# team7:$1$hfT7jp2q$u3zPkglU5aB4J3suCZ3yA/:16653:0:99999:7:::


def generateOutputs(charset, maxlength):
    return (''.join(candidate)
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
    

def findBytes(password):
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
    
    # outputList = list(generateOutputs('abcdefghijklmnopqrstuvwxyz', 6))
   
    # ------------------------------------------------------------------------
    temp = password + salt + password
    alternate_sum = hashlib.md5(temp.encode('utf-8')).digest()
    sliceAlternate = str(alternate_sum[0:len(password)])
    intermediate_0 = password  + magic + salt + sliceAlternate + findBytes(password) 
    print(intermediate_0)
    solution = str(hashlib.md5(intermediate_0.encode('utf-8')).digest())
    intermediate_temp = solution
    for i in range(1000):
        if i%2 == 0: solution += intermediate_temp
        if i%2 == 1: solution += password
        if i%3 != 0: solution += salt
        if i%7 != 0: solution += password
        if i%2 == 0: solution += password
        if i%2 == 1: solution += intermediate_temp
        intermediate_temp = solution
        solution = str(hashlib.md5(solution.encode('utf-8')).digest())
        print(i)

    print(len(solution))
    # ------------------------------------------------------------------------



    # str(len(hashlib.md5(temp.encode('utf-8')).digest())) + "3"



if __name__ == "__main__":
    main()