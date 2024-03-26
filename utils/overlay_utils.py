import ctypes


def set_click_through(window):
    hwnd = window.winId().__int__()
    GWL_EXSTYLE = -20
    WS_EX_LAYERED = 0x80000
    WS_EX_TRANSPARENT = 0x20
    ctypes.windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE,
                                           ctypes.windll.user32.GetWindowLongPtrW(hwnd,
                                                                                  GWL_EXSTYLE) | WS_EX_LAYERED | WS_EX_TRANSPARENT)


def toggleOverlay(overlayWindow):
    if overlayWindow.isVisible():
        overlayWindow.hide()
    else:
        overlayWindow.show()
