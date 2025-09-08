# PyQt5 Checkboxes
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox   
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
        
    def initUI(self):
        self.checkbox = QCheckBox("Do you like food?", self)
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        # inital state of the checkbox (like check or uncheck)
        self.checkbox.setChecked(False)

        # add some functionalty to the checkbox 
        self.checkbox.stateChanged.connect(self.checkbox_changed)   # checkbox.*signal*.connect(*slot*)

    # add some functionalty to the checkbox 
    def checkbox_changed(self, state):
        if state == Qt.Checked:                # Qt.Checked also equal to 2 mean, checked
            print("You like food")
        else:
            print("You DO NOT like food")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()