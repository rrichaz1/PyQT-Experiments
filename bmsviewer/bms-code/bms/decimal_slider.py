from PyQt5.QtWidgets import QSlider, QApplication, QVBoxLayout, QLabel, QWidget
from PyQt5.QtCore import Qt

class DecimalSlider(QSlider):
    def __init__(self, orientation=Qt.Horizontal, decimals=2, scale=100, *args, **kwargs):
        super().__init__(orientation, *args, **kwargs)
        self.decimals = decimals  # Number of decimal places
        self.scale = scale  # Scaling factor to simulate decimal values
        self.valueChanged.connect(self.update_label)

    def value(self):
        """Override value() to return a scaled decimal value."""
        return super().value() / self.scale

    def setValue(self, value):
        """Override setValue() to accept a decimal value."""
        scaled_value = int(value * self.scale)
        super().setValue(scaled_value)

    def setRange(self, min_val, max_val):
        """Override setRange() to handle decimal values."""
        scaled_min = int(min_val * self.scale)
        scaled_max = int(max_val * self.scale)
        super().setRange(scaled_min, scaled_max)

    def update_label(self, value):
        """Update label with decimal value whenever the slider is changed."""
        decimal_value = self.value()
        print(f"Slider Value: {decimal_value:.{self.decimals}f}")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create Decimal Slider
        self.slider = DecimalSlider(Qt.Horizontal, decimals=2, scale=100)
        self.slider.setRange(0, 1)  # Set range from 0.0 to 1.0 (scaled internally)
        self.slider.setValue(0.5)   # Set initial value to 0.5
        
        # Create Label to display value
        self.label = QLabel(f"Value: {self.slider.value():.2f}")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Update label on slider change
        self.slider.valueChanged.connect(self.update_label)

    def update_label(self, value):
        decimal_value = self.slider.value()
        self.label.setText(f"Value: {decimal_value:.2f}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
