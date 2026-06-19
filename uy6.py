import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Masala 6 - Hisoblagich")
window.setFixedSize(280, 150)

layout = QVBoxLayout()

count = [0]

label = QLabel("0")
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 48px; font-weight: bold; color: #2c3e50;")

btn_layout = QHBoxLayout()

btn_plus = QPushButton("+1")
btn_minus = QPushButton("-1")

for btn in [btn_plus, btn_minus]:
    btn.setStyleSheet("padding: 10px; font-size: 18px; font-weight: bold; border-radius: 5px; color: white;")
    btn_layout.addWidget(btn)

btn_plus.setStyleSheet("padding: 10px; font-size: 18px; font-weight: bold; border-radius: 5px; color: white; background: #27ae60;")
btn_minus.setStyleSheet("padding: 10px; font-size: 18px; font-weight: bold; border-radius: 5px; color: white; background: #e74c3c;")

def oshir():
    count[0] += 1
    label.setText(str(count[0]))

def kamayt():
    count[0] -= 1
    label.setText(str(count[0]))

btn_plus.clicked.connect(oshir)
btn_minus.clicked.connect(kamayt)

layout.addWidget(label)
layout.addLayout(btn_layout)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
