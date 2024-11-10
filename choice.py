from bfs import Algoritims2

from board import Board
from dfs import Algoritims

class AlgorithmSelector:
    def __init__(self, board):
        self.select_algorithm(board)

    def select_algorithm(self, board):
        print("Choose an algorithm to execute:")
        print("1. Depth-First Search (DFS)")
        print("2. Breadth-First Search (BFS)")
        print("3. Player")

        choice = input("Enter the number of your choice: ")

        try:
            choice_num = int(choice)
            if choice_num == 1:
                Algoritims().dfs(board.rows, board.cols, board)
            elif choice_num == 2:
                Algoritims2().bfs(board.rows, board.cols, board)
            elif choice_num == 3:
                board.magnet_selector()
            else:
                print("Invalid choice. Please select a valid option.")
                self.select_algorithm(board)
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.select_algorithm(board)
