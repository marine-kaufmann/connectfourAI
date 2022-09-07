#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: kincaid lacorte
# email: kalc@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name: Marine Kaufmann
# partner's email: marineka@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, depth_limit):
        ''' initializes searcher object with depth limit inserted'''
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        ''' adds a single state to states attribute '''
        self.states += [new_state]
        
    def should_add(self, state):
        ''' checks to see if a state is past the depth limit or has been 
        evaluated before, if not, returns True 
        '''
        if self.depth_limit != -1:
            if state.num_moves > self.depth_limit:
                return False
        if state.creates_cycle() == True:
            return False
        return True
    
    def add_states(self, new_states):
        ''' takes in a list of states and adds all that should
        be added according to should_add
        '''
        for i in range(len(new_states)):
            if self.should_add(new_states[i]) == True:
                self.add_state(new_states[i])
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        ''' finds the route to a solution of a given state '''
        self.add_state(init_state)
        while len(self.states) > 0:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal() == True:
                return s
            else:
                k = s.generate_successors()
                for i in range(len(k)):
                    if self.should_add(k[i]) == True:
                        self.add_state(k[i])
        return None
    
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    
    def next_state(self):
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    
    def next_state(self):
        s = self.states[-1]
        self.states.remove(s)
        return s
        


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    ''' a heuristic function that evaluates the number of 
    misplaced tiles in a board '''
    return state.board.num_misplaced()

def h2(state):
    ''' a heuristic function that works '''
    accu = 0
    for r in range(3):
        for c in range(3):
            if state.board.tiles[r][c] in GOAL_TILES[r]:
                x = 3
            else:
                accu += 1
            inter = int(state.board.tiles[r][c])
            if c == 0:
                if inter % 3 != 0:
                    accu += 1
            if c == 1:
                if inter % 3 != 1:
                    accu += 1
            if c == 2:
                if inter % 3 != 2:
                    accu += 1
    return accu
            
    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def __init__(self, heuristic):
        #Call search constructor
        super().__init__(-1)
        
        #Initialize non-inherited fields
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
        
    def add_state(self, state):
        ''' checks to see if a state should be added, if it should,
        calculuates priority according to the heuristic function, then 
        adds a sublist to self.states with priority and state'''
        if self.should_add(state) == True:
            k = self.priority(state)
            self.states += [[k, state]]
    
    def next_state(self):
        ''' finds the next state based on greedysearchers criteria'''
        s = max(self.states)
        self.states.remove(s)
        return s[1]
        


### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    ''' a class for objects that performed A Star based state-based search
    on an eight puzzle '''
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher and the 
        number of moves already taken
            """
        return -1 * (self.heuristic(state) + state.num_moves)
