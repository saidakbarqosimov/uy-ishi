import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class RandomChoiceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tasodifiy tanlash")
        self.resize(300, 150)

        self.students = ["Asadbek", "Madina", "Jasur", "Zilola", "Bekzod", "Shahzoda"]

        self.btn_choose = QPushButton("🎲 Tasodifiy talabani tanlash")
        self.btn_choose.clicked.connect(self.pick_student)

        self.label_winner = QLabel("Kim chiqarkon? 🤔")
        self.label_winner.setAlignment(Qt.AlignCenter)
        self.label_winner.setStyleSheet("font-size: 16px; color: blue;")

        layout = QVBoxLayout()
        layout.addWidget(self.btn_choose)
        layout.addWidget(self.label_winner)
        self.setLayout(layout)

    def pick_student(self):
        winner = random.choice(self.students)
        self.label_winner.setText(f"🎉 Omadli talaba: <b>{winner}</b>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = RandomChoiceApp()
    win.show()
    sys.exit(app.exec_())
