from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QFormLayout, QPushButton, QSizePolicy, \
    QSpacerItem
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt, Signal


class OverlayCard(QWidget):

    deleted = Signal(str)


    def __init__(self, overlayData, parent=None):
        super(OverlayCard, self).__init__(parent)

        self.overlayData = overlayData  # Store overlay data
        self.setMinimumSize(QSize(200, 300))
        self.setMaximumSize(QSize(200, 300))
        self.setupUi(overlayData)


    def setupUi(self, overlayData):
        # Main layout for the card
        vertical_layout = QVBoxLayout(self)
        vertical_layout.setSpacing(10)  # Decrease spacing if needed, or adjust as per your design
        vertical_layout.setContentsMargins(5, 5, 5, 5)  # Adjust margins if needed

        # Create and populate the image preview
        card_image_preview = QLabel(self)
        card_image_preview.setAlignment(Qt.AlignCenter)  # Center the image within the label
        card_image_preview.setPixmap(QPixmap(overlayData["imagePath"]).scaled(200, 150, Qt.KeepAspectRatio))
        vertical_layout.addWidget(card_image_preview)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vertical_layout.addItem(spacer)

        # Create and populate the details form
        card_details_frame = QFormLayout()
        card_details_frame.setRowWrapPolicy(QFormLayout.DontWrapRows)
        card_details_frame.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        card_details_frame.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
        card_details_frame.setLabelAlignment(Qt.AlignLeft)
        card_details_frame.setContentsMargins(0, 0, 0, 0)  # Minimize margins
        card_details_frame.setVerticalSpacing(5)  # Reduce vertical spacing between form rows

        # Overlay Name
        card_name_label = QLabel("Name:", self)
        card_name_input = QLineEdit(self)
        card_name_input.setText(overlayData["name"])
        card_name_input.setReadOnly(True)
        card_details_frame.addRow(card_name_label, card_name_input)

        # Overlay Hotkey
        card_hotkey_label = QLabel("Hotkey:", self)
        card_hotkey_input = QLineEdit(self)
        card_hotkey_input.setText(overlayData["hotkey"])
        card_hotkey_input.setReadOnly(True)
        card_details_frame.addRow(card_hotkey_label, card_hotkey_input)

        vertical_layout.addLayout(card_details_frame)

        # Delete button
        card_delete_button = QPushButton(QIcon(), "Delete", self)
        vertical_layout.addWidget(card_delete_button)
        card_delete_button.clicked.connect(self.onDelete)

        # Adjust spacing after the form before the delete button if needed
        vertical_layout.addSpacing(20)  # Adjust this value as per your design needs

    def onDelete(self):
        # Emit the deleted signal with an identifier, here we use 'name'
        self.deleted.emit(self.overlayData["name"])