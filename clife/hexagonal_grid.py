class HexagonalGridLogic:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = {}
        self.initialize_grid()

    def initialize_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.get_hex_neighbors(row, col)
                self.grid[(row, col)] = {'state': 0, 'neighbors': neighbors}

    def get_hex_neighbors(self, row, col):
        """Get the 6 hexagonal neighbors for offset coordinates (odd-column offset)"""
        neighbors = []
        
        if col % 2 == 0:  # Even column
            directions = [
                (-1, -1), (-1, 0),  # NW, NE
                (0, -1), (0, 1),    # W, E
                (1, -1), (1, 0)     # SW, SE
            ]
        else:  # Odd column
            directions = [
                (-1, 0), (-1, 1),   # NW, NE
                (0, -1), (0, 1),    # W, E
                (1, 0), (1, 1)      # SW, SE
            ]
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                neighbors.append((nr, nc))
        
        return neighbors

    def toggle_cell(self, row, col):
        self.grid[(row, col)]['state'] = 1 - self.grid[(row, col)]['state']

    def randomize(self, percentage):
        import random
        for cell in self.grid.values():
            cell['state'] = 1 if random.random() < percentage / 100 else 0

    def reset(self):
        for cell in self.grid.values():
            cell['state'] = 0

    def get_next_state(self, survival_min, survival_max, birth_min, birth_max):
        new_grid = {}
        for (row, col), cell in self.grid.items():
            neighbors = sum(self.grid[neighbor]['state'] for neighbor in cell['neighbors'])
            if cell['state'] == 1:
                # Use dynamic survival parameters
                new_grid[(row, col)] = {'state': 1 if survival_min <= neighbors <= survival_max else 0, 'neighbors': cell['neighbors']}
            else:
                # Use dynamic birth parameters
                new_grid[(row, col)] = {'state': 1 if birth_min <= neighbors <= birth_max else 0, 'neighbors': cell['neighbors']}
        self.grid = new_grid