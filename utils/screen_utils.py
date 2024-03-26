from PySide6.QtCore import QRect
from PySide6.QtGui import QGuiApplication, QScreen
from PySide6.QtWidgets import QComboBox, QApplication


def populateScreensComboBox(comboBox: QComboBox):
    screens = QGuiApplication.screens()
    for screen in screens:
        print(screen.name())  # Debug print to check screen names
        comboBox.addItem(screen.name())


def calculate_total_geometry():
    total_rect = QRect()
    for screen in QApplication.screens():
        total_rect = total_rect.united(screen.geometry())
    return total_rect

