# PyQt5 setStyleSheet()
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout
                    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.button1 = QPushButton('#1')
        self.button2 = QPushButton('#2')
        self.button3 = QPushButton('#3')
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        
        central_widget.setLayout(hbox)

        # Apply CSS properties to only one widget rather than all of them
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
         
        
        # Rather than applying CSS properties individually such as \  self.button.setStyleSheet() \
        # we use self.setStyleSheet() to the main window 
        # Insted of using double quote we use triple quotes, triple quote is used to write very long string 
        # in a more organized way. 
        # we could select entire class too (QPushButton) 

        self.setStyleSheet("""
                           QPushButton{
                               font-size: 40px;
                               font-family: Arial;
                               padding: 15px 75px;
                               margin: 25px;
                               border: 3px solid;
                               border-radius: 15px;
                           }
                           QPushButton#button1{
                               background-color: #ffeab8;
                           }
                           QPushButton#button2{
                               background-color: #1e81b0;
                           }
                           QPushButton#button3{
                               background-color: #abdbe3;
                           }
                           QPushButton#button1:hover{
                               background-color: #D94542;
                           }
                           QPushButton#button2:hover{
                               background-color: #D94542;
                           }
                           QPushButton#button3:hover{
                               background-color: #D94542;
                           }
                           """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()