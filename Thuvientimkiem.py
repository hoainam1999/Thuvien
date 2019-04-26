# Dữ liệu gốc
database = {
    'home': 'Ngôi nhà',
    'baby': 'Em bé'
}

def show_menu():
    print("------------------")
    print("-TỪ ĐIỂN TÌM KIẾM-")
    print("------------------")
    print("1. Thêm từ")
    print("2. Tìm từ")
    print("3. Xóa từ")
    print("4. Xem tất cả")
    print("Ấn 0 để thoát chương trình")
    print("------------------")

def add():
    word = input("Nhập từ mới: ")
    mean = input("Dịch nghĩa: ")
    database[word] = mean
    print("* Từ mới vừa được thêm: ", word)

def find():
    word = input("Nhập từ cần tìm kiếm: ")
    if word in database:
        print("[%s: %s]" % (word, database[word]))
    else:
        print("Không tìm thấy từ:  [%s]" % (word))

def delete():
    word = input("Nhập từ cần xóa: ")
    if word in database:
        del database[word]
        print("Xóa thành công từ [%s]" % word)
    else:
        print("Từ [%s] không có sẵn" % word)
def view_all():
    for word, mean in database.items():
        print("[ %s: %s]" % (word, mean))

# Hiện Menu
show_menu()

# Chương trình chính
choice = int(input("Bạn muốn làm gì: "))
while choice != 0:
    if choice == 0:
        break
    elif choice == 1:
        add()
    elif choice == 2:
        find()
    elif choice == 3:
        delete()
    elif choice == 4:
        view_all()
    else:
        print("Lựa chọn không phù hợp!")
    choice = int(input("Bạn muốn làm gì: "))
print("Hẹn gặp lại!")