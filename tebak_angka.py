import random

chance = 3
rand_number = random.randint(10, 100)

print("cheat : " + str(rand_number))
while chance > 0:
    tebakan = int(input("Silahkan tebak angka 10-100 : "))
    if tebakan == rand_number:
        print("Selamat tebakan anda benar!")
        break
    else:
        if tebakan > rand_number:
            print("Tebakan anda terlalu besar!\nSilahkan coba lagi")
        elif tebakan < rand_number:
            print("Tebakan anda terlalu kecil!\nSilahkan coba lagi")
        chance -= 1
        print("sisa nyawa anda : " + str(chance))
