# Python PyQt5 Stopwatch
# create a stopwatch widget using python's PyQt5 library.

# Importing required libraries for PyQt5 Digital Clock

# Core Application Structure:
# sys + QApplication = Basic application framework to run the app
# QWidget = Main window/container for UI elements
# QVBoxLayout, QHBoxLayout = Organize widgets vertically or horizontally

# Display & Timing:
# QLabel = Display text or images (e.g., showing time)
# QPushButton = Interactive button widget
# QTimer = Timer for periodic updates (refresh display)
# QTime = Time representation and formatting
# Qt = Constants for alignment, styling, and behavior
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

# Create a class called Stopwatch, which inherits from QWidget
class Stopwatch(QWidget):
    def __init__(self):
        # Initialize the QWidget superclass (sets up the main window)
        super().__init__()
        # Create a QTime object to keep track of stopwatch time (hours, minutes, seconds, milliseconds)
        self.time = QTime(0, 0, 0, 0) 
        # QLabel widget to display the current stopwatch time in "HH:MM:SS.ms" format
        self.time_label = QLabel("00:00:00.00", self)
        # QPushButton to start/resume the stopwatch
        self.start_button = QPushButton("Start", self)
        # QPushButton to pause/stop the stopwatch
        self.stop_button = QPushButton("Stop", self)
        # QPushButton to reset the stopwatch time back to zero
        self.reset_button = QPushButton("Reset", self)
        # QTimer object to trigger periodic updates (every few milliseconds) to the time_label
        # It emits a 'timeout' signal at a defined interval, which will be connected to an update function
        self.timer = QTimer(self)
        # Call the method initUI() to set up the user interface
        self.initUI()
    
    # if within this method we will be designing the layout of the stopwatch
    def initUI(self):
        # set the title for window
        self.setWindowTitle("Stopwatch")

        # use the vertical layout manager for labels and buttons
        vbox = QVBoxLayout()
        # get the layout manager and add the following widget
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        # Align the time label text to the center of the widget
        self.time_label.setAlignment(Qt.AlignCenter)        

        # Create a horizontal layout to arrange the Start, Stop, and Reset buttons side by side
        hbox = QHBoxLayout()

        # Add each button to the horizontal layout
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        # Add the horizontal button layout to the main vertical layout
        # This ensures the buttons appear below the time label while keeping the overall layout vertical
        vbox.addLayout(hbox)

        # applying a style sheet
        self.setStyleSheet("""
                           QPushButton, QLabel{
                               padding: 20px;
                               font-weight: bold;
                           }                                                          
                           QPushButton{
                               font-size: 50px;
                           }
                           QLabel{
                               font-size: 120px;
                               background-color: #b3e5ff;
                               border-radius: 20px;
                           }
                           """)

        # Connect the Start button to the start() method → begins/resumes the stopwatch
        self.start_button.clicked.connect(self.start)

        # Connect the Stop button to the stop() method → pauses the stopwatch
        self.stop_button.clicked.connect(self.stop)

        # Connect the Reset button to the reset() method → resets time back to 00:00:00.00
        self.reset_button.clicked.connect(self.reset)

        # Connect the QTimer's timeout signal to update_display()
        # → this ensures the time label is refreshed at regular intervals (every tick of the timer)
        self.timer.timeout.connect(self.update_display)

    # method to start the stopwatch (timer triggers every 10 ms)
    def start(self):
        self.timer.start(10)

    # method to stop the stopwatch (pause counting)
    def stop(self):
        self.timer.stop()

    # method to reset the stopwatch (set time back to 0)
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    # method to format the time (convert QTime -> hh:mm:ss.ms string)
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"

    # method to update the time (increase by 10 ms & refresh label display)
    def update_display(self):
        self.time = self.time.addMSecs(10)  # add 10 ms to time object
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

