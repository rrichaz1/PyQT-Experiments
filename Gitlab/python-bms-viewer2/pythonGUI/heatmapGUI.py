from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from worker import Worker, TimedWorker
from heatmap import Heatmap
import numpy as np
import sys

class HeatmapGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMS Viewer") 
        self.threadpool = QThreadPool() 
        
        self.bottomLayout = QHBoxLayout() 
        widget = QWidget(self) 
        widget.setLayout(self.bottomLayout) 
        
        self.create_buttons() 
        self.create_labels() 
        self.create_slider() 
        self.set_layout()
        self.voltage_heatmap = Heatmap(3.0, 4.2, "Voltage") 
        self.temperature_heatmap = Heatmap(0.0, 60.0, "Temperature") 

        central_widget = QWidget(self) 
        gridLayout = QGridLayout() 
        gridLayout.addWidget(QWidget(), 0, 0) 
        gridLayout.addWidget(self.voltage_heatmap, 1, 0)
        gridLayout.addWidget(self.temperature_heatmap, 2, 0) 
        gridLayout.addWidget(widget, 3, 0) 
        
        central_widget = QWidget(self) 
        self.setCentralWidget(central_widget) 
        central_widget.setLayout(gridLayout) 

        QTimer.singleShot(0, self.start_workers)
        self.show()

    def create_labels(self):
        self.amperage = QLabel("Amps")
        self.amperage.setAlignment(Qt.AlignVCenter) 
        self.amperage.setFixedSize(50, 30) 
        self.ampCount = QLabel("0") 
        self.ampCount.setFixedSize(400, 50) 

    def create_slider(self):
        self.slider = QSlider(Qt.Horizontal) 
        self.slider.setMinimum(0) 
        self.slider.setMaximum(150) 
        self.slider.setSingleStep(1) 
        self.slider.setFixedWidth(200)
        self.slider.valueChanged.connect(self.value_changed) 
        self.slider.sliderMoved.connect(self.slider_position) 
        self.slider.sliderPressed.connect(self.slider_pressed) 
        self.slider.sliderReleased.connect(self.slider_released) 

    def create_buttons(self): 
        self.quitButton = QPushButton("Quit") 
        self.quitButton.setStyleSheet("background-color: grey; border-radius: 5px") 
        self.quitButton.setFixedSize(50, 50) 
        self.quitButton.clicked.connect(self.quit_button_clicked)

        self.resetButton = QPushButton("Reset") 
        self.resetButton.setStyleSheet("background-color: blue; border-radius: 5px")
        self.resetButton.setFixedSize(150, 50)
        self.resetButton.clicked.connect(self.reset_button_clicked) 

        self.startButton = QPushButton("Start")
        self.startButton.setStyleSheet("background-color: green; border-radius: 5px") 
        self.startButton.setFixedSize(150, 50) 
        self.startButton.clicked.connect(self.start_button_clicked) 

        self.stopButton = QPushButton("Stop") 
        self.stopButton.setStyleSheet("background-color: red; border-radius: 5px") 
        self.stopButton.setFixedSize(150, 50) 
        self.stopButton.clicked.connect(self.stop_button_clicked) 

    def set_layout(self):
        self.bottomLayout.addWidget(self.quitButton) 
        self.bottomLayout.addWidget(QWidget()) 
        self.bottomLayout.addWidget(self.amperage)
        self.bottomLayout.addWidget(self.slider)
        self.bottomLayout.addWidget(self.ampCount) 
        self.bottomLayout.addWidget(self.resetButton) 
        self.bottomLayout.addWidget(self.startButton) 
        self.bottomLayout.addWidget(self.stopButton) 

    def start_workers(self):
        """Start the worker to refresh temperature data every second."""
        self.worker = TimedWorker(self.refresh_temperature_data) 
        self.worker.signals.result.connect(self.temperature_heatmap.plot) 
        self.threadpool.start(self.worker)
        """Start the worker to refresh voltage data every second."""
        self.worker = TimedWorker(self.refresh_voltage_data) 
        self.worker.signals.result.connect(self.voltage_heatmap.plot)  
        self.threadpool.start(self.worker)

    def refresh_voltage_data(self):
        """Simulate refreshing voltage data every 3 seconds."""
        random_data = (np.random.rand(12, 12) * 2.5) + 2.5
        self.voltage_heatmap.plot(random_data) 

    def refresh_temperature_data(self):
        """Simulate refreshing temperature data every 3 seconds."""
        random_data = (np.random.rand(12, 12) * 80) - 10
        self.temperature_heatmap.plot(random_data)
    
    def start_button_clicked(self):
        worker = Worker(self.start_thread_function) 
        self.threadpool.start(worker) 
    
    def stop_button_clicked(self):
        worker = Worker(self.stop_thread_function) 
        self.threadpool.start(worker) 

    def reset_button_clicked(self):
        worker = Worker(self.reset_thread_function) 
        self.threadpool.start(worker) 

    def quit_button_clicked(self):
        worker = Worker(self.quit_thread_function) 
        self.threadpool.start(worker) 

    def start_thread_function(self):
        print("Start button clicked") 

    def stop_thread_function(self):
        print("Stop button clicked") 
    
    def reset_thread_function(self):
        print("Reset button clicked") 

    def quit_thread_function(self):
        print("Quit button clicked") 

    def value_changed(self, current_value):
        self.ampCount.setText(str(current_value)) 
        print(current_value) 

    def slider_position(self, pos):
        print(pos) 

    def slider_pressed(self):
        print("Slider pressed") 
    
    def slider_released(self):
        print("Slider released") 


if __name__ == '__main__':
    app = QApplication([])
    heatmapGUI = HeatmapGUI()
    heatmapGUI.resize(2000, 1500)
    heatmapGUI.show()
    sys.exit(app.exec())
