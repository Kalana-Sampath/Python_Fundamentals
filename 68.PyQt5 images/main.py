# PyQt5 images
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel   
from PyQt5.QtGui import QPixmap
                    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)       # (x, y, width, height)

        pixmap = QPixmap("68.PyQt5 images/profile_pic.jpg")
        label.setPixmap(pixmap)s

        label.setScaledContents(True)           # set size of the scaled
        
        # set the image widow left,right and center
        label.setGeometry((self.width() - label.width()),
                          self.height() - label.height(),
                          label.width(),
                          label.height())

        # to place a center
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
