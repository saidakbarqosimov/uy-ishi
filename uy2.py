import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class BudgetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Byudjet nazorati")
        self.resize(300, 150)

        self.budget = {
            "Yanvar": [1000000, 500000],
            "Fevral": [1200000, 600000],
            "Mart": [1500000, 600000]
        }

        self.combo = QComboBox()
        self.combo.addItems(self.budget.keys())
        self.combo.currentIndexChanged.connect(self.calculate_budget)

        self.label_title = QLabel("Oyni tanlang:")
        self.label_result = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.combo)
        layout.addWidget(self.label_result)
        self.setLayout(layout)

        self.calculate_budget()

    def calculate_budget(self):
        month = self.combo.currentText()
        expenses = self.budget.get(month, [])
        total = sum(expenses)
        self.label_result.setText(f"Umumiy xarajat: <b>{total:,} so'm</b>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = BudgetApp()
    win.show()
    sys.exit(app.exec_())
