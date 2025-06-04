class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def toggle_cell(self, row, col):
        self.grid[row][col] = 1 - self.grid[row][col]

    def randomize(self, percentage):
        import random
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = 1 if random.random() < percentage / 100 else 0

    def reset(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def get_next_state(self):
        def count_neighbors(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            count = 0
            for dr, dc in directions:
                nr = (r + dr) % self.rows  # Wrap around vertically
                nc = (c + dc) % self.cols  # Wrap around horizontally
                count += self.grid[nr][nc]
            return count

        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = count_neighbors(row, col)
                if self.grid[row][col] == 1:
                    new_grid[row][col] = 1 if neighbors in [2, 3] else 0
                else:
                    new_grid[row][col] = 1 if neighbors == 3 else 0
        self.grid = new_grid
