class Cell:
    def __init__(self,pos_x,pos_y,cell_type='.',whiteSpace=False,whiteFilled=False):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.cell_type = cell_type 
        self.whiteSpace = whiteSpace
        self.whiteFilled = whiteFilled
    def __str__(self):
        return self.cell_type if self.cell_type != '.' else '.'
