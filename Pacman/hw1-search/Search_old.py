# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #print type(problem.getSuccessors(problem.getStartState())[0])
    #print "(1,1) is Goal?:", problem.isGoalState((1,1))
    #print "End Successors:", problem.getSuccessors((1,1))
    #print '\n'
    "*** YOUR CODE HERE ***"
    # command: 
    #   python pacman.py -l tinyMaze -p SearchAgent --frameTime 0
    #   python pacman.py -l mediumMaze -p SearchAgent --frameTime 0
    #   python pacman.py -l bigMaze -z .5 -p SearchAgent --frameTime 0
    Stack = util.Stack()
    Visited = []
    motion = []  

    def _dfs(v):
        if Stack.isEmpty()==0:
            if v[0]!=problem.getStartState():
                Stack.push(v)
            Visited.append(v[0])
            next = problem.getSuccessors(v[0])
            i = len(next)-1
            while(i>=0):
                if (next[i][0] not in Visited):
                    if problem.isGoalState(next[i][0]):
                        print 'Find Goal'
                        motion.insert(0, next[i][1])
                        while(Stack.isEmpty()==0):
                            direction = Stack.pop()[1]
                            if direction == 'Start':
                                return 
                            else:
                                motion.insert( 0, direction )
                    else:
                        _dfs(next[i])
                i = i - 1
            if Stack.isEmpty()==0:
                Stack.pop()

    Start = () + (problem.getStartState(),) + ('Start',) + (1,)
    Stack.push(Start)
    _dfs(Start)
    #print motion
    #print len(motion)
    return motion
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime 0
    #python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5 --frameTime 0
    "*** YOUR CODE HERE ***"

    class ChildNode:
        def __init__(self, state, parent, action, cost):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost
        def getState(self):
            return self.state
        def getParent(self):
            return self.parent
        def getAction(self):
            return self.action
        def getCost(self):
            return self.cost

    Queue = util.Queue()
    Visited = []
    Nodes = []
    motion = []

    Start = () + (problem.getStartState(),) + ('Start',) + (1,) + (1,) #cost
    Queue.push(Start)
    Visited.append(problem.getStartState())
    while(Queue.isEmpty!=1):
        v = Queue.pop()
        w = problem.getSuccessors(v[0])
        for i in range( len(w) ):
            if problem.isGoalState(w[i][0]):
                print 'Find Goal'
                motion.insert(0, w[i][1])
                cur_state = v
                while(1):
                    if cur_state[0] == problem.getStartState():
                        return motion
                    for node in Nodes:
                        if node.getState() == cur_state[0]:
                            motion.insert(0, node.getAction())
                            cur_state = node.getParent()                         

            if w[i][0] not in Visited:
                Visited.append(w[i][0])
                Queue.push(w[i] + (v[3]+1,) )
                CN = ChildNode(w[i][0], v, w[i][1], v[3]+1)
                Nodes.append(CN)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
    #python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
    #python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

    class ChildNode:
        def __init__(self, state, parent, action, cost):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost
        def getState(self):
            return self.state
        def getParent(self):
            return self.parent
        def getAction(self):
            return self.action
        def getCost(self):
            return self.cost
        def SetCost(self, new_cost):
            self.cost = new_cost

    PriorQueue = util.PriorityQueue()
    frontier = []
    Visited = []
    Nodes = []
    motion = []
    Cost = 0

    Start = () + (problem.getStartState(),) + ('Start',) + (0,)
    Nodes.append(ChildNode(problem.getStartState(), 'None', 'None', 0))
    PriorQueue.push(Start, 0)
    frontier.append(problem.getStartState())
    
    while(PriorQueue.isEmpty!=1):
        v = PriorQueue.pop()
        w = problem.getSuccessors(v[0])
        for node in Nodes:
            if node.getState() == v[0]:
                Cost = node.getCost()
                break;

        if problem.isGoalState(v[0]):
            print 'Find Goal'          
            for node in Nodes:
                    if node.getState() == v[0]:
                        cur_state = node.getParent()
                        motion.insert(0, node.getAction())
                        break
            while(1):
                if cur_state[0] == problem.getStartState():
                    return motion
                for node in Nodes:
                    if node.getState() == cur_state[0]:
                        motion.insert(0, node.getAction())
                        cur_state = node.getParent()          

        Visited.append(v[0])
        for i in range( len(w) ):                        
            if w[i][0] not in Visited:
                if w[i] not in frontier:
                    frontier.append(w[i][0])
                    Nodes.append( ChildNode(w[i][0], v, w[i][1], Cost+w[i][2]) )
                    PriorQueue.update( w[i], Cost+w[i][2] )
                elif (w[i] in frontier):
                    for node in Nodes:
                        if node.getState() == w[i][0]:
                            Orig_Cost = node.getCost()
                            if( Orig_Cost > Cost+w[i][2] ):
                                PriorQueue.update( w[i], Cost+w[i][2] )
                                node.SetCost(Cost+w[i][2])
                            break
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    # print heuristic(problem.getStartState(), problem) 34
    class ChildNode:
        def __init__(self, state, parent, action, cost):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost
        def getState(self):
            return self.state
        def getParent(self):
            return self.parent
        def getAction(self):
            return self.action
        def getCost(self):
            return self.cost
        def SetCost(self, new_cost):
            self.cost = new_cost

    PriorQueue = util.PriorityQueue()
    frontier = []
    Visited = []
    Nodes = []
    motion = []
    Cost = 0

    Start = () + (problem.getStartState(),) + ('Start',) + (0,)
    Nodes.append(ChildNode(problem.getStartState(), 'None', 'None', 0))
    PriorQueue.push(Start, 0)
    frontier.append(problem.getStartState())
    
    while(PriorQueue.isEmpty!=1):
        v = PriorQueue.pop()
        w = problem.getSuccessors(v[0])
        for node in Nodes:
            if node.getState() == v[0]:
                Cost = node.getCost()
                break;
        
        if problem.isGoalState(v[0]):
            print 'Find Goal'        
            for node in Nodes:
                    if node.getState() == v[0]:
                        cur_state = node.getParent()
                        motion.insert(0, node.getAction())
                        break
            while(1):
                if cur_state[0] == problem.getStartState():
                    return motion
                for node in Nodes:
                    if node.getState() == cur_state[0]:
                        motion.insert(0, node.getAction())
                        cur_state = node.getParent()          

        Visited.append(v[0])
        for i in range( len(w) ):                        
            if w[i][0] not in Visited:
                if w[i] not in frontier:
                    frontier.append(w[i][0])
                    Nodes.append( ChildNode(w[i][0], v, w[i][1], Cost+w[i][2]+heuristic(w[i][0],problem)) )
                    PriorQueue.update( w[i], Cost+w[i][2]+heuristic(w[i][0],problem) )
                elif (w[i] in frontier):
                    for node in Nodes:
                        if node.getState() == w[i][0]:
                            Orig_Cost = node.getCost()
                            if( Orig_Cost > Cost+w[i][2]+heuristic(w[i][0],problem) ):
                                PriorQueue.update( w[i], Cost+w[i][2]+heuristic(w[i][0],problem) )
                                node.SetCost(Cost+w[i][2]+heuristic(w[i][0],problem))
                            break

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
