from collections import deque
import copy

from colorama import Back, Fore

from cell import Cell
from current_position import Current_position

class Algoritims2:
    def bfs(self, rows, cols, board):
        queue = deque([(board, [])]) 
        visited = set()

        while queue:
            current_board, path = queue.popleft()

            board_str = self.board_to_str(current_board)
            if board_str in visited:
                continue
            
            visited.add(board_str)
            self.print_board(current_board)
            
            if self.is_goal_state(current_board):
                print("Goal state reached")
                self.print_board(current_board)
                return current_board

            magnet_positions = self.get_magnet_positions(rows, cols, current_board)
            for magnet_x, magnet_y in magnet_positions:
                moves = self.get_moves(rows, cols, current_board)
                for move in moves:
                    n_board = self.copy_board(rows, cols, current_board)
                    self.move_magnet(magnet_x, magnet_y, move.pos_x, move.pos_y, n_board)
                    queue.append((n_board, path + [(magnet_x, magnet_y, move.pos_x, move.pos_y)]))

        print("No solution found")
        return None

    def is_goal_state(self, board):
        for row in board.board:
            for cell in row:
                if cell.whiteSpace and cell.cell_type not in ['I', 'N', 'R']:
                    return False
        return True

    def place_cell(self, n_board, x, y, cell_type, whiteSpace):
        cell = Cell(x, y, cell_type, whiteSpace)
        n_board.board[x][y] = cell

    def get_magnet_positions(self, rows, cols, board):
        magnet_positions = []
        for x in range(rows):
            for y in range(cols):
                if board.board[x][y].cell_type in ['R', 'N']:
                    magnet_positions.append((x, y))
        return magnet_positions

    def get_moves(self, rows, cols, board):
        moves = []
        for x in range(rows):
            for y in range(cols):
                if board.board[x][y].cell_type == '.':
                    move = Current_position(x, y)
                    moves.append(move)
        return moves

    def copy_board(self, rows, cols, board):
        from board import Board
        n_board = Board(rows, cols)
        for x in range(rows):
            for y in range(cols):
                n_board.board[x][y] = copy.deepcopy(board.board[x][y])
        return n_board

    def move_magnet(self, magnet_x, magnet_y, avail_x, avail_y, n_board):
        if n_board.board[magnet_x][magnet_y].cell_type == 'R':
            if n_board.board[avail_x][avail_y].whiteSpace:
                self.place_cell(n_board, avail_x, avail_y, 'R', True)
            else:
                self.place_cell(n_board, avail_x, avail_y, 'R', False)
            self.move_iron_towards_magnet_pos(n_board, avail_x, avail_y)
        elif n_board.board[magnet_x][magnet_y].cell_type == 'N':
            if n_board.board[avail_x][avail_y].whiteSpace:
                self.place_cell(n_board, avail_x, avail_y, 'N', True)
            else:
                self.place_cell(n_board, avail_x, avail_y, 'N', False)
            self.move_iron_away_magnet_neg(n_board, avail_x, avail_y)
        
        if n_board.board[magnet_x][magnet_y].whiteSpace:
            self.place_cell(n_board, magnet_x, magnet_y, '.', True)
        else:
            self.place_cell(n_board, magnet_x, magnet_y, '.', False)

    def board_to_str(self, board):
        return ''.join([''.join([str(cell.cell_type) for cell in row]) for row in board.board])

    def print_board(self, n_board):
        for row in n_board.board:
            formatted_row = []
            for cell in row:
                if cell.whiteSpace:
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
        print("-------------------------------")

    def move_iron_towards_magnet_pos(self, n_board, magnet_pos_x, magnet_pos_y):
        for x in range(magnet_pos_x - 1, 0, -1):
            current_cell = n_board.board[x][magnet_pos_y]
            above_cell = n_board.board[x - 1][magnet_pos_y] if x - 1 >= 0 else None

            if current_cell.cell_type == '.':
                if above_cell and above_cell.cell_type in ['N', 'I']:
                    current_cell.cell_type, above_cell.cell_type = above_cell.cell_type, current_cell.cell_type

        for x in range(magnet_pos_x + 1, n_board.rows - 1, 1):
            current_cell = n_board.board[x][magnet_pos_y]
            below_cell = n_board.board[x + 1][magnet_pos_y] if x + 1 < n_board.rows else None

            if current_cell.cell_type == '.':
                if below_cell and below_cell.cell_type in ['N', 'I']:
                    current_cell.cell_type, below_cell.cell_type = below_cell.cell_type, current_cell.cell_type

        for y in range(magnet_pos_y - 1, 0, -1):
            current_cell = n_board.board[magnet_pos_x][y]
            left_cell = n_board.board[magnet_pos_x][y - 1] if y - 1 >= 0 else None

            if current_cell.cell_type == '.':
                if left_cell and left_cell.cell_type in ['N', 'I']:
                    current_cell.cell_type, left_cell.cell_type = left_cell.cell_type, current_cell.cell_type

        for y in range(magnet_pos_y + 1, n_board.cols - 1, 1):
            current_cell = n_board.board[magnet_pos_x][y]
            right_cell = n_board.board[magnet_pos_x][y + 1] if y + 1 < n_board.cols else None

            if current_cell.cell_type == '.':
                if right_cell and right_cell.cell_type in ['N', 'I']:
                    current_cell.cell_type, right_cell.cell_type = right_cell.cell_type, current_cell.cell_type

   
    def move_iron_away_magnet_neg(self,n_board, magnet_neg_x, magnet_neg_y):
        moved = False
        for x in range(magnet_neg_x - 1, 0, -1):
            if x < 1:
                break
            current_cell = n_board.board[x][magnet_neg_y]
            above_cell = n_board.board[x - 1][magnet_neg_y]

            if current_cell.cell_type == '.':
                continue
            elif current_cell.cell_type in ['R', 'I']:
                if above_cell.cell_type == '.':
                    above_cell.cell_type = current_cell.cell_type
                    current_cell.cell_type = '.'
                    moved = True
                    break
                elif x - 2 >= 0 and above_cell.cell_type in ['R', 'I']:
                    temp = n_board.board[x - 2][magnet_neg_y].cell_type
                    n_board.board[x - 2][magnet_neg_y].cell_type = above_cell.cell_type
                    above_cell.cell_type = '.'
                    above_cell.cell_type = temp
                    above_cell.cell_type = current_cell.cell_type
                    current_cell.cell_type = '.'
                    moved = True
                    break

        for x in range(magnet_neg_x + 1, n_board.rows-1):
            if x >= n_board.rows - 1:
                break
            current_cell = n_board.board[x][magnet_neg_y]
            below_cell = n_board.board[x + 1][magnet_neg_y]

            if current_cell.cell_type == '.':
                continue
            elif current_cell.cell_type in ['R', 'I']:
                if below_cell.cell_type == '.':
                    below_cell.cell_type = current_cell.cell_type
                    current_cell.cell_type = '.'
                    moved = True
                    break
                elif x + 2 < n_board.rows and below_cell.cell_type in ['R', 'I']:
                    temp = n_board.board[x + 2][magnet_neg_y].cell_type
                    n_board.board[x + 2][magnet_neg_y].cell_type = below_cell.cell_type
                    below_cell.cell_type = '.'
                    below_cell.cell_type = temp
                    below_cell.cell_type = current_cell.cell_type
                    current_cell.cell_type = '.'
                    moved = True
                    break

        for y in range(magnet_neg_y - 1, 0, -1):
            if y < 1:
                break
            current_cell = n_board.board[magnet_neg_x][y]
            left_cell = n_board.board[magnet_neg_x][y - 1]

            if current_cell.cell_type == '.':
                continue
            elif current_cell.cell_type in ['R', 'I']:
                if left_cell.cell_type == '.':
                    left_cell.cell_type = current_cell.cell_type
                    current_cell.cell_type = '.'
                    moved = True
                    break
                elif y - 2 >= 0 and left_cell.cell_type in ['R', 'I']:
                    temp = n_board.board[magnet_neg_x][y - 2].cell_type
                    n_board.board[magnet_neg_x][y - 2].cell_type = left_cell.cell_type
                    left_cell.cell_type = '.'
                    left_cell.cell_type = temp
                    left_cell.cell_type = current_cell.cell_type
                    current_cell.cell_type = '.'
                    moved = True
                    break

        for y in range(magnet_neg_y + 1, n_board.cols-1):
            if y >= n_board.cols - 1:
                break
            current_cell = n_board.board[magnet_neg_x][y]
            right_cell = n_board.board[magnet_neg_x][y + 1]

            if current_cell.cell_type == '.':
                continue
            elif current_cell.cell_type in ['R', 'I']:
                if right_cell.cell_type == '.':
                    right_cell.cell_type = current_cell.cell_type
                    current_cell.cell_type = '.'
                    moved = True
                    break
                elif y + 2 < n_board.cols and right_cell.cell_type in ['R', 'I']:
                    temp = n_board.board[magnet_neg_x][y + 2].cell_type
                    n_board.board[magnet_neg_x][y + 2].cell_type = right_cell.cell_type
                    right_cell.cell_type = '.'
                    right_cell.cell_type = temp
                    right_cell.cell_type = current_cell.cell_type
                    current_cell.cell_type = '.'
                    moved = True