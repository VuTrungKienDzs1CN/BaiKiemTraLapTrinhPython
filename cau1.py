def them_sach(danh_sach, ma, ten, gia, soluong):
    """Thêm một cuốn sách vào danh sách."""
    danh_sach.append({
        "ma": ma,
        "ten": ten,
        "gia": gia,
        "soluong": soluong,
    })


def tim_kiem_theo_ten(danh_sach, tu_khoa):
    """Trả về các sách có tên chứa từ khóa (không phân biệt hoa/thường)."""
    tu_khoa = tu_khoa.strip().lower()
    return [s for s in danh_sach if tu_khoa in s["ten"].lower()]


def tong_gia_tri_kho_sach(danh_sach):
    """Tổng giá trị kho = tổng (Gia x SoLuong)."""
    return sum(s["gia"] * s["soluong"] for s in danh_sach)


def in_danh_sach(ds):
    """In danh sách sách dạng bảng."""
    if not ds:
        print("Không có sách nào.")
        return
    print(f"{'MaSach':<8}{'TenSach':<35}{'Gia':>10}{'SoLuong':>9}")
    print("-" * 62)
    for s in ds:
        print(f"{s['ma']:<8}{s['ten']:<35}{s['gia']:>10,}{s['soluong']:>9}")


def nhap_so(thong_bao, kieu=int):
    """Nhập số hợp lệ (không âm), nhập sai thì yêu cầu nhập lại."""
    while True:
        try:
            gia_tri = kieu(input(thong_bao))
            if gia_tri < 0:
                print("Giá trị không được âm. Vui lòng nhập lại!")
                continue
            return gia_tri
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập lại!")


def hien_thi_menu():
    print("\n===== QUẢN LÝ SÁCH THƯ VIỆN =====")
    print("1. Thêm sách")
    print("2. Tìm kiếm theo tên")
    print("3. Xem tổng giá trị kho sách")
    print("4. Thoát chương trình")


def main():
    # Dữ liệu mẫu để kiểm thử
    danh_sach = []
    them_sach(danh_sach, "S001", "Lập trình Python cơ bản", 95000, 40)
    them_sach(danh_sach, "S002", "Cấu trúc dữ liệu và giải thuật", 120000, 6)
    them_sach(danh_sach, "S003", "Nhập môn trí tuệ nhân tạo", 150000, 25)

    while True:
        hien_thi_menu()
        chon = input("Chọn chức năng (1-4): ").strip()

        if chon == "1":
            ma = input("Nhập mã sách: ").strip()
            if any(s["ma"].lower() == ma.lower() for s in danh_sach):
                print("Mã sách đã tồn tại!")
                continue
            ten = input("Nhập tên sách: ").strip()
            gia = nhap_so("Nhập giá: ")
            soluong = nhap_so("Nhập số lượng: ")
            them_sach(danh_sach, ma, ten, gia, soluong)
            print("Đã thêm sách thành công!")

        elif chon == "2":
            tu_khoa = input("Nhập từ khóa tìm kiếm: ")
            ket_qua = tim_kiem_theo_ten(danh_sach, tu_khoa)
            in_danh_sach(ket_qua)

        elif chon == "3":
            tong = tong_gia_tri_kho_sach(danh_sach)
            print(f"Tổng giá trị kho sách: {tong:,} VNĐ")

        elif chon == "4":
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4!")


if __name__ == "__main__":
    main()