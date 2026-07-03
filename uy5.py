import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class ScheduleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dars jadvali")
        self.resize(300, 180)

        self.schedule = {
            "Dushanba": ["Matematika", "Fizika", "Ona tili"],
            "Seshanba": ["Ingliz tili", "Tarix", "Kimyo"],
            "Chorshanba": ["Informatika", "Adabiyot"]
        }

        self.combo = QComboBox()
        self.combo.addItems(self.schedule.keys())
        self.combo.currentIndexChanged.connect(self.show_schedule)

        self.label_res = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Kunni tanlang:"))
        layout.addWidget(self.combo)
        layout.addWidget(QLabel("<b>Darslar ro'yxati:</b>"))
        layout.addWidget(self.label_res)
        self.setLayout(layout)

        self.show_schedule()

    def show_schedule(self):
        day = self.combo.currentText()
        lessons = self.schedule.get(day, [])
        text = "\n".join([f"🔹 {lesson}" for lesson in lessons])
        self.label_res.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ScheduleApp()
    win.show()
    sys.exit(app.exec_())
