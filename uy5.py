import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Masala 5 - Parol Tekshiruvchi")
window.setFixedSize(300, 170)

layout = QVBoxLayout()

edit = QLineEdit()
edit.setEchoMode(QLineEdit.Password)
edit.setPlaceholderText("Parolni kiriting...")
edit.setStyleSheet("padding: 8px; font-size: 14px; border: 1px solid #bdc3c7; border-radius: 4px;")

result_label = QLabel("")
result_label.setAlignment(Qt.AlignCenter)
result_label.setStyleSheet("font-size: 18px; font-weight: bold;")

btn = QPushButton("Tekshirish")
btn.setStyleSheet("padding: 8px; font-size: 14px; background: #2ecc71; color: white; border-radius: 5px;")

def tekshir():
    if edit.text() == "12345":
        result_label.setText("✅ Parol to'g'ri")
        result_label.setStyleSheet("font-size: 18px; font-weight: bold; color: green;")
    else:
        result_label.setText("❌ Noto'g'ri parol")
        result_label.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")

btn.clicked.connect(tekshir)

layout.addWidget(edit)
layout.addWidget(btn)
layout.addWidget(result_label)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
