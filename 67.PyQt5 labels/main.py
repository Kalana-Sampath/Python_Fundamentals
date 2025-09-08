# PyQt5 labels

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel   
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt          
                    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("67.PyQt5 labels/profile_pic.jpg"))

# for the text of the label we will pass the string "Hello", for the second argument we will pss self, Self 
# refers to this window object

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 25))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: blue")
        label.setStyleSheet("color: #D62B06;" 
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")          # you can also use rgb or hexadecimal code
        label.setAlignment(Qt.AlignTop)         # VERTICALLY TOP
        label.setAlignment(Qt.AlignBottom)      # VERTICALLY BOTTOM
        label.setAlignment(Qt.AlignVCenter)     # VERTICALLY CENTER

        label.setAlignment(Qt.AlignRight)       # HORIZONTALLY RIGHT
        label.setAlignment(Qt.AlignHCenter)     # HORIZONTALLY CENTER
        label.setAlignment(Qt.AlignLeft)        # HORIZONTALLY LEFT

        # combine both vertical and horizontal alignment together
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)       # CENTER & TOP
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)    # CENTER & BOTTOM 
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)   # CENTER & CENTER

        # Shortcut for double align(horizontally and vertically) center
        label.setAlignment(Qt.AlignCenter)          # CENTER & CENTER

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



