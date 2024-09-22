# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget 
from PyQt5.QtCore import QThreadPool
from worker import Worker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.threadpool = QThreadPool()
        # Create a central widget to hold the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()

        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.run_task1)

        button2 = QPushButton("Button 2")
        button2.clicked.connect(self.run_task2)
        layout.addWidget(button1)
        # Add a stretchable space
        layout.addStretch(1)  # Adjust the stretch factor as needed
        layout.addWidget(button2)
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
        print("Task 1 started")

    def task2_function(self):
        # Long-running task 2
        print("Task 2 started")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())