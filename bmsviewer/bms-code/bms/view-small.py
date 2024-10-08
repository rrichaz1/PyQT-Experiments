import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import QThreadPool
from heatmap import HeatmapWidget   

from worker import TimedWorker
import numpy as np


class View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.threadpool = QThreadPool()
        
        # Create HeatmapWidget
        self.heatmap = HeatmapWidget()

        # Create start and stop buttons
        self.start_btn = QPushButton('Start Refresh')
        self.stop_btn = QPushButton('Stop Refresh')

        # Connect buttons to methods
        self.start_btn.clicked.connect(self.start_worker)
        self.stop_btn.clicked.connect(self.stop_worker)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.heatmap)
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()

    def start_worker(self):
        """Start the worker to refresh data every second."""
        self.worker = TimedWorker(self.refresh_data)  # Create worker with refresh_data function
        self.worker.signals.result.connect(self.heatmap.plot)  # Update heatmap in main thread
        self.threadpool.start(self.worker)

    def refresh_data(self):
        """Simulate refreshing data every second."""

        random_data = np.random.rand(10, 10) * 100  # Generate random heatmap data
        print("Refreshing heatmap data...")
        return random_data    

    def stop_worker(self):
        """Stop the background worker."""
        if hasattr(self, 'worker'):
            self.worker.stop()

if __name__ == '__main__':
    app = QApplication([])
    view = View()
    view.resize(1500, 700)
    view.show()
    sys.exit(app.exec())