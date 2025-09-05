# PyQt5 introduction

# pip install PyQt5

import sys 
#This module provides access to some variables used or maintained by the interpreter and to functions 
# that interact strongly with the interpreter. It is always available.

from PyQt5.QtWidgets import QApplication, QMainWindow   # Widgets are the building blocks of a PyQT5 application, 
                                                        # begin with Q. That helps distinguish them from other libraries
                    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
    
# sys.argv
# The list of command line arguments passed to a Python script. argv[0] is the script name 
# (it is operating system dependent whether this is a full pathname or not). If the command 
# was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. 
# If no script name was passed to the Python interpreter, argv[0] is the empty string.

# this is a boilerplate code that we need for a basic window.



# -----------------------------------------------------------------------------------------------
# ------------ Let's customize it. --------------------------------------------------------------

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow   
from PyQt5.QtGui import QIcon
                    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("66.PyQt5 GUI intro/profile_pic.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

