import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox, QPushButton

class MarketApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supermarket")
        self.resize(300, 220)

        self.products = {
            "Olma": 5000,
            "Banan": 7000,
            "Sut": 12000,
            "Go'sht": 90000
        }

        self.combo = QComboBox()
        self.combo.addItems(self.products.keys())

        self.spin_qty = QSpinBox()
        self.spin_qty.setRange(1, 100)

        self.btn_calc = QPushButton("Hisoblash")
        self.btn_calc.clicked.connect(self.calculate_total)

        self.label_res = QLabel("Savat summasi: 0 so'm")
        self.label_bonus = QLabel("")
        self.label_bonus.setStyleSheet("color: green; font-weight: bold;")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Mahsulotni tanlang:"))
        layout.addWidget(self.combo)
        layout.addWidget(QLabel("Miqdori:"))
        layout.addWidget(self.spin_qty)
        layout.addWidget(self.btn_calc)
        layout.addWidget(self.label_res)
        layout.addWidget(self.label_bonus)
        self.setLayout(layout)

    def calculate_total(self):
        prod = self.combo.currentText()
        price = self.products[prod]
        qty = self.spin_qty.value()
        
        total = price * qty
        self.label_res.setText(f"Savat summasi: {total:,} so'm")

        if total > 100000:
            discount = total * 0.9
            self.label_bonus.setText(f"🎉 Chegirma qo'llandi! Yakuniy narx: {discount:,} so'm")
        else:
            self.label_bonus.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MarketApp()
    win.show()
    sys.exit(app.exec_())
