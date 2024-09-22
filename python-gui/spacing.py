import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

app = QApplication(sys.argv)
window = QWidget()
layout = QHBoxLayout()

button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")

layout.addWidget(button1)
# Add a stretchable space
layout.addStretch(1)  # Adjust the stretch factor as needed
layout.addWidget(button2)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())