import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

RANGLAR = ["red", "blue", "green", "yellow", "orange", "purple", "hotpink", "cyan"]

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Masala 4 - Rang Almashtiruvchi")
window.setFixedSize(300, 150)

layout = QVBoxLayout()

label = QLabel("Matn rangi o'zgaradi!")
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 22px; font-weight: bold;")

btn = QPushButton("Rangni almashtir")
btn.setStyleSheet("padding: 8px; font-size: 14px; background: #34495e; color: white; border-radius: 5px;")

def rang_almastir():
    rang = random.choice(RANGLAR)
    label.setStyleSheet(f"font-size: 22px; font-weight: bold; color: {rang};")
    label.setText(f"Rang: {rang}")

btn.clicked.connect(rang_almastir)

layout.addWidget(label)
layout.addWidget(btn)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
