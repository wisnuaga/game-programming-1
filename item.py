inventory = []


def prev_item(tas):
    if len(tas) <= 1:
        return "Kosong!"
    else:
        return tas[len(tas) - 1]


def get_item():
    item = input("Masukkan nama item : ")
    stat = input("Masukkan stat item : ")
    return [item, stat]


def weakest_item(tas):
    weak_item = tas[0]
    for i in range(len(tas)):
        if weak_item[1] > tas[i][1]:
            weak_item = tas[i]
    return weak_item


def strongest_item(tas):
    weak_item = tas[0]
    for i in range(len(tas)):
        if weak_item[1] < tas[i][1]:
            weak_item = tas[i]
    return weak_item


flag = 'y'
while flag == 'y':
    item_baru = get_item()
    inventory.append(item_baru)
    print("Item sebelumnya : " + str(prev_item(inventory)))
    print("Item terlemah : " + str(weakest_item(inventory)))
    print("Item terkuat : " + str(strongest_item(inventory)))

    flag = input("mau lanjut lagi? [y/n] : ")
