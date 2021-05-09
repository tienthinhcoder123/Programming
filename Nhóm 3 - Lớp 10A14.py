maSoAo = [1, 2, 3]
tenAo = ["vay", "dam", "ao thun"]
giaAo = [15000, 42314, 352532142423]
tenKhachHangMuaAo = ["Thinh", "Trump", "Biden"]
ngayNhapAo = ["24/3/1234", "31/3/243", '12/12/2021']
sapxepThuTu = []

def maSo():
    maSo_a = input("Nhập mã số áo: ")
    try:
        int(int(maSo_a) * len(maSo_a) ** (1/2))
        return int(maSo_a)
    except:
        maSo()

def ten():
    tenao = input("Nhập tên áo: ")
    try:
        1 / len(tenao)
        return tenao
    except:
        ten()

def gia():
    gia_a = input("Nhập giá bán áo: ")
    try:
        int(int(gia_a) * len(gia_a) ** (1/2))
        return int(gia_a)
    except:
        gia()

def tenKhach():
    tenkhach = input("Nhập tên khách hàng mua áo: ")
    try:
        1 / len(tenkhach)
        return tenkhach
    except:
        tenkhach()

def ngayNhap():
    ngaynhap = input("Nhập ngày nhập áo: ")
    try:
        1 / len(ngaynhap)
        return ngaynhap
    except:
        ngaynhap()

# ham them
def them():
    print("THÊM THÔNG TIN")
    maso = maSo()
    tenao = ten()
    gia_a = gia()
    tenkhach = tenKhach()
    ngaynhap = ngayNhap()

    maSoAo.append(maso)
    tenAo.append(tenao)
    giaAo.append(gia_a)
    tenKhachHangMuaAo.append(tenkhach)
    ngayNhapAo.append(ngaynhap)

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
    for i in range(len(giaAo)):
        sapxepThuTu.append([giaAo[i], tenAo[i], maSoAo[i], tenKhachHangMuaAo[i], ngayNhapAo[i]])
    sapxepThuTu.sort()
    print('Sắp xếp thự tự:')
    print('------------------')
    print('Mã số\tTên áo\tGiá áo\t\tKhách\tNgày\n----------------------------------------------')
    for i in range(len(sapxepThuTu)):
        print(str(sapxepThuTu[i][2])[:10]+ '\t' + str(sapxepThuTu[i][1])[:10]+ '\t' + str(str(sapxepThuTu[i][2])+' '*(10-len(str(sapxepThuTu[i][2]))))[:10]+ '\t' +str(sapxepThuTu[i][3])[:10]+ '\t' +str(sapxepThuTu[i][4])[:10]+ '\t')
        

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
