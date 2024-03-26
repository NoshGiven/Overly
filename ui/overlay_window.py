from PySide6 import QtWidgets, QtCore, QtGui


class OverlayWindow(QtWidgets.QWidget):
    def __init__(self, gif_path, pos_x=None, pos_y=None):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)
        self.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)

        self.label = QtWidgets.QLabel(self)

        if gif_path.lower().endswith('.gif'):
            # Handle GIF images using QMovie
            movie = QtGui.QMovie(gif_path)
            self.label.setMovie(movie)
            movie.start()
            self.resize(movie.frameRect().size())
        else:
            # Handle static images using QPixmap
            pixmap = QtGui.QPixmap(gif_path)
            self.label.setPixmap(pixmap)
            self.resize(pixmap.size())

        # Decide whether to center or use the specified position
        if pos_x is not None and pos_y is not None:
            self.move(pos_x, pos_y)
        else:
            self.center_on_screen()

    def center_on_screen(self):
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
