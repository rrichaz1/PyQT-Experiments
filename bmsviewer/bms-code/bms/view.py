from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QGridLayout, QWidget, QSlider, QLabel
from PyQt5.QtCore import QThreadPool, Qt
from worker import Worker
import sys
from heatmap import HeatmapWidget   

class View(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMS Viewer") # sets window title when run
        self.threadpool = QThreadPool() # creates threadpool for multithreading purposes
        
        self.bottomLayout = QHBoxLayout() # creates a horizontal layout for the buttons and slider at the bottom of the window
        widget = QWidget(self) # creates a widget to hold the buttons and slider
        widget.setLayout(self.bottomLayout) # sets the layout of the widget to the bottomLayout
        
        self.create_buttons() # calls the create_buttons function
        self.create_labels() # calls the create_labels function
        self.create_slider() # calls the create_slider function
        self.set_layout() # calls the set_layout function to add buttons and slider to the layout
        self.heatmap = HeatmapWidget()

        central_widget = QWidget(self)
        gridLayout = QGridLayout()
        gridLayout.addWidget(QWidget(), 0, 0) # fills row 1 for now
        gridLayout.addWidget(QWidget(), 1, 0) #fills row 2 for now
        gridLayout.addWidget(QWidget(), 2, 0) #fills row 3 for now
        gridLayout.addWidget(widget, 3, 0) # adds the widget with buttons and slider to row 4
        
        central_widget = QWidget(self) # creates a central widget to hold the grid layout
        self.setCentralWidget(central_widget) # sets the central widget to the central widget
        central_widget.setLayout(gridLayout) # sets the layout of the central widget to the grid layout

    def create_labels(self):
        self.amperage = QLabel("Amps") # creates a label stating the slider changes the amperage
        self.amperage.setAlignment(Qt.AlignVCenter) # aligns the label to the center
        self.amperage.setFixedSize(50, 30) # sets the size of the label
        self.ampCount = QLabel("0") # creates a label to display the initial amperage
        self.ampCount.setFixedSize(400, 50) # sets the size of the counter label

    def create_slider(self):
        self.slider = QSlider(Qt.Horizontal) # creates a horizontal slider
        self.slider.setMinimum(0) # sets the minimum value of the slider to 0
        self.slider.setMaximum(150) # sets the maximum value of the slider to 150
        self.slider.setSingleStep(1) # sets the step of the slider to 1
        self.slider.setFixedWidth(200) # sets the width of the slider to 200
        self.slider.valueChanged.connect(self.value_changed) # connects the valueChanged signal to the value_changed function
        self.slider.sliderMoved.connect(self.slider_position) # connects the sliderMoved signal to the slider_position function
        self.slider.sliderPressed.connect(self.slider_pressed) # connects the sliderPressed signal to the slider_pressed function
        self.slider.sliderReleased.connect(self.slider_released) # connects the sliderReleased signal to the slider_released function

    def create_buttons(self): 
        self.quitButton = QPushButton("Quit") # creates a quit button
        self.quitButton.setStyleSheet("background-color: grey; border-radius: 5px") # sets the style of the button
        self.quitButton.setFixedSize(50, 50) # sets the size of the quit button
        self.quitButton.clicked.connect(self.quit_button_clicked) # connects the clicked signal to the quit_button_clicked function

        self.resetButton = QPushButton("Reset") # creates a reset button
        self.resetButton.setStyleSheet("background-color: blue; border-radius: 5px") # sets the style of the reset button
        self.resetButton.setFixedSize(150, 50) # sets the size of the reset button
        self.resetButton.clicked.connect(self.reset_button_clicked) # connects the clicked signal to the reset_button_clicked function

        self.startButton = QPushButton("Start") # creates a start button
        self.startButton.setStyleSheet("background-color: green; border-radius: 5px") # sets the style of the start button
        self.startButton.setFixedSize(150, 50) # sets the size of the start button
        self.startButton.clicked.connect(self.start_button_clicked) # connects the clicked signal to the start_button_clicked function

        self.stopButton = QPushButton("Stop") # creates a stop button
        self.stopButton.setStyleSheet("background-color: red; border-radius: 5px") # sets the style of the stop button
        self.stopButton.setFixedSize(150, 50) # sets the size of the stop button
        self.stopButton.clicked.connect(self.stop_button_clicked) # connects the clicked signal to the stop_button_clicked function

    def set_layout(self):
        self.bottomLayout.addWidget(self.quitButton) # adds the quit button to the bottom layout
        self.bottomLayout.addWidget(QWidget()) # adds a blank widget to the bottom layout
        self.bottomLayout.addWidget(self.amperage) # adds the amperage label to the bottom layout
        self.bottomLayout.addWidget(self.slider) # adds the slider to the bottom layout
        self.bottomLayout.addWidget(self.ampCount) # adds the amperage counter label to the bottom layout
        self.bottomLayout.addWidget(self.resetButton) # adds the reset button to the bottom layout
        self.bottomLayout.addWidget(self.startButton) # adds the start button to the bottom layout
        self.bottomLayout.addWidget(self.stopButton) # adds the stop button to the bottom layout
    
    def start_button_clicked(self):
        worker = Worker(self.start_thread_function) # creates a worker object with the start_thread_function
        self.threadpool.start(worker) # starts the worker
    
    def stop_button_clicked(self):
        worker = Worker(self.stop_thread_function) # creates a worker object with the stop_thread_function
        self.threadpool.start(worker) # starts the worker

    def reset_button_clicked(self):
        worker = Worker(self.reset_thread_function) # creates a worker object with the reset_thread_function
        self.threadpool.start(worker) # starts the worker

    def quit_button_clicked(self):
        worker = Worker(self.quit_thread_function) # creates a worker object with the quit_thread_function
        self.threadpool.start(worker) # starts the worker

    def start_thread_function(self):
        print("Start button clicked") # prints to the console when the start button is clicked

    def stop_thread_function(self):
        print("Stop button clicked") # prints to the console when the stop button is clicked
    
    def reset_thread_function(self):
        print("Reset button clicked") # prints to the console when the reset button is clicked

    def quit_thread_function(self):
        print("Quit button clicked") # prints to the console when the quit button is clicked

    def value_changed(self, current_value):
        self.ampCount.setText(str(current_value)) # sets the text of the label to the current value of the slider 
        print(current_value) # prints the current value of the slider to the console

    def slider_position(self, pos):
        print(pos) # prints the position of the slider to the console

    def slider_pressed(self):
        print("Slider pressed") # prints to the console when the slider is pressed
    
    def slider_released(self):
        print("Slider released") # prints to the console when the slider is released


if __name__ == '__main__':
    app = QApplication([])
    view = View()
    view.resize(1500, 700)
    view.show()
    sys.exit(app.exec())
