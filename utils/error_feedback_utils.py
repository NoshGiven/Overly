from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtWidgets import QGraphicsOpacityEffect


class FeedbackHandler:
    def __init__(self, feedback_output):
        self.errorFeedbackAnimation = None
        self.errorFeedbackEffect = None
        self.feedback_output = feedback_output
        self.setupErrorFeedbackAnimation()

    def setupErrorFeedbackAnimation(self):
        # Set up the opacity effect
        self.errorFeedbackEffect = QGraphicsOpacityEffect(self.feedback_output)
        self.feedback_output.setGraphicsEffect(self.errorFeedbackEffect)

        # Set up the animation
        self.errorFeedbackAnimation = QPropertyAnimation(self.errorFeedbackEffect, b"opacity")
        self.errorFeedbackAnimation.setDuration(3000)
        self.errorFeedbackAnimation.setStartValue(1.0)
        self.errorFeedbackAnimation.setEndValue(0.0)
        self.errorFeedbackAnimation.setEasingCurve(QEasingCurve.InOutQuad)

    def showErrorFeedback(self, message):
        # Check if the message is different from the current one
        if self.feedback_output.text() != message:
            # Set the error message
            self.feedback_output.setText(message)

            # Apply CSS class for styling
            self.feedback_output.setProperty("class", "ErrorFeedback")
            self.feedback_output.style().unpolish(self.feedback_output)
            self.feedback_output.style().polish(self.feedback_output)

            # Apply the graphics effect for future opacity animation
            self.feedback_output.setGraphicsEffect(self.errorFeedbackEffect)

            # Reset opacity to full and stop any ongoing animation
            self.errorFeedbackEffect.setOpacity(1.0)
            self.errorFeedbackAnimation.stop()

            QTimer.singleShot(3000, self.errorFeedbackAnimation.start)

        self.errorFeedbackAnimation.finished.connect(self.clearErrorFeedback)

    def clearErrorFeedback(self):
        self.feedback_output.clear()
