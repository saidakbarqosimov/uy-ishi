import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class OfficeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ofis xodimlari")
        self.resize(350, 200)

        self.staff = {
            "Dilshod": "Direktor",
            "Aziza": "Hisobchi",
            "Anvar": "Dasturchi"
        }

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Ism kiriting...")
        self.input_name.textChanged.connect(self.search_staff)

        self.input_role = QLineEdit()
        self.input_role.setPlaceholderText("Yangi xodim lavozimi...")

        self.btn_add = QPushButton("Yangi xodim qo'shish")
        self.btn_add.clicked.connect(self.add_staff)

        self.label_info = QLabel("Xodim lavozimi: -")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Xodim ismi:"))
        layout.addWidget(self.input_name)
        layout.addWidget(self.label_info)
        layout.addWidget(QLabel("Yangi xodim uchun lavozim:"))
        layout.addWidget(self.input_role)
        layout.addWidget(self.btn_add)
        self.setLayout(layout)

    def search_staff(self):
        name = self.input_name.text().strip()
        if name in self.staff:
            self.label_info.setText(f"Xodim lavozimi: <b>{self.staff[name]}</b>")
        else:
            self.label_info.setText("Xodim lavozimi: <i>Bunday xodim topilmadi</i>")

    def add_staff(self):
        name = self.input_name.text().strip()
        role = self.input_role.text().strip()

        if name and role:
            self.staff[name] = role
            QMessageBox.information(self, "Muvaffaqiyatli", f"{name} ({role}) bazaga qo'shildi!")
            self.input_role.clear()
            self.search_staff()
        else:
            QMessageBox.warning(self, "Xatolik", "Ism va lavozim maydonlarini to'ldiring!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = OfficeApp()
    win.show()
    sys.exit(app.exec_())
