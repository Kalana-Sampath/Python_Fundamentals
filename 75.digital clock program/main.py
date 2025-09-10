# Python PyQt5 Digital Clock
# create a digital clock widget using python's PyQt5 library.

# import following library 
# Core Application Structure:

# sys + QApplication = Basic app framework
# QWidget = Main window container
# QVBoxLayout = Vertical organization of elements

# Display & Timing:

# QLabel = Text/image display (for showing time)
# QTimer = Periodic updates (refreshing the display)
# QTime = Time manipulation and formatting
# Qt = Constants for alignment, styling, and behavior
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
# To Work with specific fonts, we will nedd the following 
from PyQt5.QtGui import QFont, QFontDatabase

# Create a class called DigitalClock, which inherits from QWidget
class DigitalClock(QWidget):
    
    def __init__(self):
        # Call the constructor of the parent class (QWidget) 
        # to properly initialize the base functionality of QWidget
        super().__init__()

        # Call the method initUI() to set up the user interface
        self.initUI()
    
    # if within this method we will be designing the layout of the digital clock 
    def initUI(self):
        
        # this label display the time
        self.time_label = QLabel(self)
        # we are addig to the timer to the clock
        # QTimer object to update the time every second
        
        # ------------------- for testing purpose -------------------------
        # temporarily create a QLabel with placeholder text
        # self.time_label = QLabel("12:00:00", self)
        # this label will later display the actual current time
        # "12:00:00" is just an initial placeholder for layout purposes
        # -----------------------------------------------------------------
        
        self.timer = QTimer(self)

        # designing the layout of our clock
        # set the title of the application window
        self.setWindowTitle("Digital Clock")
        # set the position (x=600, y=400) and size (width=300, height=100) of the window
        self.setGeometry(600, 400, 300, 100)

       # add a vertical box layout manager to control widget arrangement
        vbox = QVBoxLayout()
        # add our time label widget into the layout (stacked vertically)
        vbox.addWidget(self.time_label)
        # apply the layout to the main window so all widgets follow this layout
        self.setLayout(vbox)

        # set the label horizontally - center text
        self.time_label.setAlignment(Qt.AlignCenter)

        # set the font - big green text
        self.time_label.setStyleSheet("font-size: 150px;"
                                    # "font-family: Arial;"       # delete this one becsuse of use specific font
                                    "color: #26ff00;")

        # change the background color - black background
        self.setStyleSheet("background-color: black;")


        # add specific font - load custom font file into the app
        font_id = QFontDatabase.addApplicationFont("75.digital clock program/DS-DIGIT.TTF")
        # create a local variable - get font family name from loaded font
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        # set a font - create QFont object with custom family and size 150
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)  # apply custom font to label


        # update every second - connect timer to update_time, triggers every 1000 ms
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # start timer with 1-second interval


        # call update_time - refresh clock
        self.update_time()  

# create a method to update time - update clock
    def update_time(self):
    # get the current time - current time
        current_time = QTime.currentTime().toString("hh:mm:ss AP")      # format - hh:mm:ss AM/PM
    # set the text of the label - show time
        self.time_label.setText(current_time)



# This block ensures that the code only runs when this file
# is executed directly, and not when it is imported as a module
if __name__ == "__main__":
    
    # Create the QApplication object
    # - sys.argv passes command line arguments to the application
    # - Every PyQt5 app needs exactly ONE QApplication object
    # - It manages the GUI application's control flow and main settings
    app = QApplication(sys.argv)
    
    # Create an instance of our custom DigitalClock widget
    # - This object represents the digital clock window
    clock = DigitalClock()
    
    # Show the clock widget on the screen
    # - Without calling .show(), the window will not appear
    clock.show()
    
    # Start the application's event loop
    # - sys.exit() ensures a clean exit when the app is closed
    # - app.exec_() enters the Qt event loop, keeping the window responsive
    sys.exit(app.exec_())



    
