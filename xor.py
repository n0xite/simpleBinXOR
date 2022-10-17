from getopt import getopt
import random
import string
import sys



#GET ARGUMENTS FROM CLI

PT = ''.join(sys.argv[1:])
global key
key = ""
file = []

with open(PT, "rb") as f:
    while (byte := f.read(1)):
        file.append(byte)



#Generate one time key ,same length as data
def OTKgen(length):
    chars = string.ascii_letters + string.digits
    result_str = "".join(random.choice(chars) for i in range(length))
    print('Key: ', result_str)
    key = result_str
    return key

#XOR the data and the key
def XOR(a, b):
    
    output = ""
    key = OTKgen(len(file))

    for i in range(len(file)):
        cur = file[i] #Inserted Data
        cur_key = key[i % len(key)] #Max length
        output += chr(ord(cur) ^ ord(cur_key)) #XOR
    return output

    






 #Len for a key to generate

CT = XOR(file,key) 
print('Xored: ' + '0x' + ', 0x'.join(hex(ord(x))[2:] for x in CT))




