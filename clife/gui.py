from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QLabel, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter
from grid import Grid

class GameOfLifeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conway's Game of Life")
        self.setGeometry(100, 100, 800, 800)

        self.grid_size = 80  # Number of cells in each dimension
        self.cell_size = 10
        self.grid = Grid(self.grid_size, self.grid_size)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.grid_widget = GridWidget(self.grid, self.cell_size)
        layout.addWidget(self.grid_widget)

        controls_layout = QHBoxLayout()
        layout.addLayout(controls_layout)

        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_game)
        controls_layout.addWidget(start_button)

        stop_button = QPushButton("Stop")
        stop_button.clicked.connect(self.stop_game)
        controls_layout.addWidget(stop_button)

        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset_game)
        controls_layout.addWidget(reset_button)

        random_button = QPushButton("Random")
        random_button.clicked.connect(self.randomize_grid)
        controls_layout.addWidget(random_button)

        self.random_slider = QSlider(Qt.Horizontal)
        self.random_slider.setRange(0, 100)
        self.random_slider.setValue(30)
        controls_layout.addWidget(QLabel("Random %"))
        controls_layout.addWidget(self.random_slider)

        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(0, 1000)  # Speed in milliseconds
        self.speed_slider.setValue(100)  # Default speed is 100ms
        self.speed_slider.valueChanged.connect(self.update_timer_interval)
        controls_layout.addWidget(QLabel("Speed (ms)"))
        controls_layout.addWidget(self.speed_slider)

    def start_game(self):
        self.timer.start(100)  # Update every 100ms

    def stop_game(self):
        self.timer.stop()

    def update_simulation(self):
        self.grid.get_next_state()
        self.grid_widget.update()

    def reset_game(self):
        self.grid.reset()
        self.grid_widget.update()

    def randomize_grid(self):
        percentage = self.random_slider.value()
        self.grid.randomize(percentage)
        self.grid_widget.update()

    def update_timer_interval(self):
        self.timer.setInterval(self.speed_slider.value())

class GridWidget(QWidget):
    def __init__(self, grid, cell_size):
        super().__init__()
        self.grid = grid
        self.cell_size = cell_size
        self.setFixedSize(grid.cols * cell_size, grid.rows * cell_size)

    def paintEvent(self, event):
        painter = QPainter(self)
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                rect_x = col * self.cell_size
                rect_y = row * self.cell_size
                color = QColor("lightgreen") if self.grid.grid[row][col] == 1 else QColor("white")
                painter.fillRect(rect_x, rect_y, self.cell_size, self.cell_size, color)
                painter.setPen(QColor("black"))
                painter.drawRect(rect_x, rect_y, self.cell_size, self.cell_size)

    def mousePressEvent(self, event):
        self.handle_mouse_event(event)

    def mouseMoveEvent(self, event):
        self.handle_mouse_event(event)

    def handle_mouse_event(self, event):
        if event.buttons() & Qt.LeftButton:
            col = event.x() // self.cell_size
            row = event.y() // self.cell_size
            if 0 <= row < self.grid.rows and 0 <= col < self.grid.cols:
                self.grid.toggle_cell(row, col)
                self.update()
