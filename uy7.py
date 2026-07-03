import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QListWidget, QLabel

class LibraryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kutubxona qidiruv tizimi")
        self.resize(350, 250)

        self.books = [
            "Python Asoslari", 
            "Flask Dasturlash", 
            "Sun'iy Intellekt", 
            "Django Mukammal Kurs", 
            "Ma'lumotlar Strukturasi"
        ]

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Kitob nomini yozing...")
        self.search_box.textChanged.connect(self.filter_books)

        self.list_widget = QListWidget()
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Qidiruv:"))
        layout.addWidget(self.search_box)
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

        self.filter_books()

    def filter_books(self):
        self.list_widget.clear()
        query = self.search_box.text().lower().strip()

        for book in self.books:
            if query in book.lower():
                self.list_widget.addItem(book)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LibraryApp()
    win.show()
    sys.exit(app.exec_())
