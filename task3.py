def bomber_man(n, grid):
    grid = [list(row) for row in grid]
    rows, cols = len(grid), len(grid[0])
    
    def detonate(positions):
        for r, c in positions:
            grid[r][c] = '.'
            if r > 0 and grid[r-1][c] == 'O':
                grid[r-1][c] = '.'
            if r < rows-1 and grid[r+1][c] == 'O':
                grid[r+1][c] = '.'
            if c > 0 and grid[r][c-1] == 'O':
                grid[r][c-1] = '.'
            if c < cols-1 and grid[r][c+1] == 'O':
                grid[r][c+1] = '.'
    if n == 1:
        return grid
    elif n == 2:
        return [['O' for _ in range(cols)] for _ in range(rows)]
   
    detonate([])
    if n == 3:
        return grid
    previous_positions = set()
    current_positions = set()
    for i in range(4, n+1):
        detonate(previous_positions)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '.':
                    grid[r][c] = 'O'
                    current_positions.add((r, c))
        previous_positions = current_positions
        current_positions = set()
    
    return grid









    
    
    

    
    
   






        
        
    
        

        
        
    
        
    
   







