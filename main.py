import sys
from PyQt5.QtWidgets import QApplication
from gui import GameOfLifeGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameOfLifeGUI()
    window.show()
    sys.exit(app.exec_())
