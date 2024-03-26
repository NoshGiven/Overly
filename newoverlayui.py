# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FinalOverlayAppui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 900)
        MainWindow.setMinimumSize(QSize(900, 900))
        MainWindow.setMaximumSize(QSize(900, 900))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.NewOverlayTab = QWidget()
        self.NewOverlayTab.setObjectName(u"NewOverlayTab")
        self.gridLayout = QGridLayout(self.NewOverlayTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.NewOverlayTabWidget = QWidget(self.NewOverlayTab)
        self.NewOverlayTabWidget.setObjectName(u"NewOverlayTabWidget")
        self.gridLayout_3 = QGridLayout(self.NewOverlayTabWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.NewOverlayDetailsWidget = QWidget(self.NewOverlayTabWidget)
        self.NewOverlayDetailsWidget.setObjectName(u"NewOverlayDetailsWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewOverlayDetailsWidget.sizePolicy().hasHeightForWidth())
        self.NewOverlayDetailsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.NewOverlayDetailsWidget)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.OverlayDetailsFrame = QFrame(self.NewOverlayDetailsWidget)
        self.OverlayDetailsFrame.setObjectName(u"OverlayDetailsFrame")
        self.OverlayDetailsFrame.setFrameShape(QFrame.StyledPanel)
        self.OverlayDetailsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.OverlayDetailsFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.OverlayNameLabel = QLabel(self.OverlayDetailsFrame)
        self.OverlayNameLabel.setObjectName(u"OverlayNameLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.OverlayNameLabel.sizePolicy().hasHeightForWidth())
        self.OverlayNameLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.OverlayNameLabel)

        self.OverlayNameInput = QLineEdit(self.OverlayDetailsFrame)
        self.OverlayNameInput.setObjectName(u"OverlayNameInput")

        self.verticalLayout_5.addWidget(self.OverlayNameInput)

        self.OverlayHotkeyLabel = QLabel(self.OverlayDetailsFrame)
        self.OverlayHotkeyLabel.setObjectName(u"OverlayHotkeyLabel")
        sizePolicy1.setHeightForWidth(self.OverlayHotkeyLabel.sizePolicy().hasHeightForWidth())
        self.OverlayHotkeyLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.OverlayHotkeyLabel)

        self.OverlayHotkeyInput = QLineEdit(self.OverlayDetailsFrame)
        self.OverlayHotkeyInput.setObjectName(u"OverlayHotkeyInput")

        self.verticalLayout_5.addWidget(self.OverlayHotkeyInput)


        self.verticalLayout_2.addWidget(self.OverlayDetailsFrame)

        self.FileSelectionDetailsFrame = QFrame(self.NewOverlayDetailsWidget)
        self.FileSelectionDetailsFrame.setObjectName(u"FileSelectionDetailsFrame")
        self.FileSelectionDetailsFrame.setFrameShape(QFrame.StyledPanel)
        self.FileSelectionDetailsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.FileSelectionDetailsFrame)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ChooseFileButton = QPushButton(self.FileSelectionDetailsFrame)
        self.ChooseFileButton.setObjectName(u"ChooseFileButton")
        self.ChooseFileButton.setAcceptDrops(True)

        self.verticalLayout_6.addWidget(self.ChooseFileButton)

        self.OriginalWidthHeightForm = QFormLayout()
        self.OriginalWidthHeightForm.setObjectName(u"OriginalWidthHeightForm")
        self.OriginalWidthDisplay = QLineEdit(self.FileSelectionDetailsFrame)
        self.OriginalWidthDisplay.setObjectName(u"OriginalWidthDisplay")
        self.OriginalWidthDisplay.setReadOnly(True)

        self.OriginalWidthHeightForm.setWidget(1, QFormLayout.FieldRole, self.OriginalWidthDisplay)

        self.OriginalHeightDisplay = QLineEdit(self.FileSelectionDetailsFrame)
        self.OriginalHeightDisplay.setObjectName(u"OriginalHeightDisplay")
        self.OriginalHeightDisplay.setReadOnly(True)

        self.OriginalWidthHeightForm.setWidget(2, QFormLayout.FieldRole, self.OriginalHeightDisplay)

        self.ChosenFileName = QLineEdit(self.FileSelectionDetailsFrame)
        self.ChosenFileName.setObjectName(u"ChosenFileName")
        self.ChosenFileName.setReadOnly(True)

        self.OriginalWidthHeightForm.setWidget(0, QFormLayout.FieldRole, self.ChosenFileName)

        self.ChosenFileNameIcon = QLabel(self.FileSelectionDetailsFrame)
        self.ChosenFileNameIcon.setObjectName(u"ChosenFileNameIcon")

        self.OriginalWidthHeightForm.setWidget(0, QFormLayout.LabelRole, self.ChosenFileNameIcon)

        self.OriginalWidthIcon = QLabel(self.FileSelectionDetailsFrame)
        self.OriginalWidthIcon.setObjectName(u"OriginalWidthIcon")

        self.OriginalWidthHeightForm.setWidget(1, QFormLayout.LabelRole, self.OriginalWidthIcon)

        self.OriginalHeightIcon = QLabel(self.FileSelectionDetailsFrame)
        self.OriginalHeightIcon.setObjectName(u"OriginalHeightIcon")

        self.OriginalWidthHeightForm.setWidget(2, QFormLayout.LabelRole, self.OriginalHeightIcon)


        self.verticalLayout_6.addLayout(self.OriginalWidthHeightForm)


        self.verticalLayout_2.addWidget(self.FileSelectionDetailsFrame)

        self.OverlayAdjustmentsFrame = QFrame(self.NewOverlayDetailsWidget)
        self.OverlayAdjustmentsFrame.setObjectName(u"OverlayAdjustmentsFrame")
        self.OverlayAdjustmentsFrame.setEnabled(True)
        self.OverlayAdjustmentsFrame.setFrameShape(QFrame.StyledPanel)
        self.OverlayAdjustmentsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.OverlayAdjustmentsFrame)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.OverlayAdjustmentExpandButton = QPushButton(self.OverlayAdjustmentsFrame)
        self.OverlayAdjustmentExpandButton.setObjectName(u"OverlayAdjustmentExpandButton")

        self.verticalLayout_3.addWidget(self.OverlayAdjustmentExpandButton)

        self.AdjustmentsCollapsableFrame = QFrame(self.OverlayAdjustmentsFrame)
        self.AdjustmentsCollapsableFrame.setObjectName(u"AdjustmentsCollapsableFrame")
        self.AdjustmentsCollapsableFrame.setFrameShape(QFrame.StyledPanel)
        self.AdjustmentsCollapsableFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.AdjustmentsCollapsableFrame)
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ResizeOverlayFormLayout = QFormLayout()
        self.ResizeOverlayFormLayout.setObjectName(u"ResizeOverlayFormLayout")
        self.WidthLabel = QLabel(self.AdjustmentsCollapsableFrame)
        self.WidthLabel.setObjectName(u"WidthLabel")

        self.ResizeOverlayFormLayout.setWidget(2, QFormLayout.LabelRole, self.WidthLabel)

        self.WidthInput = QLineEdit(self.AdjustmentsCollapsableFrame)
        self.WidthInput.setObjectName(u"WidthInput")

        self.ResizeOverlayFormLayout.setWidget(2, QFormLayout.FieldRole, self.WidthInput)

        self.HeightLabel = QLabel(self.AdjustmentsCollapsableFrame)
        self.HeightLabel.setObjectName(u"HeightLabel")

        self.ResizeOverlayFormLayout.setWidget(3, QFormLayout.LabelRole, self.HeightLabel)

        self.HeightInput = QLineEdit(self.AdjustmentsCollapsableFrame)
        self.HeightInput.setObjectName(u"HeightInput")

        self.ResizeOverlayFormLayout.setWidget(3, QFormLayout.FieldRole, self.HeightInput)

        self.RatioLabel = QLabel(self.AdjustmentsCollapsableFrame)
        self.RatioLabel.setObjectName(u"RatioLabel")

        self.ResizeOverlayFormLayout.setWidget(4, QFormLayout.LabelRole, self.RatioLabel)

        self.RatioCheckBox = QCheckBox(self.AdjustmentsCollapsableFrame)
        self.RatioCheckBox.setObjectName(u"RatioCheckBox")

        self.ResizeOverlayFormLayout.setWidget(4, QFormLayout.FieldRole, self.RatioCheckBox)


        self.verticalLayout_7.addLayout(self.ResizeOverlayFormLayout)

        self.ResizeButton = QPushButton(self.AdjustmentsCollapsableFrame)
        self.ResizeButton.setObjectName(u"ResizeButton")

        self.verticalLayout_7.addWidget(self.ResizeButton)

        self.DynamicAlignmentButton = QPushButton(self.AdjustmentsCollapsableFrame)
        self.DynamicAlignmentButton.setObjectName(u"DynamicAlignmentButton")

        self.verticalLayout_7.addWidget(self.DynamicAlignmentButton)

        self.DynamicPositionFormLayout = QFormLayout()
        self.DynamicPositionFormLayout.setObjectName(u"DynamicPositionFormLayout")
        self.PositionLabel = QLineEdit(self.AdjustmentsCollapsableFrame)
        self.PositionLabel.setObjectName(u"PositionLabel")
        self.PositionLabel.setReadOnly(True)

        self.DynamicPositionFormLayout.setWidget(0, QFormLayout.FieldRole, self.PositionLabel)

        self.PositionIcon = QLabel(self.AdjustmentsCollapsableFrame)
        self.PositionIcon.setObjectName(u"PositionIcon")

        self.DynamicPositionFormLayout.setWidget(0, QFormLayout.LabelRole, self.PositionIcon)


        self.verticalLayout_7.addLayout(self.DynamicPositionFormLayout)


        self.verticalLayout_3.addWidget(self.AdjustmentsCollapsableFrame)


        self.verticalLayout_2.addWidget(self.OverlayAdjustmentsFrame)

        self.SaveDiscardFrame = QFrame(self.NewOverlayDetailsWidget)
        self.SaveDiscardFrame.setObjectName(u"SaveDiscardFrame")
        self.SaveDiscardFrame.setFrameShape(QFrame.StyledPanel)
        self.SaveDiscardFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.SaveDiscardFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.SaveButton = QPushButton(self.SaveDiscardFrame)
        self.SaveButton.setObjectName(u"SaveButton")

        self.verticalLayout_4.addWidget(self.SaveButton)

        self.DiscardButton = QPushButton(self.SaveDiscardFrame)
        self.DiscardButton.setObjectName(u"DiscardButton")

        self.verticalLayout_4.addWidget(self.DiscardButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.SaveDiscardFrame)


        self.gridLayout_3.addWidget(self.NewOverlayDetailsWidget, 0, 0, 1, 1)

        self.PVSpaceFeedbacklayout = QVBoxLayout()
        self.PVSpaceFeedbacklayout.setObjectName(u"PVSpaceFeedbacklayout")
        self.PreviewSpaceWidget = QWidget(self.NewOverlayTabWidget)
        self.PreviewSpaceWidget.setObjectName(u"PreviewSpaceWidget")
        self.gridLayout_2 = QGridLayout(self.PreviewSpaceWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.PreviewSpaceLabel = QLabel(self.PreviewSpaceWidget)
        self.PreviewSpaceLabel.setObjectName(u"PreviewSpaceLabel")
        self.PreviewSpaceLabel.setScaledContents(False)

        self.gridLayout_2.addWidget(self.PreviewSpaceLabel, 1, 0, 1, 1)

        self.ErrorFeedbackOutput = QLabel(self.PreviewSpaceWidget)
        self.ErrorFeedbackOutput.setObjectName(u"ErrorFeedbackOutput")
        sizePolicy1.setHeightForWidth(self.ErrorFeedbackOutput.sizePolicy().hasHeightForWidth())
        self.ErrorFeedbackOutput.setSizePolicy(sizePolicy1)
        self.ErrorFeedbackOutput.setMinimumSize(QSize(0, 35))
        self.ErrorFeedbackOutput.setMaximumSize(QSize(16777215, 20))
        self.ErrorFeedbackOutput.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ErrorFeedbackOutput, 0, 0, 1, 1)


        self.PVSpaceFeedbacklayout.addWidget(self.PreviewSpaceWidget)


        self.gridLayout_3.addLayout(self.PVSpaceFeedbacklayout, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.NewOverlayTabWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.NewOverlayTab, "")
        self.MyOverlays = QWidget()
        self.MyOverlays.setObjectName(u"MyOverlays")
        self.gridLayout_5 = QGridLayout(self.MyOverlays)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.SavedOverlaysWidget = QWidget(self.MyOverlays)
        self.SavedOverlaysWidget.setObjectName(u"SavedOverlaysWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SavedOverlaysWidget.sizePolicy().hasHeightForWidth())
        self.SavedOverlaysWidget.setSizePolicy(sizePolicy2)
        self.gridLayout_6 = QGridLayout(self.SavedOverlaysWidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea = QScrollArea(self.SavedOverlaysWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 838, 818))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_6.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.SavedOverlaysWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.MyOverlays, "")
        self.AboutTab = QWidget()
        self.AboutTab.setObjectName(u"AboutTab")
        self.gridLayout_4 = QGridLayout(self.AboutTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AboutOverlyFrame = QFrame(self.AboutTab)
        self.AboutOverlyFrame.setObjectName(u"AboutOverlyFrame")
        self.AboutOverlyFrame.setFrameShape(QFrame.StyledPanel)
        self.AboutOverlyFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.AboutOverlyFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.AboutOverlyLabel = QLabel(self.AboutOverlyFrame)
        self.AboutOverlyLabel.setObjectName(u"AboutOverlyLabel")
        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        self.AboutOverlyLabel.setFont(font)
        self.AboutOverlyLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.AboutOverlyLabel.setWordWrap(True)

        self.gridLayout_7.addWidget(self.AboutOverlyLabel, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.AboutOverlyFrame)

        self.UsingOverlyFrame = QFrame(self.AboutTab)
        self.UsingOverlyFrame.setObjectName(u"UsingOverlyFrame")
        self.UsingOverlyFrame.setFrameShape(QFrame.StyledPanel)
        self.UsingOverlyFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.UsingOverlyFrame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.UsingOverlyLabel = QLabel(self.UsingOverlyFrame)
        self.UsingOverlyLabel.setObjectName(u"UsingOverlyLabel")
        self.UsingOverlyLabel.setFont(font)
        self.UsingOverlyLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.UsingOverlyLabel.setWordWrap(True)

        self.gridLayout_9.addWidget(self.UsingOverlyLabel, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.UsingOverlyFrame)


        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout_4.setRowStretch(0, 2)
        self.tabWidget.addTab(self.AboutTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Overly", None))
        self.OverlayNameLabel.setText(QCoreApplication.translate("MainWindow", u"Overlay Name", None))
        self.OverlayHotkeyLabel.setText(QCoreApplication.translate("MainWindow", u"Overlay Hotkey", None))
        self.ChooseFileButton.setText(QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.OriginalWidthDisplay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No File Selected", None))
        self.OriginalHeightDisplay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No File Selected", None))
        self.ChosenFileName.setText("")
        self.ChosenFileName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No File Selected", None))
        self.ChosenFileNameIcon.setText("")
        self.OriginalWidthIcon.setText("")
        self.OriginalHeightIcon.setText("")
        self.OverlayAdjustmentExpandButton.setText(QCoreApplication.translate("MainWindow", u"   Overlay Adjustments", None))
        self.WidthLabel.setText(QCoreApplication.translate("MainWindow", u"New Width", None))
        self.HeightLabel.setText(QCoreApplication.translate("MainWindow", u"New Height", None))
        self.RatioLabel.setText(QCoreApplication.translate("MainWindow", u"Maintain Ratio", None))
        self.RatioCheckBox.setText("")
        self.ResizeButton.setText(QCoreApplication.translate("MainWindow", u"Resize", None))
        self.DynamicAlignmentButton.setText(QCoreApplication.translate("MainWindow", u"Dynamic Alignment ", None))
        self.PositionIcon.setText("")
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.DiscardButton.setText(QCoreApplication.translate("MainWindow", u"Discard", None))
        self.PreviewSpaceLabel.setText("")
        self.ErrorFeedbackOutput.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NewOverlayTab), QCoreApplication.translate("MainWindow", u"New Overlay", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MyOverlays), QCoreApplication.translate("MainWindow", u"My Overlays", None))
        self.AboutOverlyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#55aaff;\">Using Overly</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">To start creating your overlay with Overly, follow these simple steps:</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#55aaff;\">Overlay Name:</span><span style=\" font-size:12pt; color:#55aaff;\"/><span style=\" font-size:12pt; color:#ffffff;\">Begin by entering a unique name for your overlay. This name will help you identify it later among other overlays you may create.</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#55aaff;\">Hotkey Assignment:</span><span style=\" font-size:12pt; color:#55aaff;\"/><span style=\" font-size:12pt; color:#ffffff;\">Assign a hotkey to your overlay. This is the keyboard shortcut that will toggle the visibility of your overlay on your screen. Remember, the hotkey should include a combination of keys separated by a plus sign (e.g., Ctrl+Shift+O, not CtrlShiftO). Sing"
                        "le characters or numbers without a plus sign are not accepted as valid hotkeys.</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#55aaff;\">Choose an Image or GIF:</span><span style=\" font-size:12pt; color:#55aaff;\"/><span style=\" font-size:12pt; color:#ffffff;\">Select an image or GIF for your overlay. This will be the content displayed when your overlay is active. You can choose files from your computer that best fit the purpose of your overlay.</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#55aaff;\">Resize (Optional):</span><span style=\" font-size:12pt; color:#55aaff;\"/><span style=\" font-size:12pt; color:#ffffff;\">Once you've selected an image or GIF, you have the option to resize it.This allows you to ensure that the overlay fits well within your screen space without overwhelming your workspace or being too small to see.</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#55aaff;\">Positioning Your Overlay (Optional): </span><span style=\" fon"
                        "t-size:12pt; color:#ffffff;\">By using Dynamic Alignment button, you can place your overlay precisely where you want it on your screen. You can drag the overlay to your desired location, ensuring it does not obstruct important information or interfere with your workflow.</span></p><p><span style=\" font-size:12pt; font-weight:600; color:#55aaff;\">Save or Discard:</span><span style=\" font-size:12pt; color:#55aaff;\"/><span style=\" font-size:12pt; color:#ffffff;\">After setting up your overlay, you can choose to save your settings, making the overlay ready to use, or discard them if you're not satisfied with the setup. Saved overlays can be toggled using their assigned hotkeys, allowing for quick access to their content. When saved, overlays will appear in My Overlays tab.</span></p></body></html>", None))
        self.UsingOverlyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#55aaff;\">Overly</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">Version: 1.0.0 </span></p><p><span style=\" font-size:12pt; color:#ffffff;\"><br/>&quot;Overly&quot; is a Windows desktop application designed to allows users to create overlays on their screen, providing quick access to information, tools, or any other content they wish to keep handy while working on other tasks.</span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AboutTab), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

