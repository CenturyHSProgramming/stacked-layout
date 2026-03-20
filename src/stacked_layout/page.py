"""
page.py
by Chris Winikka
An attempt to create a specialized widget "page" to be imported.
"""

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QWidget,
)

class Page(QWidget):
    """A """
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.screen = QGridLayout()
        self.title_label = QLabel(title)


        self.screen.addWidget(self.title_label, 0, 0, 1, 3)
        
        self.splash_button = QPushButton("Home")
        self.splash_button.clicked.connect(self.goto_page)
        self.to_artist_button = QPushButton("Artist Search")
        self.to_artist_button.clicked.connect(self.goto_page)
        self.screen.addWidget(self.splash_button, 1, 0)
        self.screen.addWidget(self.to_artist_button, 1, 2)
    
    def goto_page(self):
        sending_button = self.sender()
        if sending_button.text() == "Art Types":
            self.stacked_layout.setCurrentIndex(1)
        elif sending_button.text() == "Artist Search":
            self.stacked_layout.setCurrentIndex(2)
        else:
            self.stacked_layout.setCurrentIndex(0)
