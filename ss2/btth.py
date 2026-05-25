ten = input("Nhập tên bệnh nhân: ")
nam_sinh = int(input("Nhập năm sinh: "))
so_ngay_bi_benh = int(input("Nhập số ngày bị bệnh: "))
nhiet_do = float(input("Nhập nhiệt độ cơ thể (°C): "))
chi_phi_kham = float(input("Nhập chi phí khám: "))

hop_le = True

if ten.strip() == "":
    print("Tên không được để trống")
    hop_le = False

if not (1900 <= nam_sinh <= 2025):
    print("Năm sinh không hợp lệ")
    hop_le = False

if so_ngay_bi_benh < 0:
    print("Số ngày bị bệnh phải >= 0")
    hop_le = False

if not (30 <= nhiet_do <= 45):
    print("Nhiệt độ không hợp lệ")
    hop_le = False

if chi_phi_kham <= 0:
    print("Chi phí khám phải > 0")
    hop_le = False

if hop_le == False:
    print("Dữ liệu không hợp lệ. Kết thúc chương trình!")
    exit()

tuoi = 2025 - nam_sinh
phu_phi = chi_phi_kham * 0.10
tong_chi_phi = chi_phi_kham + phu_phi

if nhiet_do > 38 and so_ngay_bi_benh > 3:
    tinh_trang = "Nguy hiểm"
elif nhiet_do > 38:
    tinh_trang = "Sốt cao"
elif nhiet_do > 37.5:
    tinh_trang = "Sốt nhẹ"
else:
    tinh_trang = "Bình thường"

if tinh_trang == "Nguy hiểm":
    if tuoi > 60:
        muc_do_uu_tien = "Cấp cứu"
    else:
        muc_do_uu_tien = "Ưu tiên cao"
else:
    muc_do_uu_tien = "Bình thường"

muc_chi_phi = "Cao" if tong_chi_phi > 500000 else "Thấp"

print("\n------ KẾT QUẢ ------")
print("Tên bệnh nhân:", ten)
print("Tuổi:", tuoi)
print("Nhiệt độ:", nhiet_do, "°C")
print("Số ngày bị bệnh:", so_ngay_bi_benh)
print("Tình trạng:", tinh_trang)
print("Mức độ ưu tiên:", muc_do_uu_tien)
print("Tổng chi phí:", tong_chi_phi, "VND")
print("Mức chi phí:", muc_chi_phi)