
from bfs import Algoritims2
from board import Board
from choice import AlgorithmSelector
from dfs import Algoritims


class Level1:
    
    def __init__(self):
        self.board = Board(rows=3, cols=4,lives=5)
        self.board.place_cell(2, 0,'N',False)
        self.board.place_cell(1, 2,'I',False)
        self.board.place_cell(1,1,'.',True)
        self.board.place_cell(1,3,'.',True)

    def display(self):
        AlgorithmSelector(self.board)
        
class Level2:
    
    def __init__(self):
        self.board = Board(rows=5, cols=5,lives=5)
        self.board.place_cell(2, 1,'I',False)
        self.board.place_cell(1, 2,'I',False)
        self.board.place_cell(2, 3,'I',False)
        self.board.place_cell(3, 2,'I',False)
        self.board.place_cell(0, 2,'.',True)
        self.board.place_cell(2, 0,'.',True)
        self.board.place_cell(2, 2,'.',True)
        self.board.place_cell(2, 4,'.',True)
        self.board.place_cell(4, 2,'.',True)
        self.board.place_cell(4, 0,'N',False)

    def display(self):
        AlgorithmSelector(self.board)
        
class Level3:
    
    def __init__(self):
        self.board = Board(rows=3, cols=4,lives=5)
        self.board.place_cell(0,0,' ',False)
        self.board.place_cell(0,1,' ',False)
        self.board.place_cell(0,2,' ',False)
        self.board.place_cell(1, 2,'I',False)
        self.board.place_cell(0, 3,'.',True)
        self.board.place_cell(2, 3,'.',True)
        self.board.place_cell(2, 0,'N',False)

    def display(self):
        AlgorithmSelector(self.board)
        
class Level4:
    
    def __init__(self):
        self.board = Board(rows=5, cols=3,lives=2)
        self.board.place_cell(1,0,' ',False)
        self.board.place_cell(3,0,' ',False)
        self.board.place_cell(1, 1,'I',False)
        self.board.place_cell(3, 1,'I',False)
        self.board.place_cell(0, 0,'.',True)
        self.board.place_cell(0, 2,'.',True)
        self.board.place_cell(4, 1,'.',True)
        self.board.place_cell(2, 0,'N',False)

    def display(self):
        AlgorithmSelector(self.board)
        
class Level5:
    
    def __init__(self):
        self.board = Board(rows=4, cols=3,lives=2)
        self.board.place_cell(0,1,' ',False)
        self.board.place_cell(1,1,' ',False)
        self.board.place_cell(2,1,' ',False)
        self.board.place_cell(1, 0,'I',True)
        self.board.place_cell(2, 0,'I',False)
        self.board.place_cell(1, 2,'I',True)
        self.board.place_cell(2, 2,'I',False)
        self.board.place_cell(0, 0,'.',True)
        self.board.place_cell(0, 2,'.',True)
        self.board.place_cell(3, 0,'.',True)
        self.board.place_cell(3, 1,'N',False)

    def display(self):
        AlgorithmSelector(self.board)
        
class Level6: 
 
    def __init__(self): 
        self.board = Board(rows=3, cols=5,lives=2) 
        self.board.place_cell(2, 0,'N',False) 
        self.board.place_cell(1, 1,'I',False) 
        self.board.place_cell(1, 3,'I',False) 
        self.board.place_cell(1,2,'.',True) 
        self.board.place_cell(0,3,'.',True) 
        self.board.place_cell(2,3,'.',True) 
 
    def display(self):
        AlgorithmSelector(self.board)
                 
        
class Level7: 
 
    def __init__(self): 
        self.board = Board(rows=5, cols=4,lives=2) 
        self.board.place_cell(0,0,'.',True) 
        self.board.place_cell(1, 0,'I',True) 
        self.board.place_cell(2, 0,'I',False) 
        self.board.place_cell(3, 1,'I',False) 
        self.board.place_cell(3, 2,'I',True) 
        self.board.place_cell(2, 1,'N',False) 
        self.board.place_cell(2,3,'.',True) 
        self.board.place_cell(4,3,'.',True) 
        self.board.place_cell(4,0,' ',False) 
        self.board.place_cell(4,1,' ',False) 
        self.board.place_cell(4,2,' ',False) 
 
    def display(self):
        AlgorithmSelector(self.board)
            
class Level8: 
 
    def __init__(self): 
        self.board = Board(rows=3, cols=4,lives=2) 
        self.board.place_cell(2, 0,'N',False) 
        self.board.place_cell(1, 1,'I',False) 
        self.board.place_cell(1, 2,'I',False) 
 
        self.board.place_cell(0,0,'.',True) 
        self.board.place_cell(0,2,'.',True) 
        self.board.place_cell(2,2,'.',True) 
 
    def display(self):
        AlgorithmSelector(self.board)
                
        
class Level9: 
 
    def __init__(self): 
        self.board = Board(rows=1, cols=7,lives=2) 
        self.board.place_cell(0, 0,'N',False) 
        self.board.place_cell(0, 1,'.',True) 
        self.board.place_cell(0,2,'I',True) 
        self.board.place_cell(0,5,'I',False) 
        self.board.place_cell(0,6,'.',True) 
         
 
    def display(self):
        AlgorithmSelector(self.board)
                 
 
class Level10: 
 
    def __init__(self): 
        self.board = Board(rows=4, cols=4,lives=2) 
        self.board.place_cell(0, 0,'N',False) 
        self.board.place_cell(1, 1,'.',True) 
        self.board.place_cell(1, 3,'.',True) 
        self.board.place_cell(2, 2,'I',False) 
        self.board.place_cell(2, 3,'I',False) 
        self.board.place_cell(3, 0,'.',True) 
        self.board.place_cell(3,1,'I',False) 
        self.board.place_cell(3,3,'.',True) 
         
 
    def display(self):
        AlgorithmSelector(self.board)
                 
                  
class Level11: 
 
    def __init__(self): 
        self.board = Board(rows=2, cols=5,lives=1) 
        self.board.place_cell(0, 1,'.',True) 
        self.board.place_cell(0, 2,'.',True) 
        self.board.place_cell(0, 3,'.',True) 
        self.board.place_cell(0, 0,'I',False) 
        self.board.place_cell(0, 4,'I',False) 
        self.board.place_cell(1,2,'R',False) 
        self.board.place_cell(1,0,' ',False) 
        self.board.place_cell(1,1,' ',False) 
        self.board.place_cell(1,3,' ',False) 
        self.board.place_cell(1,4,' ',False) 
 
    def display(self):
        AlgorithmSelector(self.board)
                 
 
class Level12: 
 
    def __init__(self): 
        self.board = Board(rows=5, cols=4,lives=1) 
        self.board.place_cell(0, 0,'I',False) 
        self.board.place_cell(1, 0,'I',True) 
        self.board.place_cell(4, 3,'I',False) 
        self.board.place_cell(2,0,'.',True) 
        self.board.place_cell(4, 0,'.',True) 
        self.board.place_cell(4, 2,'.',True) 
        self.board.place_cell(3,1,'R',False) 
        self.board.place_cell(0,2,' ',False) 
        self.board.place_cell(0,3,' ',False) 
        self.board.place_cell(1,2,' ',False) 
        self.board.place_cell(1,3,' ',False) 
 
    def display(self):
        AlgorithmSelector(self.board)
             
        
class Level13: 
     
    def __init__(self): 
        self.board = Board(rows=3, cols=6,lives=2) 
        self.board.place_cell(0, 0,'I',False) 
        self.board.place_cell(0, 4,'I',True) 
        self.board.place_cell(0, 5,'I',False) 
        self.board.place_cell(0,3,'.',True) 
        self.board.place_cell(1,1,'.',True) 
        self.board.place_cell(2,1,'.',True) 
        self.board.place_cell(2,3,'R',False) 
        self.board.place_cell(1,0,' ',False) 
        self.board.place_cell(2,0,' ',False) 
        self.board.place_cell(1,4,' ',False) 
        self.board.place_cell(1,5,' ',False) 
        self.board.place_cell(2,4,' ',False) 
        self.board.place_cell(2,5,' ',False) 
 
 
    def display(self):
        AlgorithmSelector(self.board)
                 
 
class Level14: 
     
    def __init__(self): 
        self.board = Board(rows=4, cols=4,lives=2) 
        self.board.place_cell(0, 3,'I',False) 
        self.board.place_cell(2, 0,'I',False) 
        self.board.place_cell(3, 0,'I',False) 
        self.board.place_cell(1,0,'.',True) 
        self.board.place_cell(1,2,'.',True) 
        self.board.place_cell(2,1,'.',True) 
        self.board.place_cell(2,2,'.',True) 
        self.board.place_cell(3,3,'R',False) 
 
 
    def display(self):
        AlgorithmSelector(self.board)
                   
 
 
class Level15: 
     
    def __init__(self): 
        self.board = Board(rows=3, cols=5,lives=2) 
        self.board.place_cell(0, 1,'I',False) 
        self.board.place_cell(0, 3,'I',False) 
        self.board.place_cell(0,0,'.',True) 
        self.board.place_cell(0,2,'.',True) 
        self.board.place_cell(1,4,'.',True) 
        self.board.place_cell(2,4,'.',True) 
        self.board.place_cell(1,2,'N',False) 
        self.board.place_cell(2,2,'R',False) 
 
    def display(self):
        AlgorithmSelector(self.board)
                 
 
class Level16: 
     
    def __init__(self): 
        self.board = Board(rows=5, cols=5,lives=3) 
        self.board.place_cell(1, 2,'I',False) 
        self.board.place_cell(3, 2,'I',False) 
        self.board.place_cell(0,3,'.',True) 
        self.board.place_cell(0,4,'.',True) 
        self.board.place_cell(4,0,'.',True) 
        self.board.place_cell(4,3,'.',True) 
        self.board.place_cell(2,4,'N',False) 
        self.board.place_cell(2,0,'R',False) 
 
    def display(self):
        AlgorithmSelector(self.board)
                   
 
 
class Level17: 
     
    def __init__(self): 
        self.board = Board(rows=4, cols=4,lives=2) 
        self.board.place_cell(0, 2,'I',False) 
        self.board.place_cell(2, 0,'I',False) 
        self.board.place_cell(1,1,'.',True) 
        self.board.place_cell(1,3,'.',True) 
        self.board.place_cell(2,2,'.',True) 
        self.board.place_cell(3,1,'.',True) 
        self.board.place_cell(3,3,'N',False) 
        self.board.place_cell(0,0,'R',False) 
    def display(self):
        AlgorithmSelector(self.board)
                 
 
class Level18: 
     
    def __init__(self): 
        self.board = Board(rows=5, cols=6,lives=2) 
        self.board.place_cell(0, 3,'I',False) 
        self.board.place_cell(2, 0,'I',False) 
        self.board.place_cell(2, 5,'I',True) 
        self.board.place_cell(1,3,'.',True) 
        self.board.place_cell(2,1,'.',True) 
        self.board.place_cell(2,2,'.',True) 
        self.board.place_cell(2,3,'.',True) 
        self.board.place_cell(4,3,'N',False) 
        self.board.place_cell(4,2,'R',False) 
        self.board.place_cell(0,0,' ',False) 
        self.board.place_cell(0,1,' ',False) 
        self.board.place_cell(1,0,' ',False) 
        self.board.place_cell(1,1,' ',False) 
        self.board.place_cell(0,4,' ',False) 
        self.board.place_cell(0,5,' ',False) 
        self.board.place_cell(1,4,' ',False) 
        self.board.place_cell(1,5,' ',False) 
        self.board.place_cell(4,0,' ',False) 
        self.board.place_cell(4,1,' ',False) 
        self.board.place_cell(4,4,' ',False) 
        self.board.place_cell(4,5,' ',False) 
 
    def display(self):
        AlgorithmSelector(self.board)
                   
        
class Level19: 
     
    def __init__(self): 
        self.board = Board(rows=5, cols=5,lives=4) 
        self.board.place_cell(0, 1,'I',False) 
        self.board.place_cell(0, 3,'I',False) 
        self.board.place_cell(4, 1,'I',False) 
        self.board.place_cell(4, 3,'I',False) 
        self.board.place_cell(1,0,'.',True) 
        self.board.place_cell(1,4,'.',True) 
        self.board.place_cell(2,1,'.',True) 
        self.board.place_cell(3,0,'.',True) 
        self.board.place_cell(3,2,'.',True) 
        self.board.place_cell(3,4,'.',True) 
        self.board.place_cell(0,2,'N',False) 
        self.board.place_cell(2,2,'R',False) 
        self.board.place_cell(0,0,' ',False) 
        self.board.place_cell(0,4,' ',False) 
        self.board.place_cell(2,0,' ',False) 
        self.board.place_cell(2,4,' ',False) 
        self.board.place_cell(4,0,' ',False) 
        self.board.place_cell(4,4,' ',False) 
         
 
    def display(self):
        AlgorithmSelector(self.board)
                 
 
class Level20: 
     
    def __init__(self): 
        self.board = Board(rows=5, cols=4,lives=2) 
        self.board.place_cell(0, 1,'I',True) 
        self.board.place_cell(0, 2,'I',False) 
        self.board.place_cell(4, 0,'I',False) 
        self.board.place_cell(0,3,'.',True) 
        self.board.place_cell(1,0,'.',True) 
        self.board.place_cell(2,0,'.',True) 
        self.board.place_cell(3,0,'.',True) 
        self.board.place_cell(4,2,'N',False) 
        self.board.place_cell(4,3,'R',False) 
         
 
    def display(self):
        AlgorithmSelector(self.board)
                  
        
class Level21: 
     
    def __init__(self): 
        self.board = Board(rows=3, cols=4,lives=2) 
        self.board.place_cell(0, 1,'I',False) 
        self.board.place_cell(1, 0,'I',True) 
        self.board.place_cell(1, 1,'I',True) 
        self.board.place_cell(1, 2,'I',False) 
        self.board.place_cell(0,2,'.',True) 
        self.board.place_cell(1,0,'.',True) 
        self.board.place_cell(2,1,'.',True) 
        self.board.place_cell(2,0,'N',True) 
        self.board.place_cell(2,3,'R',False) 
         
 
    def display(self):
        AlgorithmSelector(self.board)
                 
        
class Level22: 
     
    def __init__(self): 
        self.board = Board(rows=4, cols=5,lives=3) 
        self.board.place_cell(0, 3,'I',True) 
        self.board.place_cell(0, 4,'I',False) 
        self.board.place_cell(3, 0,'I',False) 
        self.board.place_cell(0,1,'.',True) 
        self.board.place_cell(1,0,'.',True) 
        self.board.place_cell(2,1,'.',True) 
        self.board.place_cell(1,4,'.',True) 
        self.board.place_cell(3,2,'R',False) 
        self.board.place_cell(0,0,'N',False) 
        self.board.place_cell(0,2,' ',False) 
        self.board.place_cell(1,2,' ',False) 
        self.board.place_cell(3,4,' ',False) 
 
 
 
    def display(self):
        AlgorithmSelector(self.board)
                  

class Level23: 
     
    def __init__(self): 
        self.board = Board(rows=4, cols=5,lives=3) 
        self.board.place_cell(0, 3,'I',False) 
        self.board.place_cell(1, 4,'I',True) 
        self.board.place_cell(2, 0,'I',False) 
 
        self.board.place_cell(0,2,'.',True) 
        self.board.place_cell(2,1,'.',True) 
        self.board.place_cell(2,2,'.',True) 
        self.board.place_cell(2,3,'.',True) 
 
        self.board.place_cell(3,2,'R',True) 
        self.board.place_cell(3,4,'N',False) 
 
    def display(self):
        AlgorithmSelector(self.board)
                    
        
class Level24: 
     
    def __init__(self): 
        self.board = Board(rows=5, cols=5,lives=3) 
        self.board.place_cell(0, 1,'I',False) 
        self.board.place_cell(1, 3,'I',False) 
        self.board.place_cell(3, 4,'I',False) 
        self.board.place_cell(0,3,'.',True) 
        self.board.place_cell(2,1,'.',True) 
        self.board.place_cell(2,3,'.',True) 
        self.board.place_cell(4,1,'.',True) 
        self.board.place_cell(4,2,'.',True) 
        self.board.place_cell(3,0,'R',False) 
        self.board.place_cell(1,4,'N',False)
        self.board.place_cell(4,0,' ',False) 
        self.board.place_cell(4,4,' ',False) 
 
    def display(self):
        AlgorithmSelector(self.board)
                  
        
        
class Level25: 
     
    def __init__(self): 
        self.board = Board(rows=5, cols=4,lives=3) 
        self.board.place_cell(0, 0,'I',True) 
        self.board.place_cell(1, 2,'I',False) 
        self.board.place_cell(3, 2,'I',False) 
        self.board.place_cell(4, 3,'I',False) 
        self.board.place_cell(0,3,'.',True) 
        self.board.place_cell(2,0,'.',True) 
        self.board.place_cell(4,1,'.',True) 
        self.board.place_cell(4,2,'.',True) 
        self.board.place_cell(0,3,'R',True) 
        self.board.place_cell(4,0,'N',True) 
 
 
    def display(self):
        AlgorithmSelector(self.board)
                   
        
 