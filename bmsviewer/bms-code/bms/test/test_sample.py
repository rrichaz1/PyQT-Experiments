import pytest
import numpy as np
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from bms.heatmap import HeatmapWidget   # Import the widget from the main file


# execute the test pytest bms/test/test_sample.py

# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_heatmap_update( qtbot):
    """Test that the heatmap updates with random values 10 times."""
    app = HeatmapWidget()
    qtbot.addWidget(app)

    for _ in range(2):
        # Generate random data and call plot method
        random_data = np.random.rand(10, 10) * 100
        app.plot(random_data)
        
        # Verify that the table has been updated
        for i in range(10):
            for j in range(10):
                item = app.table.item(i, j)
                assert item is not None  # Ensure the cell is not empty
                cell_value = float(item.text())
                assert 0 <= cell_value <= 100  # Check if the value is in the correct range

        # Wait for 1 second between updates (simulate refresh)
        qtbot.wait(1000)
