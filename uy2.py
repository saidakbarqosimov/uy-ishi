import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Masala 2 - Ism/Familiya/Sana")
window.setFixedSize(350, 160)

layout = QVBoxLayout()

label = QLabel("Tugmani bosing...")
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 22px; font-weight: bold; color: #2c3e50; padding: 10px;")

btn_layout = QHBoxLayout()

btn1 = QPushButton("Ism")
btn2 = QPushButton("Familiya")
btn3 = QPushButton("Tug'ilgan sana")

for btn in [btn1, btn2, btn3]:
    btn.setStyleSheet("padding: 8px; font-size: 13px; background: #9b59b6; color: white; border-radius: 5px;")
    btn_layout.addWidget(btn)

btn1.clicked.connect(lambda: label.setText("SAIDAKBER"))
btn2.clicked.connect(lambda: label.setText("QOSIMOV"))
btn3.clicked.connect(lambda: label.setText("17.10.2010"))

layout.addWidget(label)
layout.addLayout(btn_layout)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
