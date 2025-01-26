import sys
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from gui import Ui_Form  # Import the generated class

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Setup the UI from the generated class
        self.setWindowIcon(QIcon("time.ico"))

        # Setup a timer to update the time
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        date = datetime.datetime.now()
        self.heu.display(int(date.strftime("%H")))  # Assuming 'heu' is a display element
        self.min.display(int(date.strftime("%M")))  # Assuming 'min' is a display element
        self.sec.display(int(date.strftime("%S")))  # Assuming 'sec' is a display element

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
