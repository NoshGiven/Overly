from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt


def scale_icons(icon_path, target_width, target_height):
    """
    Scale an icon to the specified width and height while maintaining its aspect ratio.

    :param icon_path: Path to the icon file.
    :param target_width: Desired width of the icon.
    :param target_height: Desired height of the icon.
    :return: Scaled QPixmap object.
    """
    pixmap = QPixmap(icon_path)
    return pixmap.scaled(QSize(target_width, target_height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
