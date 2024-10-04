from PyQt5.QtCore import pyqtSignal, QObject, QRunnable, pyqtSlot
import numpy as np
import time
import sys

class WorkerSignals(QObject):
    """Defines the signals available from a running worker thread."""
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)  # To pass the heatmap data back to the UI thread
    progress = pyqtSignal(int)

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
            self.signals.finished.emit()

    def stop(self):
        """Stop the worker loop."""
        print("Worker stopped")
        self.is_running = False
        print("Worker stopped flag set to ", self.is_running)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        # self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            print("Thread start")
            result = self.fn(
                *self.args, **self.kwargs
            )
        except:
            traceback.print_exc()
            print("Thread error")
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done    

            