class Queen:
    """Class representing the position of a Queen on the chessboard."""
    def __init__(self, row, column):
        self.row = row
        self.column = column

        if self.row < 0:
            raise ValueError("row not positive")
        elif self.row > 7:
            raise ValueError("row not on board")
        elif self.column < 0:
            raise ValueError("column not positive")
        elif self.column > 7:
            raise ValueError("column not on board")

    def can_attack(self, another_queen):    
        other_row = another_queen.row
        other_column = another_queen.column
        
        row_diff = abs(self.row - other_row)
        column_diff = abs(self.column - other_column)

        if (self.row == other_row and self.column == other_column):
            raise ValueError("Invalid queen position: both queens in the same square")

        if (self.row == other_row or self.column == other_column) or (row_diff == column_diff):
            return True
        return False
