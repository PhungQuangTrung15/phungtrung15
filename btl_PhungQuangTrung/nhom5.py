import json

danh_sach_cong_viec = {}

def doc_danh_sach_cong_viec():
    try:
        with open('D:\\btl_PhungQuangTrung\\du_lieu.json', 'r', encoding = "utf-8") as f:
            global danh_sach_cong_viec
            danh_sach_cong_viec = json.load(f)
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra đường dẫn")

def luu_danh_sach_cong_viec():
    try:
        with open('D:\\btl_PhungQuangTrung\\du_lieu.json', 'w', encoding = "utf-8") as f:
            json.dump(danh_sach_cong_viec, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Lỗi khi lưu danh sách công việc: {e}")

def them_cong_viec():
    so_cong_viec =int(input("Nhập số lượng công việc muốn thêm: "))
    for i in range(so_cong_viec):
        print(f"Nhập thông tin công việc thứ {i + 1}:")
        ten_cong_viec = input("Nhập tên công việc: ")
        ma_cong_viec = input("Nhập mã công việc: ")
        mo_ta = input("Nhập mô tả công việc: ")
        ngay_tao = input("Nhập ngày tạo công việc (dd/mm/yyyy): ")
        han_hoan_thanh = input("Nhập hạn hoàn thành công việc (dd/mm/yyyy): ")
        while True:
            print("Công việc có các trạng thái sau: ")
            print("1. Chưa bắt đầu")
            print("2. Đang thực hiện")
            print("3. Hoàn thành")
            trang_thai = input("Nhập trạng thái công việc (1/2/3): ")
            if trang_thai == '1':
                trang_thai = 'Chưa bắt đầu'
                break
            elif trang_thai == '2':
                trang_thai = 'Đang thực hiện'
                break
            elif trang_thai == '3':
                trang_thai = 'Hoàn thành'
                break
            else:
                print("Chọn sai lựa chọn, vui lòng nhập lại")          
                print("=" * 20)
        nguoi_phu_trach = input("Nhập tên người phụ trách công việc: ")
        danh_sach_cong_viec[ten_cong_viec] = {
            'Mã công việc': ma_cong_viec,
            'Mô tả': mo_ta,
            'Ngày tạo': ngay_tao,
            'Hạn hoàn thành': han_hoan_thanh,
            'Trạng thái': trang_thai,
            'Người phụ trách': nguoi_phu_trach
        }
    luu_danh_sach_cong_viec()

def xem_danh_sach_cong_viec():
    doc_danh_sach_cong_viec()
    if danh_sach_cong_viec == {}:
        print("Danh sách công việc trống.")
    else:
        print("Danh sách công việc:")
        for cong_viec, thong_tin in danh_sach_cong_viec.items():
            print(f"{cong_viec}: ")
            for key, value in thong_tin.items():
                print(f"{key}: {value}")
            print("=" * 40)

def xem_cong_viec_theo_trang_thai():
    doc_danh_sach_cong_viec()
    trang_thai = input("Nhập trạng thái công việc (Chưa bắt đầu/Đang thực hiện/Hoàn thành): ")
    print(f"Các công việc có trạng thái '{trang_thai}':")
    for cong_viec, thong_tin in danh_sach_cong_viec.items():
        if thong_tin['Trạng thái'] == trang_thai:
            print(f"{cong_viec}: ")
            for key, value in thong_tin.items():
                print(f"{key}: {value}")
            print("=" * 40)

def xem_cong_viec_theo_han_hoan_thanh():
    doc_danh_sach_cong_viec()
    han_hoan_thanh = input("Nhập vào hạn hoàn thành công việc (dd/mm/yyyy): ")
    print(f"Các công việc có hạn hoàn thành quá ngày {han_hoan_thanh}: ")
    for cong_viec, thong_tin in danh_sach_cong_viec.items():
        if thong_tin['Hạn hoàn thành'][0:2] >= han_hoan_thanh[0:2] and thong_tin['Hạn hoàn thành'][3:5] >= han_hoan_thanh[3:5] and thong_tin['Hạn hoàn thành'][6:10] >= han_hoan_thanh[6:10]:
            print(f"{cong_viec}: ")
            for key, value in thong_tin.items():
                print(f"{key}: {value}")
            print("=" * 40)

def tim_kiem_cong_viec_theo_ten():
    doc_danh_sach_cong_viec()
    ten_cong_viec = input("Nhập tên công việc cần tìm: ")
    if ten_cong_viec in danh_sach_cong_viec:
        for cong_viec, thong_tin in danh_sach_cong_viec.items():
            if ten_cong_viec == cong_viec:
                print(f"{cong_viec}: ")
                for key, value in thong_tin.items():
                    print(f"{key}: {value}")
                print("=" * 40)

def tim_cong_viec_theo_ma():
    doc_danh_sach_cong_viec()
    ma_cong_viec = input("Nhập mã công việc cần tìm: ")
    for cong_viec, thong_tin in danh_sach_cong_viec.items():
        if thong_tin['Mã công việc'] == ma_cong_viec:
            print(f"{cong_viec}")
            for key, value in thong_tin.items():
                print(f"{key}: {value}")
            print("=" * 40)

def tim_kiem_cong_viec_theo_ten_nguoi_phu_trach():
    doc_danh_sach_cong_viec()
    ten_nguoi_phu_trach = input("Nhập tên người phụ trách công việc cần tìm: ")
    print(f"Các công việc do {ten_nguoi_phu_trach} phụ trách:")
    for cong_viec, thong_tin in danh_sach_cong_viec.items():
        if thong_tin['Người phụ trách'] == ten_nguoi_phu_trach:
            print(f"{cong_viec}: ")
            for key, value in thong_tin.items():
                print(f"{key}: {value}")
            print("=" * 40)

def cap_nhat_ten_cong_viec():
    doc_danh_sach_cong_viec()
    ten_cong_viec = input("Nhập tên công việc cần cập nhật: ")
    if ten_cong_viec not in danh_sach_cong_viec:
        print("Công việc không tồn tại.")
        return
    else:
        ten_moi = input("Nhập tên mới cho công việc: ")
        danh_sach_cong_viec[ten_moi] = danh_sach_cong_viec.pop(ten_cong_viec)
        luu_danh_sach_cong_viec()

def cap_nhat_trang_thai_cong_viec():
    doc_danh_sach_cong_viec()
    ten_cong_viec = input("Nhập tên công việc cần cập nhật trạng thái: ")
    if ten_cong_viec not in danh_sach_cong_viec:
        print("Công việc không tồn tại.")
        return
    else:
        while True:
            print("Công việc có các trạng thái sau: ")
            print("1. Chưa bắt đầu")
            print("2. Đang thực hiện")
            print("3. Hoàn thành")
            trang_thai = input("Nhập trạng thái công việc (1/2/3): ")
            if trang_thai == '1':
                trang_thai = 'Chưa bắt đầu'
                break
            elif trang_thai == '2':
                trang_thai = 'Đang thực hiện'
                break
            elif trang_thai == '3':
                trang_thai = 'Hoàn thành'
                break
            else:
                print("Chọn sai lựa chọn, vui lòng nhập lại")          
                print("=" * 20)
        danh_sach_cong_viec[ten_cong_viec]['Trạng thái'] = trang_thai
        luu_danh_sach_cong_viec()

def cap_nhat_han_hoan_thanh_cong_viec():
    doc_danh_sach_cong_viec()
    ten_cong_viec = input("Nhập tên công việc cần cập nhật hạn hoàn thành: ")
    if ten_cong_viec not in danh_sach_cong_viec:
        print("Công việc không tồn tại.")
        return
    else:
        han_hoan_thanh = input("Nhập hạn hoàn thành mới (dd/mm/yyyy): ")
        danh_sach_cong_viec[ten_cong_viec]['Hạn hoàn thành'] = han_hoan_thanh
        luu_danh_sach_cong_viec()

def xoa_cong_viec_theo_ten():
    doc_danh_sach_cong_viec()
    ten_cong_viec = input("Nhập tên công việc cần xóa: ")
    if ten_cong_viec in danh_sach_cong_viec:
        del danh_sach_cong_viec[ten_cong_viec]
        luu_danh_sach_cong_viec()
        print(f"Công việc '{ten_cong_viec}' đã được xóa.")
    else:
        print("Công việc không tồn tại.")

def xoa_cong_viec_da_hoan_thanh():
    doc_danh_sach_cong_viec()
    ten_cong_viec = input("Nhập tên công việc đã hoàn thành cần xóa: ")
    if ten_cong_viec in danh_sach_cong_viec:
        if danh_sach_cong_viec[ten_cong_viec]['Trạng thái'] == 'Hoàn thành':
            del danh_sach_cong_viec[ten_cong_viec]
            luu_danh_sach_cong_viec()
            print(f"Công việc '{ten_cong_viec}' đã được xóa.")
        else:
            print("Công việc chưa hoàn thành, không thể xóa.")
    else:
        print("Công việc không tồn tại.")

def sap_xep_cong_viec_theo_han_hoan_thanh():
    doc_danh_sach_cong_viec()
    danh_sach_cong_viec_sorted = dict(sorted(danh_sach_cong_viec.items(), key=lambda item: item[1]['Hạn hoàn thành']))
    print("Danh sách công việc đã sắp xếp theo hạn hoàn thành:")
    for cong_viec, thong_tin in danh_sach_cong_viec_sorted.items():
        print(f"{cong_viec}: ")
        for key, value in thong_tin.items():
            print(f"{key}: {value}")
        print("=" * 40)

def sap_xep_cong_viec_theo_ngay_tao():
    doc_danh_sach_cong_viec()
    danh_sach_cong_viec_sorted = dict(sorted(danh_sach_cong_viec.items(), key=lambda item: item[1]['Ngày tạo']))
    print("Danh sách công việc đã sắp xếp theo ngày tạo:")
    for cong_viec, thong_tin in danh_sach_cong_viec_sorted.items():
        print(f"{cong_viec}: ")
        for key, value in thong_tin.items():
            print(f"{key}: {value}")
        print("=" * 40)

def xoa_toan_bo_cong_viec():
    doc_danh_sach_cong_viec()
    global danh_sach_cong_viec
    danh_sach_cong_viec = {}
    luu_danh_sach_cong_viec()
    print("Đã xóa toàn bộ công việc.")


if __name__ == '__main__':
    doc_danh_sach_cong_viec()
    while True:
        print("==========Chương trình quản lí công việc==========")
        print("1. Thêm công việc")
        print("2. Xem danh sách công việc")
        print("3. Xem công việc theo trạng thái (chưa bắt đầu / đang làm / hoàn thành)")
        print("4. Xem công việc theo hạn hoàn thành")
        print("5. Tìm kiếm công việc theo tên")
        print("6. Tìm kiếm công việc theo mã")
        print("7. Tìm kiếm công việc theo tên người phụ trách")
        print("8. Cập nhật tên công việc")
        print("9. Cập nhật trạng thái công việc")
        print("10. Cập nhật hạn hoàn thành công việc")
        print("11. Xóa công việc theo tên")
        print("12. Xóa công việc đã hoàn thành")
        print("13. Sắp xếp công việc theo hạn hoàn thành")
        print("14. Sắp xếp công việc theo ngày tạo")
        print("15. Xóa toàn bộ công việc")
        print("0. Thoát chương trình")
        lua_chon = input("Nhập lựa chọn của bạn ")
        if lua_chon == '1':
            them_cong_viec()
            print("=" * 20)
        elif lua_chon == '2':
            xem_danh_sach_cong_viec()
        elif lua_chon == '3':
            xem_cong_viec_theo_trang_thai()
        elif lua_chon == '4':
            xem_cong_viec_theo_han_hoan_thanh()
        elif lua_chon == '5':
            tim_kiem_cong_viec_theo_ten()
        elif lua_chon == '6':
            tim_cong_viec_theo_ma()
        elif lua_chon == '7':
            tim_kiem_cong_viec_theo_ten_nguoi_phu_trach()
        elif lua_chon == '8':
            cap_nhat_ten_cong_viec()
        elif lua_chon == '9':
            cap_nhat_trang_thai_cong_viec()
        elif lua_chon == '10':
            cap_nhat_han_hoan_thanh_cong_viec()
        elif lua_chon == '11':
            xoa_cong_viec_theo_ten()
        elif lua_chon == '12':
            xoa_cong_viec_da_hoan_thanh()
        elif lua_chon == '13':
            sap_xep_cong_viec_theo_han_hoan_thanh()
        elif lua_chon == '14':
            sap_xep_cong_viec_theo_ngay_tao()
        elif lua_chon == '15':
            xoa_toan_bo_cong_viec()
        elif lua_chon == '0':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break