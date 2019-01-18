import hashlib
import re
from itertools import chain, product
import multiprocessing as mp


# def generateOutputs(charset, maxlength):
#     # return (''.join(candidate)
#     #     for candidate in chain.from_iterable(product(charset, repeat=i)
#     #     for i in range(1, maxlength + 1)))
#     # for i in range(maxlength):
#     return
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
    

def findEnd(intermediate_0, password):
    temp = ""
    binaryPassword = bin(len(password))
    reverse = binaryPassword[:1:-1]
    for i in range(len(reverse)):
        if reverse[i] == "0": intermediate_0.update(password[0].encode())
        else: intermediate_0.update(chr(0).encode())
    return intermediate_0

def main():
    temp = ""
    arr = []
    intermediate_0 = ""
    alternate_sum = ""
    magic = "$1$"
    salt = "hfT7jp2q"
    password = "aaaaaa"
    passArray = ['a','a','a','a','a','a']
    goalState = "KyYIVk1b7GbGnSPxu1q911"
    crypt = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    goalString = ""
    p = mp.Pool(4)
    finalCrypt = ""
    maxLength = 6
    f = open("genText.txt", 'r')

    while(finalCrypt != goalState):
        # password = generateOutputs('abcdefghijklmnopqrstuvwxyz', 6)
        
        #ITERATOR
        content = f.readline()
        content = [x.strip() for x in content] 
        password = "".join(content)
        # password = "hmbthw"
        print(password)
        # for i in range(6):
            
        #     if(passArray[0] == 'z'):
        #         passArr[i] += 1
        # print(passArray)
        #HASHING
        # ------------------------------------------------------------------------
        temp = password + salt + password
        alternate_sum = hashlib.md5(temp.encode()).digest()
        print(alternate_sum)
        sliceAlternate = alternate_sum[0:len(password)]
        intermediate_0 = hashlib.md5((password  + magic + salt).encode())
        intermediate_0.update(sliceAlternate)
        intermediate_0 = findEnd(intermediate_0, password)
        
        # intermediate_temp = hashlib.md5(intermediate_0.encode()).digest()
        
        # print(intermediate_0.digest())
        
        # test=hashlib.md5("dqdgiasnjgdiqdwj".encode("utf-8")).digest()
        # print("test:")
        # print(len(test))
        # print(len(intermediate_temp))
        # print(type(intermediate_temp))
        intermediate_temp = intermediate_0.digest()
        for i in range(1000):
            solution = ""
            if i%2 == 0: solution = hashlib.md5(intermediate_temp)
            if i%2 == 1: solution = hashlib.md5(password.encode())
            if i%3 != 0: solution.update(salt.encode())
            if i%7 != 0: solution.update(password.encode())
            if i%2 == 0: solution.update(password.encode())
            if i%2 == 1: solution.update(intermediate_temp)
            # solution = hashlib.md5(solution.encode()).digest()
            intermediate_temp = solution.digest()
            # print(i)
        print(intermediate_temp)
        # print(len(intermediate_temp))
        goalArray = []
        arr = [11, 4, 10, 5, 3, 9, 15, 2, 8, 14, 1, 7, 13, 0, 6, 12]
        for i in range(len(arr)): goalArray.append(str(bin(intermediate_temp[arr[i]]))[2:].zfill(8))
        # print(goalArray)
        # for i in range(len(goalArray)): goalString += goalArray[i]

        goalString = "".join(goalArray)

        # print(goalString)
        output = ""
        # n = 6
        # remainder = len(goalString)%6
        # goalString = goalString[2:]
        # for i in range(0, len(goalString), n):
        #     sol = goalString[i:i+n] 
        #     index = int(sol, 2)
        #     output += crypt[index]
        # output += crypt[int(goalString[0:remainder],2)]
        # print(output)

        out_hash = ""
        remainder = len(goalString) % 6
        split = int(len(goalString) / 6)

        #print("bitlength: " + str(len(bits)))
        #print("lo: " + str(leftover) + "   g: " + str(split))

        for i in range(split): out_hash += crypt[int(goalString[int(128 - ((i + 1)*6)):int(128 - (i*6))],2)]
        out_hash += crypt[int(goalString[0:remainder],2)]
        print("OUTPUT: ", out_hash)
        if(out_hash == goalState):
            print("We got em boys!", out_hash)
            break
        # break
        # split = int(len(goalString)/6)
        # for i in range(split):
            
        # ------------------------------------------------------------------------
    p.close()
    p.join()
    
        #syntax
        # str(len(hashlib.md5(temp.encode('utf-8')).digest())) + "3"
        
        
        



if __name__ == "__main__":
    main()
