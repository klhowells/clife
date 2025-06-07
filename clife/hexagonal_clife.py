import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QSlider, QLabel, QHBoxLayout, QComboBox, QScrollArea
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import QPoint, Qt, QTimer
from hexagonal_grid import HexagonalGridLogic

class HexagonalGrid(QWidget):
    def __init__(self, rows, cols, hex_size):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.hex_size = hex_size
        self.grid = {}  # Updated to use dictionary-based grid
        self.setFixedSize(int(cols * hex_size * 1.5), int(rows * hex_size * 1.732))

    def paintEvent(self, event):
        painter = QPainter(self)
        for (row, col), cell in self.grid.items():
            x_offset = col * self.hex_size * 1.5
            y_offset = row * self.hex_size * 1.732
            if col % 2 == 1:
                y_offset += self.hex_size * 0.866
            hexagon = self.create_hexagon(x_offset, y_offset)
            color = QColor("lightgreen") if cell['state'] == 1 else QColor("white")
            painter.setBrush(color)
            painter.drawPolygon(hexagon)

    def create_hexagon(self, x, y):
        size = self.hex_size
        return QPolygon([QPoint(int(x + size * 0.5), int(y)),
                         QPoint(int(x + size * 1.5), int(y)),
                         QPoint(int(x + size * 2), int(y + size * 0.866)),
                         QPoint(int(x + size * 1.5), int(y + size * 1.732)),
                         QPoint(int(x + size * 0.5), int(y + size * 1.732)),
                         QPoint(int(x), int(y + size * 0.866))])

    def mousePressEvent(self, event):
        self.handle_mouse_event(event)

    def mouseMoveEvent(self, event):
        self.handle_mouse_event(event)

    def handle_mouse_event(self, event):
        if event.buttons() & Qt.LeftButton:
            x = event.x()
            y = event.y()
            col = int(x // (self.hex_size * 1.5))
            row = int((y - (self.hex_size * 0.866 if col % 2 == 1 else 0)) // (self.hex_size * 1.732))
            if (row, col) in self.grid:
                self.grid[(row, col)]['state'] = 1 - self.grid[(row, col)]['state']
                self.update()

class HexagonalClife(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hexagonal Conway's Game of Life")
        self.resize(800, 600)  # Make the window resizable

        hex_size = 8  # Adjusted hexagon size to fit 80x80 grid
        self.grid_widget = HexagonalGrid(80, 80, hex_size)
        self.grid_logic = HexagonalGridLogic(80, 80)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)
        self.timer.setSingleShot(False)

        layout = QVBoxLayout()
        controls_layout_top = QHBoxLayout()
        controls_layout_bottom = QHBoxLayout()
        exit_layout = QHBoxLayout()
        layout.addLayout(controls_layout_top)
        layout.addLayout(controls_layout_bottom)

        # --- Top row controls ---
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_game)
        controls_layout_top.addWidget(start_button)

        stop_button = QPushButton("Stop")
        stop_button.clicked.connect(self.stop_game)
        controls_layout_top.addWidget(stop_button)

        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset_game)
        controls_layout_top.addWidget(reset_button)

        random_button = QPushButton("Random")
        random_button.clicked.connect(self.randomize_grid)
        controls_layout_top.addWidget(random_button)

        controls_layout_top.addWidget(QLabel("Random %"))
        self.random_slider = QSlider(Qt.Horizontal)
        self.random_slider.setRange(1, 100)
        self.random_slider.setValue(30)
        self.random_slider.setFixedWidth(100)
        controls_layout_top.addWidget(self.random_slider)

        # --- Bottom row controls ---
        label_surv_min = QLabel("Survival Min")
        label_surv_min.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        controls_layout_bottom.addWidget(label_surv_min)
        self.survival_min_dropdown = QComboBox()
        self.survival_min_dropdown.addItems([str(i) for i in range(1, 7)])
        self.survival_min_dropdown.setCurrentText("1")
        controls_layout_bottom.addWidget(self.survival_min_dropdown)

        label_surv_max = QLabel("Survival Max")
        label_surv_max.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        controls_layout_bottom.addWidget(label_surv_max)
        self.survival_max_dropdown = QComboBox()
        self.survival_max_dropdown.addItems([str(i) for i in range(1, 7)])
        self.survival_max_dropdown.setCurrentText("3")
        controls_layout_bottom.addWidget(self.survival_max_dropdown)

        label_birth_min = QLabel("Birth Min")
        label_birth_min.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        controls_layout_bottom.addWidget(label_birth_min)
        self.birth_min_dropdown = QComboBox()
        self.birth_min_dropdown.addItems([str(i) for i in range(1, 7)])
        self.birth_min_dropdown.setCurrentText("2")
        controls_layout_bottom.addWidget(self.birth_min_dropdown)

        label_birth_max = QLabel("Birth Max")
        label_birth_max.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        controls_layout_bottom.addWidget(label_birth_max)
        self.birth_max_dropdown = QComboBox()
        self.birth_max_dropdown.addItems([str(i) for i in range(1, 7)])
        self.birth_max_dropdown.setCurrentText("4")
        controls_layout_bottom.addWidget(self.birth_max_dropdown)

        label_speed = QLabel("Speed (ms)")
        label_speed.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        controls_layout_bottom.addWidget(label_speed)
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 1000)
        self.speed_slider.setValue(100)
        self.speed_slider.valueChanged.connect(self.update_timer_interval)
        self.speed_slider.setFixedWidth(100)
        controls_layout_bottom.addWidget(self.speed_slider)

        # --- Exit button at bottom right ---
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        exit_layout.addStretch()  # Pushes the button to the right
        exit_layout.addWidget(exit_button)
        layout.addLayout(exit_layout)

        scroll_area = QScrollArea()  # Add a scroll area
        scroll_area.setWidget(self.grid_widget)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_game(self):
        self.timer.start(self.speed_slider.value())  # Ensure timer starts with the correct interval
        self.grid_widget.grid = self.grid_logic.grid  # Sync GUI grid with logic grid

    def stop_game(self):
        self.timer.stop()  # Stop simulation

    def update_simulation(self):
        # Pass the current survival and birth parameters to the logic
        survival_min = int(self.survival_min_dropdown.currentText())
        survival_max = int(self.survival_max_dropdown.currentText())
        birth_min = int(self.birth_min_dropdown.currentText())
        birth_max = int(self.birth_max_dropdown.currentText())

        self.grid_logic.get_next_state(survival_min, survival_max, birth_min, birth_max)
        self.grid_widget.grid = self.grid_logic.grid  # Sync GUI grid with logic grid
        self.grid_widget.update()

    def reset_game(self):
        self.grid_logic.reset()
        self.grid_widget.grid = self.grid_logic.grid  # Sync GUI grid with logic grid
        self.grid_widget.update()

    def randomize_grid(self):
        percentage = self.random_slider.value()
        self.grid_logic.randomize(percentage)
        self.grid_widget.grid = self.grid_logic.grid  # Sync GUI grid with logic grid
        self.grid_widget.update()

    def update_timer_interval(self):
        self.timer.setInterval(self.speed_slider.value())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HexagonalClife()
    window.show()
    sys.exit(app.exec_())
