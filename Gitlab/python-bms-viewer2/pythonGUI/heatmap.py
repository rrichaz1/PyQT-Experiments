from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class TableBorder(QStyledItemDelegate):
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


class Heatmap(QWidget):
    def __init__(self, min, max, title):
        super().__init__()
        self.max_safe = max
        self.min_safe = min

        self.title = title
        self.table_title = QLabel(self.title + " Heatmap")
        self.table_title.setStyleSheet("font-size: 18px;")
        self.table_title.setAlignment(Qt.AlignCenter)
        self.table = QTableWidget(12, 12)

        border = TableBorder(self.table)
        self.table.setItemDelegate(border)
        layout = QVBoxLayout()
        layout.addWidget(self.table_title)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def plot(self, heatmapData):
        """Update the table with new heatmap data."""
        for i in range(12):
            for j in range(12):
                item = QTableWidgetItem(f"{heatmapData[i][j]:.2f}")
                value = heatmapData[i][j]
                if value > self.max_safe:
                    item.setBackground(QBrush(QColor(255, 0, 0))) # red
                elif value < self.min_safe:
                    item.setBackground(QBrush(QColor(0, 0, 255))) # blue
                self.table.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Heatmap()
    widget.resize(1500, 700)
    widget.show()
    sys.exit(app.exec_())
