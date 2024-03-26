import os
import sys
import keyboard
import json
from PIL import Image
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QGraphicsOpacityEffect
from PySide6.QtGui import QPixmap, Qt, QMovie, QIcon
from PySide6.QtCore import Qt
from newoverlayui import Ui_MainWindow
from ui.overlay_window import OverlayWindow
from ui.dynamic_alignment_window import DynamicAlignmentWindow
from utils.icon_scaler import scale_icons
from utils.overlay_utils import set_click_through, toggleOverlay
from ui.overlay_card import OverlayCard
from utils.error_feedback_utils import FeedbackHandler


#######################################################################################################################


#######################################################################################################################


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.errorFeedbackAnimation = None
        self.errorFeedbackEffect = None
        self.selectedPosY = None
        self.selectedPosX = None
        self.overlay = None
        self.originalAspectRatio = None
        self.currentImagePath = None
        self.resizedImagePath = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.statusBar().setSizeGripEnabled(False)
        self.setWindowIcon(QIcon('resources/appicon.svg'))


        icons = [
            ('resources/heighticon.svg', self.ui.OriginalHeightIcon),
            ('resources/widthicon.svg', self.ui.OriginalWidthIcon),
            ('resources/fileicon.svg', self.ui.ChosenFileNameIcon),
            ('resources/moveicon.svg', self.ui.PositionIcon),
        ]

        for iconPath, labelWidget in icons:
            scaledPixmap = scale_icons(iconPath, 16, 16)
            labelWidget.setPixmap(scaledPixmap)

        # ChooseFileButton Initialization
        self.ui.ChooseFileButton.clicked.connect(self.openFileDialog)
        self.ui.ChooseFileButton.dragEnterEvent = self.dragEnterEvent
        self.ui.ChooseFileButton.dropEvent = self.dropEvent

        # OverlayAdjustmentExpandButton Toggle Frame
        self.ui.OverlayAdjustmentExpandButton.setProperty("expanded", False)
        initialIcon = QIcon(
            'resources/expandedicon.svg') if self.ui.AdjustmentsCollapsableFrame.isVisible() else QIcon(
            'resources/collapsedicon.svg')
        self.ui.OverlayAdjustmentExpandButton.setIcon(initialIcon)
        self.ui.OverlayAdjustmentExpandButton.style().unpolish(self.ui.OverlayAdjustmentExpandButton)
        self.ui.OverlayAdjustmentExpandButton.style().polish(self.ui.OverlayAdjustmentExpandButton)
        self.ui.OverlayAdjustmentExpandButton.clicked.connect(self.toggleAdjustmentsFrame)
        self.ui.AdjustmentsCollapsableFrame.setVisible(False)

        # Save Button
        self.ui.SaveButton.clicked.connect(self.saveOverlay)
        self.ui.DiscardButton.clicked.connect(self.discardOverlay)

        # Image Resizing
        self.ui.WidthInput.textChanged.connect(lambda: self.maintainAspectRatio('width'))
        self.ui.HeightInput.textChanged.connect(lambda: self.maintainAspectRatio('height'))
        self.ui.RatioCheckBox.setChecked(True)
        self.ui.ResizeButton.clicked.connect(self.onResizeButtonClick)

        # OverlayWindow
        self.overlayWindow = None
        self.overlays = {}
        self.loadOverlaysAndSetHotkeys()  # Load overlays and set hotkeys

        # Dynamic Alignment
        self.ui.DynamicAlignmentButton.clicked.connect(self.onDynamicAlignmentButtonClicked)

        # Error Feedback
        self.feedback_handler = FeedbackHandler(self.ui.ErrorFeedbackOutput)

    def onDynamicAlignmentButtonClicked(self):
        print("Entering onDynamicAlignmentButtonClicked")

        # Check if an image has been selected
        if not self.currentImagePath:
            # Display an error message if no image is selected
            self.feedback_handler.showErrorFeedback("Please choose an image before using dynamic alignment.")
            return

        # Proceed if an image is selected
        originalWidth = float(self.ui.OriginalWidthDisplay.text().replace(" px", ""))
        originalHeight = float(self.ui.OriginalHeightDisplay.text().replace(" px", ""))
        print(f"Original dimensions: Width={originalWidth}, Height={originalHeight}")

        self.overlay = DynamicAlignmentWindow(self, originalWidth, originalHeight)
        self.overlay.positionSelected.connect(self.onPositionSelected)
        self.overlay.show()

    def onPositionSelected(self, pos_x, pos_y):
        print(f"Entering onPositionSelected with pos_x={pos_x}, pos_y={pos_y}")
        self.selectedPosX = pos_x
        self.selectedPosY = pos_y

        self.ui.PositionLabel.setText(f"Position: {pos_x}, {pos_y}")

        if self.overlayWindow and self.overlayWindow.isVisible():
            print(f"Moving overlayWindow to pos_x={pos_x}, pos_y={pos_y}")
            self.overlayWindow.move(self.selectedPosX, self.selectedPosY)

    def openFileDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                  "Images (*.png *.xpm *.jpg *.gif);;All Files (*)")

        if fileName:
            self.displayImage(fileName)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            filePath = urls[0].toLocalFile()
            self.displayImage(filePath)

    def setPlaceholderImage(self):
        originalPixmap = QPixmap('resources/nofileselected.png')
        scaledPixmap = originalPixmap.scaled(self.ui.PreviewSpaceLabel.size(), Qt.KeepAspectRatio,
                                             Qt.SmoothTransformation)
        self.ui.PreviewSpaceLabel.setPixmap(scaledPixmap)

    def displayImage(self, imagePath):
        previewSize = self.ui.PreviewSpaceLabel.size()  # Get the size of the preview area
        self.ui.PreviewSpaceLabel.setAlignment(Qt.AlignCenter)  # Center the content

        if imagePath.lower().endswith('.gif'):
            movie = QMovie(imagePath)
            movie.jumpToFrame(0)  # Go to the first frame to get its size
            frameSize = movie.currentImage().size()  # Original frame size

            # Check if the original GIF size is smaller than the preview area
            # If it is, use the original size; otherwise, scale it down.
            if frameSize.width() <= previewSize.width() and frameSize.height() <= previewSize.height():
                scaledSize = frameSize
            else:
                scaledSize = frameSize.scaled(previewSize, Qt.KeepAspectRatio)

            movie.setScaledSize(scaledSize)
            self.ui.PreviewSpaceLabel.setMovie(movie)
            movie.start()

            # Set the original width and height display
            self.ui.OriginalWidthDisplay.setText(f"{frameSize.width()} px")
            self.ui.OriginalHeightDisplay.setText(f"{frameSize.height()} px")
        else:
            pixmap = QPixmap(imagePath)
            # Check if the original pixmap size is smaller than the preview area
            # If it is, use the original size; otherwise, scale it down.
            if pixmap.width() <= previewSize.width() and pixmap.height() <= previewSize.height():
                scaledPixmap = pixmap
            else:
                scaledPixmap = pixmap.scaled(previewSize, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.ui.PreviewSpaceLabel.setPixmap(scaledPixmap)

            # Set the original width and height display
            self.ui.OriginalWidthDisplay.setText(f"{pixmap.width()} px")
            self.ui.OriginalHeightDisplay.setText(f"{pixmap.height()} px")

        originalWidth = float(self.ui.OriginalWidthDisplay.text().replace(" px", ""))
        originalHeight = float(self.ui.OriginalHeightDisplay.text().replace(" px", ""))
        self.originalAspectRatio = originalWidth / originalHeight

        # Extract and display the file name
        fileName = os.path.basename(imagePath)
        self.ui.ChosenFileName.setText(fileName)

        self.currentImagePath = imagePath  # Store the image path

    def maintainAspectRatio(self, modified_dimension):
        if not self.ui.RatioCheckBox.isChecked():
            return

        try:
            if modified_dimension == 'width':
                new_width = int(self.ui.WidthInput.text())
                new_height = int(round(new_width / self.originalAspectRatio))
                self.ui.HeightInput.setText(str(new_height))
            elif modified_dimension == 'height':
                new_height = int(self.ui.HeightInput.text())
                new_width = int(round(new_height * self.originalAspectRatio))
                self.ui.WidthInput.setText(str(new_width))
        except ValueError:
            pass

    def resize_and_save_image(self, original_path, new_width, new_height):
        file_root, file_extension = os.path.splitext(original_path)

        new_path = f"{file_root}_resized{file_extension}"

        if file_extension.lower() == '.gif':
            with Image.open(original_path) as img:
                # Ensure the save_all parameter is set to maintain the GIF frames
                img.seek(0)  # Go to the first frame

                # Create a list to hold the resized frames
                new_frames = []

                while True:
                    # Extract the frame and work on its copy
                    frame = img.copy()

                    if frame.mode != 'RGBA':
                        frame = frame.convert('RGBA')

                    # Resize the frame
                    frame = frame.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    # Append the resized frame to the list of new frames
                    new_frames.append(frame)

                    # Try to move to the next frame
                    try:
                        img.seek(img.tell() + 1)
                    except EOFError:
                        break

                # Save the resized frames as a new GIF
                new_frames[0].save(new_path, save_all=True, append_images=new_frames[1:], optimize=False, loop=0,
                                   transparency=0, disposal=2)
        else:
            with Image.open(original_path) as img:
                new_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                new_img.save(new_path)

        self.resizedImagePath = new_path
        return new_path

    def needsResizing(self, new_width, new_height):
        # Load the current image to compare its dimensions
        with Image.open(self.currentImagePath) as img:
            original_width, original_height = img.size
            return (new_width, new_height) != (original_width, original_height)

    def onResizeButtonClick(self):
        new_width = self.ui.WidthInput.text().strip()
        new_height = self.ui.HeightInput.text().strip()
        imagePath = self.currentImagePath
        if not new_width or not new_height or not imagePath:
            self.feedback_handler.showErrorFeedback("Please fill out all fields: New Width, New Height and choose an "
                                                    "Image.")
            return
        # Retrieve new dimensions
        new_width_str = self.ui.WidthInput.text()
        new_height_str = self.ui.HeightInput.text()

        if new_width_str and new_height_str:
            new_width = int(new_width_str)
            new_height = int(new_height_str)

            # Resize the image only if necessary
            if self.needsResizing(new_width, new_height):
                resized_image_path = self.resize_and_save_image(self.currentImagePath, new_width, new_height)
                self.currentImagePath = resized_image_path

                # Extract and display the new filename
                fileName = os.path.basename(resized_image_path)
                self.ui.ChosenFileName.setText(fileName)

                # Extract and display the new dimensions
                self.ui.OriginalWidthDisplay.setText(f"{new_width} px")
                self.ui.OriginalHeightDisplay.setText(f"{new_height} px")

                # Update the preview with the resized image
                self.displayImage(resized_image_path)

    def saveOverlay(self):
        selectedPosX = getattr(self, 'selectedPosX', None)
        selectedPosY = getattr(self, 'selectedPosY', None)
        name = self.ui.OverlayNameInput.text().strip()
        hotkey = self.ui.OverlayHotkeyInput.text().strip()
        imagePath = self.currentImagePath

        missing_fields = []
        if not name:
            missing_fields.append("Name")
        if not hotkey:
            missing_fields.append("Hotkey")
        elif '+' not in hotkey and len(hotkey) > 1:
            self.feedback_handler.showErrorFeedback("Hotkey format is not supported. Please use '+' between keys (e.g., Ctrl+A).")
            return
        if not imagePath:
            missing_fields.append("Image")

        if missing_fields:
            missing_fields_string = ", ".join(missing_fields)
            message = f"Please fill out the following field{'s' if len(missing_fields) > 1 else ''}: {missing_fields_string}."
            self.feedback_handler.showErrorFeedback(message)
            return

        overlayData = {
            "name": name,
            "hotkey": hotkey,
            "imagePath": imagePath,
            "position": {'x': selectedPosX,
                         'y': selectedPosY} if selectedPosX is not None and selectedPosY is not None else {'x': None,
                                                                                                           'y': None}
        }

        print("Overlay data to be saved:", overlayData)

        # Load existing data
        try:
            with open("overlays.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        # Append new data
        data.append(overlayData)

        # Save updated data back to file
        with open("overlays.json", "w") as file:
            json.dump(data, file, indent=4)

        self.createAndDisplayOverlayCard(overlayData)

        print("Saving overlay data:", overlayData)
        self.createOverlay(overlayData["imagePath"], overlayData["hotkey"], overlayData["position"]['x'],
                           overlayData["position"]['y'])
        if self.overlayWindow and self.overlayWindow.isVisible():
            self.overlayWindow.move(self.selectedPosX, self.selectedPosY)

        QMessageBox.information(self, "Success", "Overlay saved successfully!")
        # Reset UI fields
        self.resetFields()

    def discardOverlay(self):
        self.resetFields()

    def resetFields(self):
        self.currentImagePath = None
        self.selectedPosX = None
        self.selectedPosY = None
        self.ui.OverlayNameInput.clear()
        self.ui.OverlayHotkeyInput.clear()
        self.ui.PreviewSpaceLabel.clear()
        self.ui.ChosenFileName.clear()
        self.ui.OriginalWidthDisplay.clear()
        self.ui.OriginalHeightDisplay.clear()
        self.setPlaceholderImage()
        self.ui.WidthInput.clear()
        self.ui.HeightInput.clear()
        self.ui.PositionLabel.clear()


    def toggleAdjustmentsFrame(self):
        isVisible = self.ui.AdjustmentsCollapsableFrame.isVisible()
        self.ui.AdjustmentsCollapsableFrame.setVisible(not isVisible)
        # Update the button's icon based on the new state
        if not isVisible:
            self.ui.OverlayAdjustmentExpandButton.setIcon(QIcon('resources/expandedicon.svg'))
        else:
            self.ui.OverlayAdjustmentExpandButton.setIcon(QIcon('resources/collapsedicon.svg'))

        self.ui.OverlayAdjustmentExpandButton.setProperty("expanded", not isVisible)
        self.ui.OverlayAdjustmentExpandButton.style().unpolish(self.ui.OverlayAdjustmentExpandButton)
        self.ui.OverlayAdjustmentExpandButton.style().polish(self.ui.OverlayAdjustmentExpandButton)

    def loadOverlaysAndSetHotkeys(self):
        try:
            with open("overlays.json", "r") as file:
                overlays = json.load(file)
                for overlay in overlays:
                    gif_path = overlay["imagePath"]
                    hotkey = overlay["hotkey"]
                    # Extract position if it exists, or default to None
                    pos_x = overlay.get("position", {}).get("x", None)
                    pos_y = overlay.get("position", {}).get("y", None)

                    # Pass the position to createOverlay
                    self.createOverlay(gif_path, hotkey, pos_x, pos_y)

                    self.createAndDisplayOverlayCard(overlay)

        except FileNotFoundError:
            print("Overlays file not found.")
        except Exception as e:
            print(f"Failed to load overlays: {e}")


    def createAndDisplayOverlayCard(self, overlayData):
        new_card = OverlayCard(overlayData, self.ui.scrollArea.widget())
        new_card.deleted.connect(self.deleteOverlay)

        # Determine the position for a new card within the grid
        layout = self.ui.scrollArea.widget().layout()
        position = layout.count()
        max_col = 2
        row = position // (max_col + 1)
        col = position % (max_col + 1)

        layout.addWidget(new_card, row, col)

    def deleteOverlay(self, overlayName):
        reply = QMessageBox.question(self, 'Confirm Deletion',
                                     f"Are you sure you want to delete the overlay '{overlayName}'?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            with open("overlays.json", "r") as file:
                overlays = json.load(file)

            overlayToDelete = next((overlay for overlay in overlays if overlay.get('name') == overlayName), None)
            if overlayToDelete:
                hotkey = overlayToDelete.get('hotkey')

                # Check if the hotkey is linked with an overlay and remove it
                if hotkey in self.overlays:
                    # Close and delete the overlay window
                    self.overlays[hotkey].close()
                    del self.overlays[hotkey]

                    # Remove hotkey binding
                    keyboard.remove_hotkey(hotkey)

                # Remove the overlay's data and update the JSON file
                overlays = [overlay for overlay in overlays if overlay.get('name') != overlayName]
                with open("overlays.json", "w") as file:
                    json.dump(overlays, file, indent=4)

                self.refreshUI()

    def refreshUI(self):
        layout = self.ui.scrollArea.widget().layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.loadOverlaysAndSetHotkeys()

    def createOverlay(self, gif_path, hotkey, pos_x=None, pos_y=None):
        print(f"Creating/Updating overlay: hotkey={hotkey}, pos_x={pos_x}, pos_y={pos_y}")
        if hotkey in self.overlays:
            overlayWindow = self.overlays[hotkey]
            if pos_x is not None and pos_y is not None:
                print(f"Moving existing overlay to pos_x={pos_x}, pos_y={pos_y}")
                overlayWindow.move(pos_x, pos_y)
        else:
            print("Creating new overlay window.")
            # If the overlay does not exist, create a new one.
            overlayWindow = OverlayWindow(gif_path, pos_x, pos_y)
            set_click_through(overlayWindow)
            self.overlays[hotkey] = overlayWindow  # Store the overlay window with its hotkey
            keyboard.add_hotkey(hotkey, lambda: toggleOverlay(overlayWindow))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("styles.qss", "r") as file:
        qss = file.read()
        app.setStyleSheet(qss)
    window = MainWindow()
    window.show()
    window.setPlaceholderImage()

    sys.exit(app.exec())
