import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Masala 1 - Random Son")
window.setFixedSize(300, 150)

layout = QVBoxLayout()

label = QLabel("Son chiqadi...")
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 28px; font-weight: bold; color: #2c3e50;")

btn = QPushButton("Random son chiqar")
btn.setStyleSheet("padding: 8px; font-size: 14px; background: #3498db; color: white; border-radius: 5px;")
btn.clicked.connect(lambda: label.setText(str(random.randint(1, 100))))

layout.addWidget(label)
layout.addWidget(btn)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
