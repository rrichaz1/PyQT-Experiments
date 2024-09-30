import sys
import numpy as np
import time
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer

class HeatmapWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(10, 10)
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_data)
        self.timer.start(1000)  # Refresh every 1 second

    def plot(self, heatmapData):
        """Update the table with new heatmap data."""
        for i in range(10):
            for j in range(10):
                item = QTableWidgetItem(f"{heatmapData[i][j]:.2f}")
                self.table.setItem(i, j, item)

    def refresh_data(self):
        """Simulate refreshing data every second."""
        random_data = np.random.rand(10, 10) * 100  # Generate random heatmap data
        self.plot(random_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = HeatmapWidget()
    widget.show()
    sys.exit(app.exec_())
