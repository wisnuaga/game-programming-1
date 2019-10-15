import random


def acak_kata(kata):
    string_acak = ""
    size = len(kata)
    list_index = random.sample(range(size), size)
    for item in list_index:
        string_acak += kata[item]
    return string_acak


kata_asli = input("input sebuah kata : ").upper()

flag = False
while not flag:
    print("================================")
    kata_acak = acak_kata(kata_asli)
    print("kata acak : " + kata_acak)
    tebakan = input("tebakan anda : ").upper()
    if kata_asli == tebakan:
        print("benar!")
        print(kata_asli)
        flag = True
    else:
        print("coba lagi!")
    print("================================")
