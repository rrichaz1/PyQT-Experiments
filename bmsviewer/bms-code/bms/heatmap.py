import sys
import numpy as np
import time
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QStyledItemDelegate, QStyleOptionViewItem, QStyle
from PyQt5.QtGui import QColor, QBrush, QPen, QPainter

from PyQt5.QtCore import QTimer, QModelIndex, Qt

class BorderDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        # Draw the default item content
        super().paint(painter, option, index)

        # Draw the border
        if option.state & QStyle.State_Selected:
            # Adjust the border color for selected items
            painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        else:
            painter.setPen(QPen(Qt.gray, 1, Qt.SolidLine))

        rect = option.rect.adjusted(1, 1, -1, -1)  # Adjust for border width
        painter.drawRect(rect)

class HeatmapWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget(10, 10)

        # Apply the custom delegate to the table
        delegate = BorderDelegate(self.table)
        self.table.setItemDelegate(delegate)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
        
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.refresh_data)
        # self.timer.start(1000)  # Refresh every 1 second

    def plot(self, heatmapData):
        """Update the table with new heatmap data."""
        print("Plotting heatmap data...")
        rows, cols = heatmapData.shape
        for i in range(rows):
            for j in range(cols):
                item = QTableWidgetItem(f"{heatmapData[i][j]:.2f}")
                value = heatmapData[i][j]
                 # Apply color based on the value
                if value > 70:
                    item.setBackground(QBrush(QColor(255, 0, 0)))  # Red for values > 70
                elif value < 30:
                    item.setBackground(QBrush(QColor(0, 0, 255)))  # Blue for values < 30
                else:
                    item.setBackground(QBrush(QColor(0, 0, 0)))  # Black for other values
                self.table.setItem(i, j, item)

  
    def refresh_data(self):
        """Simulate refreshing data every second."""
        random_data = np.random.rand(10, 10) * 100  # Generate random heatmap data
        print("Refreshing heatmap data...")
        return random_data   


    def print_result(self, s):
        print(s)

    def complete(self):
        print("REFRESH COMPLETE!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = HeatmapWidget()
    widget.show()
    sys.exit(app.exec_())
