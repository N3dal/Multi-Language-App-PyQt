#!/usr/bin/python3
# -----------------------------------------------------------------
#  simple sample to view multi language program;
#
#
#
# Author:N84.
#
# Create Date:Thu Jul 20 01:23:30 2023.
# ///
# ///
# ///
# -----------------------------------------------------------------


from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import uic
from sys import argv


class MainWindow(QMainWindow):
    """
        Docstring;
    """
    WIDTH = 844
    HEIGHT = 507
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        uic.loadUi("./UI.ui", self)
        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        
        self.language_selector_box = self.findChild(QComboBox, "language_selector_box")
        
        
def main():
    
    
    app = QApplication(argv)
    
    root = MainWindow()
    
    root.show()
    
    exit(app.exec())
    
    
if __name__ == "__main__":
    main()