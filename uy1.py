import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class PhoneBookApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Telefon kitobi")
        self.resize(300, 150)

        self.contacts = {
            "Ali": "+998901234567",
            "Vali": "+998919876543",
            "Olim": "+998935554433"
        }

        self.combo = QComboBox()
        self.combo.addItems(self.contacts.keys())
        self.combo.currentIndexChanged.connect(self.show_number)

        self.label_title = QLabel("Xodimni tanlang:")
        self.label_result = QLabel("")
        
        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.combo)
        layout.addWidget(self.label_result)
        self.setLayout(layout)

        self.show_number()

    def show_number(self):
        name = self.combo.currentText()
        phone = self.contacts.get(name, "Topilmadi")
        self.label_result.setText(f"Telefon: <b>{phone}</b>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PhoneBookApp()
    win.show()
    sys.exit(app.exec_())
