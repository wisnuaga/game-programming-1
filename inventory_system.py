import random

list_item = [["Pisau", "3"], ["Golok", "4"], ["Celurit", "4"], ["Pedang", "7"], ["Pistol", "10"], ["Geranat", "9"],
             ["Bom", "15"], ["Tombak", "8"]]
inventory = []


def show_item(list_input, max_capacity):
    if len(list_input) == 0:
        print("Inventory Kosong!")
        return False
    for i in range(int(max_capacity)):
        if i < len(list_input):
            print(str(i + 1) + ". nama: " + list_input[i][0] + " | stat: " + list_input[i][1])
        else:
            print(str(i + 1) + ". ")


def get_item():
    rand_item = list_item[random.randrange(0, len(list_item))]
    print("* nama: " + rand_item[0] + " | stat: " + rand_item[1])
    return rand_item


def del_item(list_input, max_capacity):
    show_item(list_input, max_capacity)
    if len(list_input) == 0:
        return False
    del_index = input("item yang dihapus : ")
    index = int(del_index) - 1
    if index >= len(list_input) or index < 0:
        print("Salah mencet kowe bos!")
        return False
    del list_input[index]
    show_item(list_input, max_capacity)


max_inv = input("Masukkan ukuran inventory : ")

flag = 'y'
print("Ukuran inventory anda : " + str(max_inv))
while flag == 'y':
    print("=== Menu Inventory ===")
    print("1. Tampil Item")
    print("2. Tambah Item")
    print("3. Hapus Item")
    command = input("pilih menu : ")
    if command == '1':
        show_item(inventory, max_inv)
    if command == '2':
        if len(inventory) >= int(max_inv):
            print("Inventory penuh!")
        else:
            inventory.append(get_item())
    if command == '3':
        del_item(inventory, max_inv)

    flag = input("mau lanjut lagi? [y/n] : ")
