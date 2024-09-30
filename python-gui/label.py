import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
print("Qt: v", QT_VERSION_STR, "\tPyQt: v", PYQT_VERSION_STR)

class MyLabel(QDialog):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        label = QLabel('Hello World!')
        label.setText('Hello Aaryan!')
        print(label.text())
        label.setAlignment(Qt.AlignCenter)
               # Create a layout and add the label to it
        self.layout = QVBoxLayout()
        self.layout.addWidget(label)
        self.create_Button()
        # Set the layout to the dialog
        self.setLayout(self.layout)

    def buttonClicked(self):
        alert = QMessageBox()
        alert.setText('You clicked the button!')
        alert.exec() 

    def create_Button(self):
        defaultPushButton = QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)
        defaultPushButton.clicked.connect(self.buttonClicked)
        self.layout.addWidget(defaultPushButton)

if __name__ == '__main__':
    # appctxt = ApplicationContext()
    app = QApplication([])
    gallery = MyLabel()
    gallery.show()
    sys.exit(app.exec())

#     app = QtWidgets.QApplication(sys.argv)