"""
stacked_layouts_example.py
by HundredVisionsGuy
A demo of the stacked layout with nav buttons. It's a proof of concept.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QWidget,
)
from page import Page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        # Create a stacked layout for multiple screens
        self.stacked_layout = QStackedLayout()

        # Splash page: 
        self.splash_page = QWidget()
        self.splash_screen = QGridLayout()
        splash_title_label = QLabel("Splash Page")
        self.splash_to_art_type_button = QPushButton("Art Types")
        self.splash_to_art_type_button.clicked.connect(self.goto_page)
        self.splash_to_artist_button = QPushButton("Artist Search")
        self.splash_to_artist_button.clicked.connect(self.goto_page)
        self.splash_screen.addWidget(splash_title_label, 0, 0, 1, 3)
        self.splash_screen.addWidget(self.splash_to_art_type_button, 1, 0, 1, 1)
        self.splash_screen.addWidget(self.splash_to_artist_button, 1, 2, 1, 1)
        self.splash_page.setLayout(self.splash_screen)

        # Art Types Screen
        self.art_types_page = Page("Art Types", self.stacked_layout)

        # Artist Search Screen
        self.artist_page = QWidget()
        self.artist_search_screen = QGridLayout()
        artist_title_label = QLabel("Artist Search")
        self.artist_to_splash_button = QPushButton("Home")
        self.artist_to_splash_button.clicked.connect(self.goto_page)
        self.artist_to_art_type_button = QPushButton("Art Types")
        self.artist_to_art_type_button.clicked.connect(self.goto_page)
        self.artist_search_screen.addWidget(artist_title_label, 0, 0, 1, 3)
        self.artist_search_screen.addWidget(self.artist_to_art_type_button, 1, 0)
        self.artist_search_screen.addWidget(self.artist_to_splash_button, 1, 2)
        self.artist_page.setLayout(self.artist_search_screen)

        # TODO: add a text input for user's name

        # TODO: add a push button to greet user

        # TODO: add a label to greet user

        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
        """

        # add widgets & layouts to main layout
        self.stacked_layout.addWidget(self.splash_page)
        self.stacked_layout.addWidget(self.art_types_page)
        self.stacked_layout.addWidget(self.artist_page)

        # [OPTIONAL] Add a stretch to move everything up
        # layout.addStretch()

        widget = QWidget()
        widget.setLayout(self.stacked_layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def goto_page(self):
        sending_button = self.sender()
        if sending_button.text() == "Art Types":
            self.stacked_layout.setCurrentIndex(1)
        elif sending_button.text() == "Artist Search":
            self.stacked_layout.setCurrentIndex(2)
        else:
            self.stacked_layout.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()