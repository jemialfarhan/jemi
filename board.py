from cell import Cell
from colorama import Fore, Back, Style, init


init()

class Board:
    white_space_counter = 0
    white_filled_counter = 0
    def __init__(self, rows=5, cols=5,lives=3):
        self.rows = rows
        self.cols = cols
        self.lives = lives
        self.board = []
        for y in range(rows):
            row = []
            for x in range(cols):
                row.append(Cell(x, y))
            self.board.append(row)

        
    def place_cell(self,x,y,cell_type,whiteSpace):
      cell = Cell(x,y,cell_type,whiteSpace)
      self.board[x][y] = cell

    def magnet_selector(self):
      
      while self.lives > 0:
        isFound = False  
        input_magnet_type = input("Enter magnet type [R - N]: ")
        if input_magnet_type not in ['R','N']:
            print("Enter A Valid Magnet type")
            continue  
        for row in range(self.rows): 
            for col in range(self.cols):
                
               if self.board[row][col].cell_type == input_magnet_type:
                   isFound = True
                   print(f"There is {input_magnet_type} magnet type at [{row}][{col}]")
                   magnet_pos_x = row
                   magnet_pos_y = col
                   
        if isFound == False:
            print(f"Magnet type {input_magnet_type} not found")
            continue   
        
        new_magnet_pos_x = int(input("Choose new X position: "))
        new_magnet_pos_y = int(input("Choose new Y position: "))

        if 0 <= new_magnet_pos_x < self.rows and 0 <= new_magnet_pos_y < self.cols:
                if self.board[new_magnet_pos_x][new_magnet_pos_y].cell_type in [' ', 'R', 'N', 'I']:
                    print("Cannot place here!")
                    return
                else:
                    self.board[new_magnet_pos_x][new_magnet_pos_y].cell_type = self.board[magnet_pos_x][magnet_pos_y].cell_type
                    if self.board[magnet_pos_x][magnet_pos_y].whiteSpace == True:
                        self.board[magnet_pos_x][magnet_pos_y].cell_type = '.'
                    else:
                        self.board[magnet_pos_x][magnet_pos_y].cell_type = '.'
                    print(f"Magnet moved to new position [{new_magnet_pos_x}] [{new_magnet_pos_y}]")
                    if self.board[new_magnet_pos_x][new_magnet_pos_y].cell_type == 'R':
                        self.move_iron_towards_magnet_pos(new_magnet_pos_x, new_magnet_pos_y)
                    else:
                        self.move_iron_away_magnet_neg(new_magnet_pos_x, new_magnet_pos_y)
                    self.print_board()
                    self.check_filled()
                    self.lives = self.lives - 1
        else:
                print("New position is out of bounds")

      if self.lives <= 0:
        print("Game Over")
        

    def move_iron_towards_magnet_pos(self, magnet_pos_x, magnet_pos_y):
        
     for x in range(magnet_pos_x - 1, -1, -1):
        current_cell = self.board[x][magnet_pos_y]
        above_cell = self.board[x - 1][magnet_pos_y] if x - 1 >= 0 else None

        if current_cell.cell_type == '.':
            if above_cell and above_cell.cell_type in ['N', 'I']:
                current_cell.cell_type, above_cell.cell_type = above_cell.cell_type, current_cell.cell_type

   
     for x in range(magnet_pos_x + 1, self.rows):
        current_cell = self.board[x][magnet_pos_y]
        below_cell = self.board[x + 1][magnet_pos_y] if x + 1 < self.rows else None

        if current_cell.cell_type == '.':
            if below_cell and below_cell.cell_type in ['N', 'I']:
                current_cell.cell_type, below_cell.cell_type = below_cell.cell_type, current_cell.cell_type

  
     for y in range(magnet_pos_y - 1, -1, -1):
        current_cell = self.board[magnet_pos_x][y]
        left_cell = self.board[magnet_pos_x][y-1] if y - 1 >= 0 else None

        if current_cell.cell_type == '.':
            if left_cell and left_cell.cell_type in ['N', 'I']:
                current_cell.cell_type, left_cell.cell_type = left_cell.cell_type, current_cell.cell_type
                

    
     for y in range(magnet_pos_y + 1, self.cols):
        current_cell = self.board[magnet_pos_x][y]
        right_cell = self.board[magnet_pos_x][y+1] if y + 1 < self.cols else None

        if current_cell.cell_type == '.':
            if right_cell and right_cell.cell_type in ['N', 'I']:
                current_cell.cell_type, right_cell.cell_type = right_cell.cell_type, current_cell.cell_type


    def move_iron_away_magnet_neg(self, magnet_neg_x, magnet_neg_y):
    
       for x in range(magnet_neg_x - 1, 0, -1):
        current_cell = self.board[x][magnet_neg_y]
        above_cell = self.board[x - 1][magnet_neg_y] if x - 1 >= 0 else None

        if current_cell.cell_type == '.':
            continue
        elif current_cell.cell_type in ['R', 'I']:
            if above_cell and above_cell.cell_type == '.':
                above_cell.cell_type = current_cell.cell_type
                current_cell.cell_type = '.'
                break
            elif above_cell and above_cell.cell_type in ['R', 'I']:
                temp = above_cell.cell_type
                self.board[x - 2][magnet_neg_y].cell_type = above_cell.cell_type
                above_cell.cell_type = '.'
                self.board[x - 2][magnet_neg_y].cell_type = temp
                above_cell.cell_type = current_cell.cell_type
                current_cell.cell_type = '.'
                break

    
       for x in range(magnet_neg_x + 1, self.rows - 1):
        current_cell = self.board[x][magnet_neg_y]
        below_cell = self.board[x + 1][magnet_neg_y] if x + 1 < self.rows else None

        if current_cell.cell_type == '.':
            continue
        elif current_cell.cell_type in ['R', 'I']:
            if below_cell and below_cell.cell_type == '.':
                below_cell.cell_type = current_cell.cell_type
                current_cell.cell_type = '.'
                break
            elif below_cell and below_cell.cell_type in ['R', 'I']:
                temp = below_cell.cell_type
                self.board[x + 2][magnet_neg_y].cell_type = below_cell.cell_type
                below_cell.cell_type = '.'
                self.board[x + 2][magnet_neg_y].cell_type = temp
                below_cell.cell_type = current_cell.cell_type
                current_cell.cell_type = '.'
                break

    
       for y in range(magnet_neg_y - 1, 0, -1):
        current_cell = self.board[magnet_neg_x][y]
        left_cell = self.board[magnet_neg_x][y - 1] if y - 1 >= 0 else None

        if current_cell.cell_type == '.':
            continue
        elif current_cell.cell_type in ['R', 'I']:
            if left_cell and left_cell.cell_type == '.':
                left_cell.cell_type = current_cell.cell_type
                current_cell.cell_type = '.'
                break
            elif left_cell and left_cell.cell_type in ['R', 'I']:
                temp = left_cell.cell_type
                self.board[magnet_neg_x][y - 2].cell_type = left_cell.cell_type
                left_cell.cell_type = '.'
                self.board[magnet_neg_x][y - 2].cell_type = temp
                left_cell.cell_type = current_cell.cell_type
                current_cell.cell_type = '.'
                break

    
       for y in range(magnet_neg_y + 1, self.cols - 1):
        current_cell = self.board[magnet_neg_x][y]
        right_cell = self.board[magnet_neg_x][y + 1] if y + 1 < self.cols else None

        if current_cell.cell_type == '.':
            continue
        elif current_cell.cell_type in ['R', 'I']:
            if right_cell and right_cell.cell_type == '.':
                right_cell.cell_type = current_cell.cell_type
                current_cell.cell_type = '.'
                break
            elif right_cell and right_cell.cell_type in ['R', 'I']:
                temp = right_cell.cell_type
                self.board[magnet_neg_x][y + 2].cell_type = right_cell.cell_type
                right_cell.cell_type = '.'
                self.board[magnet_neg_x][y + 2].cell_type = temp
                right_cell.cell_type = current_cell.cell_type
                current_cell.cell_type = '.'
                break


            
    def check_filled(self):     
       for row in range(self.rows):
        for col in range(self.cols):
            if self.board[row][col].whiteSpace == True:
              self.white_space_counter = self.white_space_counter + 1
              if self.board[row][col].cell_type in ['I','N','R']: 
                  self.board[row][col].whiteFilled = True
                  self.white_filled_counter = self.white_filled_counter + 1
              else:
                  self.board[row][col].whiteFilled = False
            else:
              pass
       self.check_won(self.white_space_counter,self.white_filled_counter)

    def check_won(self,white_space_counter,white_filled_counter):
          if white_space_counter == white_filled_counter:
            print("You Won")
            from levelselector import LevelSelector
            LevelSelector.select_level()
            return 
          else:
             self.white_space_counter = 0
             self.white_filled_counter = 0
             
    def print_board(self):
        for row in self.board:
            formatted_row = []
            for cell in row:
                if  cell.whiteSpace:
                    formatted_row.append(Fore.WHITE + Back.WHITE + cell.cell_type + Fore.RESET + Back.RESET)
                elif cell.cell_type == 'R':
                    formatted_row.append(Fore.RED + cell.cell_type + Fore.RESET)
                elif cell.cell_type == 'N':
                    formatted_row.append(Fore.MAGENTA + cell.cell_type + Fore.RESET)
                elif cell.cell_type == 'I':
                    formatted_row.append(Fore.BLACK + cell.cell_type + Fore.RESET)
                elif cell.cell_type == ' ':
                    formatted_row.append(Fore.BLACK + cell.cell_type + Fore.RESET)
                else:
                    formatted_row.append('.')
            print('  '.join(formatted_row))
      
      