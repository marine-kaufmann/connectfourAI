#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: kincaid lacorte
# email: kalc@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Marine Kaufmann
# partner's email: marineka@bu.edu
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
def process_file(filename, algorithm, param):
    ''' you give this bad boy a file, an algorithm, and a parameter, and 
    it's gonna tell you how many moves it took to solve each digit string
    how many states it tested, and some average data at the end '''
    file = open(filename, 'r')
    accu = 0
    movey = 0
    stater = 0
    for line in file: 
        fields = line.split('\n')
        fields = fields[:-1][0]
        init_board = Board(fields)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        if searcher == None:
            return
    
        soln = None
        
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            print('Search terminated.', end='')
    
        if soln == None:
            print(' Failed to find a solution.')
        else:
            accu += 1
            movey += soln.num_moves
            stater += searcher.num_tested
            print(fields,":", soln.num_moves, "moves,", 
                  searcher.num_tested, "states tested")
    print('\n')
    print("solved", accu, "puzzles")
    print("averages:", movey/accu, "moves,", stater/accu, "states tested")

        
    