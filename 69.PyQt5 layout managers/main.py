# PyQt5 layouts
import sys 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                                QWidget, QVBoxLayout, QHBoxLayout, QGridLayout) 
                    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()       
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

# anything that deals with the user interface, we are going to be write within 
# these function normally we can not add a layout manager to a main window object
# main window widgets have a specific design in layout structure 

    # to organize the widgets
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("#1", self)          
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")
        
        # then want a layout manager to avoid a overlapping 
        vbox = QVBoxLayout()
        
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        
        central_widget.setLayout(vbox)      # all the labels are arrange vertically
        
        
        # arrange all the labels in horizontal way
        hbox = QHBoxLayout()
        
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)
        
        central_widget.setLayout(hbox)
        
        
        # Grid widget
        grid = QGridLayout()
        
        grid.addWidget(label1, 0, 0)      # we want a add row and column number
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 2)
        
        central_widget.setLayout(grid)
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()