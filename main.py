import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QLabel
from PyQt6.QtCore import Qt
from cinema import Ui_MainWindow
from hoadon import Ui_MainWindow as HoaDonWindow
from nutthanhtoan import setup_hoadon_button_links

class PaymentProcessor:
    def __init__(self, main_ui):
        self.main_ui = main_ui

    def calculate_total(self):
        ve_gia = len(self.main_ui.selected_seats) * 100000
        bap_mini = self.main_ui.spinBox.value() * 70000
        bap_lon = self.main_ui.spinBox_2.value() * 90000
        pepsi = self.main_ui.spinBox_3.value() * 40000
        return ve_gia, bap_mini, bap_lon, pepsi, ve_gia + bap_mini + bap_lon + pepsi

    def get_seat_names(self):
        return ", ".join(self.main_ui.selected_seats)

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.processor = PaymentProcessor(self)
        self.selected_seats = []
        self.selected_time = None
        self.movies = self.load_movie_data("dataphim.txt")

        self.thanh_toan_button.clicked.connect(self.show_payment_window)
        self.connect_seat_buttons()
        self.connect_time_buttons()
        self.connect_movie_labels()

    def connect_seat_buttons(self):
        for row in "ABCDEF":
            for col in "123456":
                btn = self.findChild(QPushButton, f"{row}{col}")
                if btn:
                    btn.clicked.connect(lambda checked, b=btn: self.select_seat(b))

    def select_seat(self, button):
        seat = button.text()
        if seat in self.selected_seats:
            self.selected_seats.remove(seat)
            button.setStyleSheet("background-color: rgb(255, 170, 255);")
        else:
            self.selected_seats.append(seat)
            button.setStyleSheet("background-color: #ff41fc;")

    def connect_time_buttons(self):
        times = [self.eight, self.halfpastten, self.twelve, self.halfpastthree, self.sixpm, self.halfpastseven]
        for btn in times:
            btn.clicked.connect(lambda checked, b=btn: self.select_time(b))

    def select_time(self, button):
        if self.selected_time:
            self.selected_time.setStyleSheet("background-color: rgb(241, 160, 255);")
        self.selected_time = button
        button.setStyleSheet("background-color: purple;")

    def connect_movie_labels(self):
        for movie in self.movies.keys():
            label = self.findChild(QLabel, self.get_movie_id(movie))
            if label:
                label.mousePressEvent = lambda event, t=movie: self.show_movie_info(t)

    def show_movie_info(self, movie):
        info = self.movies[movie]
        self.ten_phim_label.setText(movie)
        self.the_loai_phim_label.setText(info[0])
        self.thoi_luong_phim_label.setText(info[1])
        self.mo_ta_phim_label.setText(info[2])
        self.mo_ta_phim_label.setWordWrap(True)

    def load_movie_data(self, filename):
        movies = {}
        try:
            with open(filename, "r", encoding="utf-8") as file:
                next(file)  # Bỏ qua tiêu đề
                for line in file:
                    parts = line.strip().split(" | ")
                    if len(parts) == 4:
                        ten, the_loai, thoi_luong, mo_ta = parts
                        movies[ten] = (the_loai, thoi_luong, mo_ta)
        except FileNotFoundError:
            print("Không tìm thấy file dữ liệu phim")
        return movies

    def get_movie_id(self, movie_name):
        return {
            "Avatar": "phim1",
            "Barbie": "phim2",
            "A Man Called Otto": "phim3",
            "Past lives": "phim4",
            "The Creator": "phim5",
            "Guardians of the Galaxy": "phim6",
            "Ant-Man and The Wasp": "phim7",
        }.get(movie_name, "")

    def show_payment_window(self):
        if not self.selected_seats:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn ghế!")
            return
        if not self.selected_time:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn suất chiếu!")
            return

        self.hide()

        self.payment_window = QMainWindow()
        self.payment_ui = HoaDonWindow()
        self.payment_ui.setupUi(self.payment_window)

        self.payment_ui.label_Film.setText(self.ten_phim_label.text())
        self.payment_ui.label_Suatchiu.setText(self.selected_time.text())
        self.payment_ui.label_chair.setText(self.processor.get_seat_names())

        ve_gia, bap_mini, bap_lon, pepsi, tong_tien = self.processor.calculate_total()

        self.payment_ui.label_veticket.setText(str(len(self.selected_seats)))
        self.payment_ui.label_tongticket.setText(f"{ve_gia} VNĐ")
        self.payment_ui.label_cornmini.setText(str(self.spinBox.value()))
        self.payment_ui.label_tongcornmini.setText(f"{bap_mini} VNĐ")
        self.payment_ui.label_cornbig.setText(str(self.spinBox_2.value()))
        self.payment_ui.label_tongcornbig.setText(f"{bap_lon} VNĐ")
        self.payment_ui.label_pepsi.setText(str(self.spinBox_3.value()))
        self.payment_ui.label_tongpepsi.setText(f"{pepsi} VNĐ")
        self.payment_ui.label_tongall.setText(f"{tong_tien} VNĐ")

        # Liên kết sự kiện cho các nút trên giao diện hóa đơn từ file nutthanhtoan.py
        setup_hoadon_button_links(self.payment_ui, self)
        # Liên kết nút thanh toán tiền mặt với phương thức show_cash_payment
        self.payment_ui.pushButton_tienmat.clicked.connect(self.show_cash_payment)

        self.payment_window.show()

    def show_qr_payment(self):
        self.payment_window.hide()
        from maqr import Ui_MainWindow as Ui_QRWindow  # Nếu chưa import từ đầu
        self.qr_window = QMainWindow()
        self.qr_ui = Ui_QRWindow()
        self.qr_ui.setupUi(self.qr_window)

        self.qr_ui.ButtonXacnhanTT.clicked.connect(self.qr_payment_success)
        self.qr_ui.ButtonQuaylaiTT.clicked.connect(lambda: (self.qr_window.close(), self.payment_window.show()))

        self.qr_window.show()

    def qr_payment_success(self):
        QMessageBox.information(self, "Thanh toán", "Thanh toán thành công!")
        self.qr_window.close()
        self.payment_window.close()
        self.show()

    def show_cash_payment(self):
        # Hiển thị cửa sổ thông báo thanh toán bằng tiền mặt
        QMessageBox.information(self, "Thanh toán", "Đặt vé thành công. Vui lòng thanh toán & nhận vé tại quầy!")
        self.payment_window.close()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
