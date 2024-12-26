class Game:
    def __init__(self):
        self.is_white = True  
        self.focused_cell = None  
        self.pieces_on_board = [
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ],
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', ],
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', ],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', ],
        ]
    
    def get_piece(self, x, y):
        return self.pieces_on_board[y][x]
    
    def set_piece(self, x, y, value):
        self.pieces_on_board[y][x] = value
    
    def set_focus(self, x, y):
        if self.is_white and 'w' in self.get_piece(x, y):
            print("Можно попытаться сделать ход этой фигурой")
            self.focused_cell = (x, y)
        elif not self.is_white and 'b' in self.get_piece(x, y):
            print("Можно попытаться сделать ход этой фигурой")
            self.focused_cell = (x, y)
    
    def input(self, x , y):
        self.set_focus(x,y)
        self.move_piece(x,y)

    def get_focus(self):
        return self.focused_cell

    def move_piece(self, x, y):
        if self.focused_cell is None:
            return False
        else:
            Dx = x - self.focused_cell[0]
            Dy = y - self.focused_cell[1]

            if Dx == 1 or Dx == -1:
                if self.is_white and Dy == -1:
                    self.swap(x, y)
                
                elif not self.is_white and Dy == 1:
                    self.swap(x, y)

    def swap(self, x, y):
        piece = self.get_piece(self.get_focus()[0], self.get_focus()[1])
        self.set_piece(self.get_focus()[0], self.get_focus()[1], value= " ")
        self.set_piece(x, y, piece)
        self.focused_cell = None
        self.is_white = not self.is_white

    def check_win(self):
        cal_W = 0
        cal_B = 0
        for y in range(8):
            for x in range(8):
                cell = self.get_piece(x, y)
                if "b" in cell:
                    cal_B += 1

                elif "w" in cell:
                    cal_W += 1

        if cal_W == 0:
            return "b"
        
        elif cal_B == 0:
            return "W"
        
        return "-"