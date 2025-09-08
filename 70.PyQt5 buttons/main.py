# PyQt5 buttons
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
    
    def initUI(self):
        self.button = QPushButton("Click me!", self)    # we normallt use self for each button obeject because
        self.button.setGeometry(150, 200, 200, 100)     # it can use in main window without using in initUI
        self.button.setStyleSheet("font-size: 30px")
        # we want add signal and slot for the button
        self.button.clicked.connect(self.on_click)      # widget.signal.connect(slot_function)

        self.label = QLabel("Hello", self)
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px")


    # connecting button to a function
    def on_click(self):
        print("Button Clicked!")
        self.button.setText("Clicked!")
        # we can also disable the button when we click on that
        self.button.setDisabled(True)
        # change the label text (after click the button)
        self.label.setText("Goodbye")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

