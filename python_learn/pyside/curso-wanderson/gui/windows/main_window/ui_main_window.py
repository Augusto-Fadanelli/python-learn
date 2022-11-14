# IMPORT QT CORE
from qt_core import *

class UIMainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282a36")

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)

