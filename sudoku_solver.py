#solve_puzzle
import time

class sudoku_solver:

    def __init__(self):
        """ This class will be responsable to check if the 
        sodoku puzzle has a solution.
        If that so, the class will permited to user collect
        the answare.
        If not, will response "sodoku hasn't a solution".
        
        Args:
         problem:list -> list of lists with the sodoku structure
        
        Load Variables:
         _sudoku:list
         _recursions:int -> recursion counter
         _time_solution:None
        """
        self._sudoku:list
        self._recursions:int = 0
        self._time_solution:None

    def _check_quadrant(self, x:int, y:int) -> tuple[int, int]:
        """ This method will receve the line/collum position and return the
        quadrant. Sodoku has 9 quadrants, composed of a 3x3 matrix.
        
        Args:
         x:int -> line position
         y:int -> Collumn position
        Return:
         quadrant:Tuple[int,int]
        """
        return (x//3), (y//3)
    
    def _search_quadrant(self, qx:int, qy:int, search:int)->bool:
        """ This method will check if value in search variable 
        it's present in quadrant
        Args:
         qx:int -> quandrant position x
         qy:int -> quadrant position y
         search:int -> value search on quadrant
        Return:
         True, if value is present in quadrant
         False, if value is present in quadrant
        """
        qx = qx*3
        qy = qy*3
        for x in range(qx, qx+3):
            for y in range(qy, qy+3):
                if self._sudoku[x][y] == search:
                    return True
        return False
    
    def _search_line(self, x:int, search:int) -> bool:
        """ This method will check if the value in search variable 
        it's present in the same line passing for all 9 positions
        Args:
         y:int -> line position
         search:int -> value searched
        Return:
         True, if value is present in quadrant
         False, if value is not present in quadrant
        """
        for y in range(0,9):
            if self._sudoku[x][y] == search:
                return True
        return False
    
    def _search_collumn(self, y:int, search:int) -> bool:
        """ This method will check if the value in search variable 
        it's present in the same collumn passing for all 9 positions
        Args:
         y:int -> collumn position
         search:int -> value searched
        Return:
         True, if value is present in collumn
         False, if value is not present in collumn
        """
        for x in range(0,9):
            if self._sudoku[x][y] == search:
                return True
        return False
    
    def _solver(self)->bool:
        """ Method responsable for try to solve the sudoku puzzle 
        Return:
         True, if the answare is found
         False, if not
        """
        for x in range(0,9):
            for y in range(0,9):
                if self._sudoku[x][y] == 0:
                    for value in range(1,10):    
                        qx, qy = self._check_quadrant(x,y)
                        if not self._search_quadrant(qx, qy, value) and \
                            not self._search_line(x, value) and not self._search_collumn(y, value):
                            self._sudoku[x][y] = value
                            self._recursions+=1
                            if self._solver():
                                return True
                            self._sudoku[x][y] = 0
                    return False
        self._time_solution = time.time() - self._time_solution
        return True


    @property
    def sudoku(self):
        self._sudoku
    @sudoku.setter
    def sudoku(self, new_sudoku:list):
        self._sudoku = new_sudoku
        self._time_solution = time.time()
        self._recursions = 0
    @sudoku.getter
    def sudoku(self):
        return self._sudoku

    @property
    def recursion(self):
        self._recursions
    @recursion.getter
    def recursion(self):
        return self._recursions
    
    @property
    def time_solution(self):
        self._time_solution
    @time_solution.getter
    def time_solution(self):
        return self._time_solution