#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: kincaid lacorte
# email: kalc@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Marine Kaufmann
# partner's email: marineka@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        for r in range(3):
            for c in range(3):
                if digitstr[3*r + c] == '0':
                    self.blank_r = r
                    self.blank_c = c
                self.tiles[r][c] = digitstr[3*r + c]


    ### Add your other method definitions below. ###
    
    def __repr__(self):
        """ an repr function that displays the board object
        as a string, with an underscore for the blank tile
        input: a board object
        """
        
        s = ''
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] == '0':
                    s += '_' + ' '
                else:
                    s += self.tiles[row][col] + ' '
            
            s += '\n'
        return s
    
    def move_blank(self, direction):
        """ a function that moves the blank tile around the board
            input: a board object, the direction to move the blank tile
                                    (up, down, left, right)
        """
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] == '0':
                    o = [row, col]
                    i = [row, col]
        
        # Moves coordinates of blank cell to new coordinates
        if direction == 'up':
            i[0] -= 1
        if direction == 'down':
            i[0] += 1
        if direction == 'left':
            i[1] -= 1
        if direction == 'right':
            i[1] += 1
            
            
        # Checks that new blank coordinates are valid            
        if i[0] > 2 or i[0] < 0:
            return False
        if i[1] > 2 or i[1] < 0:
            return False
        
        # Swaps tiles
        old = self.tiles[i[0]][i[1]]
        self.tiles[o[0]][o[1]] = old
        self.tiles[i[0]][i[1]] = '0'
        return True
        
    
    def digit_string(self):
        """ returns our current board as a string
            input: board
        """
        s = ''
        for r in range(3):
            for c in range(3):
                s += self.tiles[r][c]
        return s
        
    def copy(self):
        """ creates a deep copy of a board
        input: board
        """
        s = Board(self.digit_string())
        return s
        
    
    def num_misplaced(self):
        """ returns number of misplaced tiles
            input: board
        """
        i = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    i += 0
                else:
                    if self.tiles[r][c] != GOAL_TILES[r][c]:
                        i += 1
        return i
                    
    def __eq__(self, other):
        if self.tiles == other.tiles:
            return True
        return False
        
            
        
