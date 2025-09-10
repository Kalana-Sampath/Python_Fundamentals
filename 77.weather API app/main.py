import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

# Create a class called WeatherApp, which inherits from QWidget
class WeatherApp(QWidget):
    # constructor method (initialize the WeatherApp window)
    def __init__(self):  
        super().__init__()  # call QWidget constructor to set up the base class
        self.initUI()

    def initUI(self):
        # create a label asking the user to enter a city name
        self.city_label = QLabel("Enter city name: ", self)
        
        # create a text box for typing the city name
        self.city_input = QLineEdit(self)
        
        # create a button to fetch weather info
        self.get_weather_button = QPushButton("Get Weather", self)
        
        # create a label to display the temperature (° = Alt+0176)
        self.temperature_label = QLabel(self)   # Alt + 0176 for degree symbol
        
        # create a label to display a weather emoji (e.g., ☀️, 🌧️, ❄️)
        self.emoji_label = QLabel(self)
        
        # create a label to show weather description (e.g., Sunny, Rainy)
        self.desciption_label = QLabel(self)

        # set the window title
        self.setWindowTitle("Weather App")

        # create a vertical layout container
        vbox = QVBoxLayout()
        
        # add all widgets to the layout in order (top → bottom)
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desciption_label)
        
        # apply the layout to the main window
        self.setLayout(vbox)
        
        # center-align all labels and input field
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desciption_label.setAlignment(Qt.AlignCenter)
        
        # set unique object names for widgets (used for styling)
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.desciption_label.setObjectName("desciption_label")

        # apply stylesheet to widgets using object names
        self.setStyleSheet("""
                            QLabel, QPushButton{
                                font-family: calibri;
                            }
                            QLabel#city_label{
                                font-size: 40px;
                                font-style: italic;
                            }
                            QLineEdit#city_input{
                                font-size: 40px;
                            }
                            QPushButton#get_weather_button{
                                font-size: 30px;
                                font-weight: bold;
                            }
                            QLabel#temperature_label{
                                font-size: 75px;
                            }
                            QLabel#emoji_label{
                                font-size: 100px;
                                font-family: Segoe UI emoji;
                            }
                            QLabel#desciption_label{
                                font-size: 50px;
                            }
                           """)

        # connect the "Get Weather" button click to the get_weather method
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        # OpenWeatherMap API key
        api_key = "49a2ce203d761e68f737abe6d9c2eb05"
        # get city name from user input
        city = self.city_input.text()
        # build the API request URL
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url)       # send GET request to API
            response.raise_for_status()        # raise HTTPError for bad status
            data = response.json()             # parse JSON response
        
            # if request successful, display weather
            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            # handle specific HTTP errors using status code
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not Found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")
        
        # handle other request exceptions
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        # display error message in temperature label (smaller font)
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.desciption_label.clear()

    def display_weather(self, data):
        # display temperature in large font
        self.temperature_label.setStyleSheet("font-size: 75px;")
        
        # convert temperature from Kelvin to Celsius and Fahrenheit
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67

        weather_id = data["weather"][0]["id"]
        
        # get weather description from API data
        weather_description = data["weather"][0]["description"]
        
        # update temperature and description labels
        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.desciption_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        
        if 200 <= weather_id <= 232:                         # weather_id >= 200 and weather_id <= 232
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌥️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif 762 == weather_id:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🍃"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else: 
            return " "
    
        

# main entry point of the program
if __name__ == "__main__":
    app = QApplication(sys.argv)       # create the Qt application object
    weather_app = WeatherApp()         # create an instance of the WeatherApp window
    weather_app.show()                 # display the WeatherApp window
    sys.exit(app.exec_())              # start the event loop and exit cleanly on close
