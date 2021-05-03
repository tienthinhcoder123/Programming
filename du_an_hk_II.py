maSoAo = [1, 2, 3]
tenAo = ["vay", "dam", "ao thun"]
giaAo = [15000, 42314, 3525321]
tenKhachHangMuaAo = ["Thinh", "Trump", "Biden"]
ngayNhapAo = ["24/3/1234", "31/3/243", '12/12/2021']
sapxepThuTu = []

# ham them
def them():
    print("THÊM THÔNG TIN")
    maSo = input("Nhập mã số áo: ")
    ten = input("Nhập tên áo: ")
    gia = input("Nhập giá bán áo: ")
    tenKhach = input("Nhập tên khách hàng mua áo: ")
    ngayNhap = input("Nhập ngày nhập áo: ")
    #maSo
    try:
        int(maSo ** (1 / 2))
    except:
        while int(maSo) < 0 or len(maSo) == 0:
            maSo = input("Mã số bạn nhập bị sai, mới bạn nhập lại: ")
    #ten
    try:
        1 / (len(ten))
    except:
        while len(ten) == 0:
            ten = input("Tên bạn nhập bị sai, mới bạn nhập lại: ")
    #gia
    try:
        int(gia ** (1 / 2))
    except:
        while int(gia) < 0 or len(gia) == 0:
            gia = input("Giá bạn nhập bị sai, mới bạn nhập lại: ")
    #tenKhach
    try:
        1 / (len(tenKhach))
    except:
        while len(tenKhach) == 0:
            tenKhach = input("Tên khách hàng bạn nhập bị sai, mới bạn nhập lại: ")
    #ngayNhap
    try:
        1 / (len(ngayNhap))
    except:
        while len(ngayNhap) == 0:
            ngayNhap = input("Tên ngày nhập bị sai, mới bạn nhập lại: ")

    maSoAo.append(int(maSo))
    tenAo.append(ten)
    giaAo.append(int(gia))
    tenKhachHangMuaAo.append(tenKhach)
    ngayNhapAo.append(ngayNhap)

    print("Thêm thông tin thành công")

# ham xem
def xem():
    print("XEM THÔNG TIN")
    print("Mã số áo: " + str(maSoAo))
    print("Tên áo: " + str(tenAo))
    print("Giá áo: " + str(giaAo))
    print("Tên khách hàng: " + str(tenKhachHangMuaAo))
    print("Ngày nhập áo: " + str(ngayNhapAo))

# ham sua
def sua():
    print("SỬA THÔNG TIN")
    maSo = input("Nhập mã số cần sửa: ")
    if maSo in maSoAo:
        viTri = maSoAo.index(maSo)
        tenAo[viTri] = input("Nhập tên mới: ")
        giaAo[viTri] = input("Nhập giá mới: ")
        print("Sửa thông tin thành công")
    else:
        print("Không tìm thấy mã số để xửa")

# ham xoa
def xoa():
    print("XÓA THÔNG TIN")
    maSo = input("Nhập mã số cần xóa: ")
    if maSo in maSoAo:
        viTri = maSoAo.index(maSo)
        del maSoAo[viTri]
        del tenAo[viTri]
        del giaAo[viTri]
        del tenKhachHangMuaAo[viTri]
        del ngayNhapAo[viTri]
        print("Xóa thông tin thành công")
    else:
        print("Không tìm thấy mã số để xóa")

# ham sapxep
def sapxep():
    sapxepThuTu = []
    if sapxepThuTu == []:
        for i in range(len(giaAo)):
            sapxepThuTu.append([maSoAo[i], tenAo[i], giaAo[i], tenKhachHangMuaAo[i], ngayNhapAo[i]])
        sapxepThuTu.sort()
        for i in range(len(sapxepThuTu)):
            print(sapxepThuTu[i])
    else:
        print(sapxepThuTu)

def init():
    print("QUẢN LÝ SHOP QUẦN ÁO")
    print("1. Thêm thông tin")
    print("2. Xem thông tin")
    print("3. Sửa thông tin")
    print("4. Xóa thông tin")
    print("5. Sắp xếp thông tin")
    print("6. Thoát chương trình")

    chon = int(input("Chọn chức năng: "))
    while(chon >= 1 and chon <= 6):
        if(chon == 1):
            them()
        elif(chon == 2):
            xem()
        elif(chon == 3):
            sua()
        elif(chon == 4):
            xoa()
        elif(chon == 5):
            sapxep()
        else:
            break
        chon = int(input("Chọn chức năng: "))

    else:
        print("Nhập mã số không hợp lệ")

print(init())
