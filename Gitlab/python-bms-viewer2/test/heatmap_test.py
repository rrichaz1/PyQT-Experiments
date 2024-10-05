import pytest
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtTest import *
from PyQt5.QtCore import *
from pythonGUI.heatmap import Heatmap   # Import the widget from the main file

# execute the test with pytest test/heatmap_test.py
# if everything works, the terminal will say test passed

def test_voltage_heatmap(qtbot):
    test_app = Heatmap(3.0, 4.2, "Voltage")
    qtbot.addWidget(test_app)

    """Test that the heatmap updates with random values 10 times."""
    for _ in range(10):
        # Generate random data and call plot method
        random_data = (np.random.rand(12, 12) * 2.5) + 2.5
        test_app.plot(random_data)
        
        # Verify that the table has been updated
        for i in range(12):
            for j in range(12):
                item = test_app.table.item(i, j)
                assert item is not None
                cell_value = float(item.text())
                assert 2.5 <= cell_value <= 5.0  # Check if the value is in the correct range

        # Wait for 2 seconds between updates (simulate refresh)
        qtbot.wait(2000)

def test_temperature_heatmap(qtbot):
    test_app = Heatmap(0.0, 60.0, "Temperature")
    qtbot.addWidget(test_app)

    """Test that the heatmap updates with random values 10 times."""
    for _ in range(10):
        # Generate random data and call plot method
        random_data = (np.random.rand(12, 12) * 80) - 10
        test_app.plot(random_data)
        
        # Verify that the table has been updated
        for i in range(12):
            for j in range(12):
                item = test_app.table.item(i, j)
                assert item is not None
                cell_value = float(item.text())
                assert -10.0 <= cell_value <= 70.0  # Check if the value is in the correct range

        # Wait for 2 seconds between updates (simulate refresh)
        qtbot.wait(2000)
