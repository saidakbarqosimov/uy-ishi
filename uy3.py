import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Masala 3 - Kalkulyator")
window.setFixedSize(360, 200)

layout = QVBoxLayout()

input_layout = QHBoxLayout()
edit1 = QLineEdit()
edit2 = QLineEdit()
edit1.setPlaceholderText("1-son")
edit2.setPlaceholderText("2-son")
for e in [edit1, edit2]:
    e.setStyleSheet("padding: 6px; font-size: 14px; border: 1px solid #bdc3c7; border-radius: 4px;")
    input_layout.addWidget(e)

result_label = QLabel("Natija: ")
result_label.setAlignment(Qt.AlignCenter)
result_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #27ae60;")

def hisobla(amal):
    try:
        a = float(edit1.text())
        b = float(edit2.text())
        if amal == '+':
            res = a + b
        elif amal == '-':
            res = a - b
        elif amal == '*':
            res = a * b
        elif amal == '/':
            if b == 0:
                result_label.setText("Xato: 0 ga bo'lib bo'lmaydi!")
                return
            res = a / b
        result_label.setText(f"Natija: {res:.4g}")
    except ValueError:
        result_label.setText("Xato: son kiriting!")

btn_layout = QHBoxLayout()
for text, amal in [("Qo'shish", '+'), ("Ayirish", '-'), ("Ko'paytirish", '*'), ("Bo'lish", '/')]:
    btn = QPushButton(text)
    btn.setStyleSheet("padding: 7px; font-size: 12px; background: #e74c3c; color: white; border-radius: 4px;")
    btn.clicked.connect(lambda checked, a=amal: hisobla(a))
    btn_layout.addWidget(btn)

layout.addLayout(input_layout)
layout.addWidget(result_label)
layout.addLayout(btn_layout)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
