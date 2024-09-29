# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QLabel, QLineEdit, QVBoxLayout 
from PyQt5.QtCore import QThreadPool, QSize
from worker import Worker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("Battery Management System")
        self.setMinimumSize(QSize(400, 300))

        self.threadpool = QThreadPool()
        # Create a central widget to hold the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)


        layout = QHBoxLayout()
        vlayout = QVBoxLayout()

        vlayout.addWidget(self.label)
        vlayout.addWidget(self.input)
        layout.addLayout(vlayout)
        button1 = QPushButton("Start")
        button1.setCheckable(True)
        button1.clicked.connect(self.run_task1)
        button1.clicked.connect(self.the_button_was_toggled)
        button1.setChecked(self.button_is_checked)

        self.button2 = QPushButton("Stop")
        # self.button2.setCheckable(True)
        # self.button2.clicked.connect(self.run_task2)
        self.button2.clicked.connect(self.the_button_was_clicked)
        self.button2.released.connect(self.the_button_was_released)
        self.button2.setChecked(self.button_is_checked)
        layout.addWidget(button1)
        # Add a stretchable space
        layout.addStretch(1)  # Adjust the stretch factor as needed
        layout.addWidget(self.button2)
        # self.setCentralWidget(button1)
        # self.setCentralWidget(button2)
        central_widget.setLayout(layout)

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

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print("Checked?", self.button_is_checked)

    def the_button_was_released(self):
        self.button_is_checked = self.button2.isChecked()

        print(self.button_is_checked)    

    def the_button_was_clicked(self):
        self.button2.setText("You already clicked me.")
        self.button2.setEnabled(False)

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")  

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)     

    def mousePressEvent(self, event):
        print("Mouse pressed (event)")     

    def mouseMoveEvent(self, e):
        print("mouseMoveEvent")    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())