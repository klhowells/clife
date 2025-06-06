import sys
from PyQt5.QtWidgets import QApplication
from hexagonal_clife import HexagonalClife

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HexagonalClife()
    window.show()
    sys.exit(app.exec_())
