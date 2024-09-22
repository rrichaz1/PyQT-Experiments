# worker.py

from PyQt5.QtCore import QRunnable, pyqtSignal, pyqtSlot

class Worker(QRunnable):
    def __init__(self, function):
        super().__init__()
        self.function = function

    @pyqtSlot()
    def run(self):
        self.function()