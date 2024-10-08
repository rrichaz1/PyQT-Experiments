from PyQt5.QtCore import *
import traceback, sys, time

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)

class Worker(QRunnable):
    def __init__(self, function):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.function = function

    @pyqtSlot()
    def run(self):
        self.function()

class TimedWorker(QRunnable):
    """Worker thread that periodically refreshes data."""
    
    def __init__(self, fn, *args, **kwargs):
        super(TimedWorker, self).__init__()
        self.fn = fn  # Function to execute (data processing)
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.is_running = True  # Flag to control the loop
        print("Worker initialized")

    @pyqtSlot()
    def run(self):
        """Run the data processing function repeatedly every second."""
        print("Worker started")
        try:
            while self.is_running:
                result = self.fn(*self.args, **self.kwargs)  # Call the heatmap processing function
                self.signals.result.emit(result)  # Emit the result (heatmap data) to the UI
                time.sleep(1)  # Wait for 1 second between updates
                print("Worker flag set to ", self.is_running)

        except Exception as e:
            exctype, value, tb = sys.exc_info()
            self.signals.error.emit((exctype, value, tb))
        finally:
            self.signals.finished.emit()  # Done
    
    def stop(self):
        """Stop the worker loop."""
        self.is_running = False
