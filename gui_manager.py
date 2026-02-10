import sys
from gui.__init__ import *

class SpectralX(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        logs_window = QWidget(self)
        logs_window.move(10, 10)
        logs_window.setFixedSize(0, 0)
        logs_ui = Ui_logs()
        logs_ui.setupUi(logs_window)

        settings_window = QWidget(self)
        settings_window.move(10, 10)
        settings_window.setFixedSize(0, 0)
        settings_ui = Ui_settings()
        settings_ui.setupUi(settings_window)

if __name__ == "__main__":
    app = QApplication([])
    window = SpectralX()
    window.show()
    sys.exit(app.exec())