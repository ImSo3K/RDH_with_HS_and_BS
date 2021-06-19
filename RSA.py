import random
from PIL import Image
from encode_decode import Encode, Decode
import math
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
          "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", ".", "!", "?", " "]
number = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
          "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]


def cipher(num, e):
    for i in range(len(num)):
        X.append((int(num[i])**e) % n)


def decipher(num, d):
    for i in range(len(num)):
        Y.append((int(num[i])**d) % n)


def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount


def Decrypt(fname):
    global i, j, Y
    Y = []
    encoded_image_file = './temp/' + 'enc_' + fname.split('/')[-1]
    img2 = Image.open(encoded_image_file)
    print(img2, img2.mode)
    hidden_text = Decode(img2)
    print(hidden_text)
    decipher(hidden_text, d)
    numD = []
    for i in range(len(Y)):
        for j in range(len(number)):
            if(Y[i] == int(number[j])):
                numD.append(letter[j])
    for i in numD:
        print(i, end="")
    print("\n")


def Encrypt(fname, plaintext):
    # encrypts a plaintext message using the current key
    global numC, j, X
    X = []
    plaintext = (plaintext.lower())
    numC = []
    for i in range(len(plaintext)):
        for j in range(len(letter)):
            if(plaintext[i] == letter[j]):
                numC.append(number[j])
    cipher(numC, e)
    print("Ciphertext:", X)
    print("Number of Ciphertext blocks:", len(X))
    original_image_file = fname
    img = Image.open(original_image_file)
    print(img, img.mode)
    encoded_image_file = "enc_" + original_image_file.split('/')[-1]
    img_encoded = Encode(img, plaintext, X)
    if img_encoded:
        img_encoded.save('./temp/' + encoded_image_file)
        print("{} saved!".format(encoded_image_file))


n = 2537
e = 13
d = 937
