from PySide6.QtCore import Qt, QRect, QPoint, Signal
from PySide6.QtWidgets import QWidget, QApplication, QRubberBand

from utils.screen_utils import calculate_total_geometry


class DynamicAlignmentWindow(QWidget):
    positionSelected = Signal(int, int)

    def __init__(self, main_window, width, height):
        super().__init__()
        self.main = main_window
        self.main.hide()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowOpacity(0.5)
        self.setStyleSheet("background-color: rgba(0, 0, 255, 38);")

        self.lastPosition = None  # Initialize last known position

        # Calculate total screen geometry and set window geometry
        total_screen_rect = calculate_total_geometry()
        self.setGeometry(total_screen_rect)

        # Translate the primary screen geometry to widget-based coordinates
        origin = total_screen_rect.topLeft()
        primary_screen_geometry = QApplication.primaryScreen().geometry()
        local_screen_geometry = primary_screen_geometry.translated(-origin)
        center = local_screen_geometry.center()

        # Initialize and position the rubber band based on the translated coordinates
        self.rubber_band = QRubberBand(QRubberBand.Rectangle, self)
        self.rubber_band.setGeometry(
            QRect(center.x() - width // 2, center.y() - height // 2, width, height))
        self.rubber_band.show()

        self.dragging = False
        self.drag_position = QPoint()

    def mousePressEvent(self, event):
        event_position = event.position().toPoint()
        if self.rubber_band.geometry().contains(event_position):
            self.dragging = True
            self.drag_position = event_position - self.rubber_band.pos()
        else:
            if self.lastPosition:
                # Emit the last position in global screen coordinates
                self.positionSelected.emit(self.lastPosition.x(), self.lastPosition.y())
            self.main.show()
            self.hide()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.dragging:
            new_position = event.position().toPoint() - self.drag_position
            self.rubber_band.move(new_position)
            # Update the last position to reflect global screen coordinates
            self.lastPosition = self.rubber_band.geometry().topLeft() + self.pos()

    def mouseReleaseEvent(self, event):
        if self.dragging:
            # Finalize the last position in global screen coordinates
            self.lastPosition = self.rubber_band.geometry().topLeft() + self.pos()
            self.dragging = False

    def closeEvent(self, event):
        if self.lastPosition:
            # Emit the last position in global screen coordinates on close
            self.positionSelected.emit(self.lastPosition.x(), self.lastPosition.y())
        event.accept()

    def getLastPosition(self):
        # Return the last position in global screen coordinates
        return self.lastPosition

    def exec_(self):
        pass
