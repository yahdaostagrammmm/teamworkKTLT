from PyQt6 import QtCore, QtGui, QtWidgets, uic


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cinema.ui", self)  # Load giao diện từ file .ui

        # Load dữ liệu phim từ file dataphim.txt
        self.movies = self.load_movie_data("dataphim.txt")

        # Lấy danh sách các ghế từ file UI
        self.selected_seats = set()
        self.seat_buttons = []
        for row in "ABCDEF":
            for col in "123456":
                btn = self.findChild(QtWidgets.QPushButton, f"{row}{col}")
                if btn:
                    btn.clicked.connect(lambda _, b=btn: self.toggle_seat(b))
                    self.seat_buttons.append(btn)

        # Lấy danh sách các nút thời gian từ file UI
        self.selected_time = None
        self.time_buttons = []
        for time_id in ["eight", "halfpastten", "twelve", "halfpastthree", "sixpm", "halfpastseven"]:
            btn = self.findChild(QtWidgets.QPushButton, time_id)
            if btn:
                btn.clicked.connect(lambda _, b=btn: self.select_time(b))
                self.time_buttons.append(btn)

        # Liên kết QLabel poster phim với sự kiện click
        for phim_ten in self.movies.keys():
            phim_id = self.get_movie_id(phim_ten)
            lbl = self.findChild(QtWidgets.QLabel, phim_id)
            if lbl:
                lbl.mousePressEvent = lambda event, t=phim_ten: self.show_movie_info(t, self.movies[t])

    def load_movie_data(self, filename):
        movies = {}
        try:
            with open(filename, "r", encoding="utf-8") as file:
                next(file)  # Bỏ qua dòng tiêu đề
                for line in file:
                    parts = line.strip().split(" | ")
                    if len(parts) == 4:
                        ten, the_loai, thoi_luong, mo_ta = parts
                        movies[ten] = (the_loai, thoi_luong, mo_ta)
        except FileNotFoundError:
            print("Không tìm thấy file dataphim.txt")
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

    def toggle_seat(self, button):
        if button in self.selected_seats:
            button.setStyleSheet("background-color: rgb(200, 181, 195);")
            self.selected_seats.remove(button)
        else:
            button.setStyleSheet("background-color: gray;")
            self.selected_seats.add(button)

    def select_time(self, button):
        if self.selected_time:
            self.selected_time.setStyleSheet("background-color: rgb(241, 160, 255);")
        self.selected_time = button
        button.setStyleSheet("background-color: purple;")

    def show_movie_info(self, ten_phim, info):
        the_loai, thoi_luong, mo_ta = info
        self.ten_phim_label.setText(ten_phim)  # Hiển thị tên phim
        self.the_loai_phim_label.setText(the_loai)
        self.thoi_luong_phim_label.setText(thoi_luong)
        self.mo_ta_phim_label.setWordWrap(True)  # Cho phép xuống dòng
        self.mo_ta_phim_label.setText(mo_ta)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
