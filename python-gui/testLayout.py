import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5 import QtGui

app = QApplication(sys.argv)

window = QWidget()
layout = QGridLayout(window)

# Create some labels
label1 = QLabel("Label 1")
label1.setStyleSheet("background-color: red")
#expand label1 width   
label1.setFixedWidth(100)
label2 = QLabel("Label 2")
label2.setStyleSheet("background-color: blue")
label3 = QLabel("Label 3")
label3.setStyleSheet("background-color: green")

# Add labels to the layout
layout.addWidget(label1, 0, 0)
layout.addWidget(label2, 1, 1)
layout.addWidget(label3, 2, 0)

# Set the stretch factor for the first row to 2
layout.setRowStretch(0, 1)

# Set the stretch factor for the second row to 1
layout.setRowStretch(1, 2)

# Set the stretch factor for the third row to 3
layout.setRowStretch(2, 3)
layout.setColumnStretch(2, 3)

# glay = QGridLayout(window)
# for i in range(3):
#     for j in range(3):
#         label = QLabel("{}x{}".format(i, j))
#         color = QtGui.QColor(*random.sample(range(255), 3))
#         label.setStyleSheet("background-color: {}".format(color.name()))
#         glay.addWidget(label, i, j)
# glay.setRowStretch(0, 1)
# glay.setRowStretch(1, 2)
# glay.setRowStretch(2, 3)
   

# window.setLayout(layout)
window.resize(640, 480)
window.show()
sys.exit(app.exec_())