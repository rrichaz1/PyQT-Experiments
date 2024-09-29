# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QGridLayout, QSlider
from PyQt5.QtCore import QThreadPool, QSize, Qt
from worker import Worker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

       
        self.button_is_checked = True
        self.setWindowTitle("Battery Management System")
        self.setMinimumSize(QSize(400, 300))

        self.threadpool = QThreadPool()
       
        
       
       
        button1 = QPushButton("Start")
        button1.setCheckable(True)
        button1.setStyleSheet("background-color : green")
        button1.clicked.connect(self.run_task1)
        button1.setChecked(self.button_is_checked)

        self.button2 = QPushButton("Stop")
        # self.button2.setCheckable(True)
        # self.button2.clicked.connect(self.run_task2)
        self.button2.clicked.connect(self.the_button_was_clicked)
        self.button2.setChecked(self.button_is_checked)
        self.button2.setStyleSheet("background-color : red")
        
        self.create_slider()
        
        bottomlayout = QHBoxLayout()
        
        bottomlayout.addWidget(button1)
        # Add a stretchable space
        bottomlayout.addStretch(1)  # Adjust the stretch factor as needed
        bottomlayout.addWidget(self.slider)


        bottomlayout.addWidget(self.button2)
        # self.setCentralWidget(button1)
        # self.setCentralWidget(button2)

        ##create a widget to hold the layout
        widget = QWidget()
        widget.setLayout(bottomlayout)

        ## Add a grid bottomlayout to the central widget
        gridlayout = QGridLayout()
        ##create a empty widget to fill the top space
        gridlayout.addWidget(QWidget(), 0, 0)
        ## Add bottomlayount with buttons and slider at bottom
        
        gridlayout.addWidget(widget, 3, 0)

         # Create a central widget to hold the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(gridlayout)

    def create_slider(self):
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(30)
        self.slider.setSingleStep(3)
        self.slider.setSizeIncrement(3, 0)
        self.slider.setGeometry(10, 10, 200, 30)
        self.slider.valueChanged.connect(self.value_changed)
        self.slider.sliderMoved.connect(self.slider_position)
        self.slider.sliderPressed.connect(self.slider_pressed)
        self.slider.sliderReleased.connect(self.slider_released)



    def run_task1(self):
        worker = Worker(self.task1_function)
        self.threadpool.start(worker)

    def run_task2(self):
        worker = Worker(self.task2_function)
        self.threadpool.start(worker)

    def task1_function(self):
        # Long-running task 1
        print("Task 1 started - stopped")
        

    def task2_function(self):
        # Long-running task 2
        print("Task 2 started")

    def the_button_was_clicked(self):
        self.button2.setText("You already clicked me.")
        self.button2.setEnabled(False)

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")  


    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())