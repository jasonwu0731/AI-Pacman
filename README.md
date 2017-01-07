Artificial Intelligence, Pacman Game (Fall 2016)
======================================

##Intro
[The Pacman Projects](http://ai.berkeley.edu/project_overview.html) by the [University of California, Berkeley](http://berkeley.edu/).

![Animated gif pacman game](http://ai.berkeley.edu/images/pacman_game.gif)

> In this project, Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. Try to build general search algorithms and apply them to Pacman scenarios.

Start a game by the command:
```
$ python pacman.py
```
You can see the list of all options and their default values via:
```
$ python pacman.py -h
```

##HW1 Search
DFS, BFS, UCS, ASTAR, ASTAR heuristic 
```
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs
$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
$ python pacman.py -l bigMaze -p SearchAgent -a fn=ucs
$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
Corner problem, Corner heuristic
```
$ python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
$ python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

Eating all the dots
```
$ python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

> for more information, check [here](https://github.com/jasonwu0731/NTU-AI-Fall2016/blob/master/Pacman/hw1-search/Project1.html) for details

##HW2 multi-agent
ReflexAgent: 
A capable reflex agent will have to consider both food locations and ghost locations to perform well.
```
$ python pacman.py --frameTime 0 -p ReflexAgent -k 2
$ python pacman.py -p ReflexAgent -l openClassic -n 10 -q
```
MinimaxAgent: 
Write an adversarial search agent in the provided MinimaxAgent class stub in multiAgents.py
```
$ python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
```
AlphaBetaAgent: 
Make a new agent that uses alpha-beta pruning to more efficiently explore the minimax tree.
```
$ python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10
```
Expectimax: 
ExpectimaxAgent is useful for modeling probabilistic behavior of agents who may make suboptimal choices.
```
$ python pacman.py -l smallClassic -p ExpectimaxAgent -a evalFn=better -q -n 30
```

##HW3 reinforcement 
In this project, you will implement value iteration and Q-learning. You will test your agents first on Gridworld (from class), then apply them to a simulated robot controller (Crawler) and Pacman.
```
$ python gridworld.py -m
```
Value Iteration: an offline planner, not a reinforcement learning agent, and so the relevant training option is the number of iterations of value iteration it should run (option -i) in its initial planning phase.
```
$ python gridworld.py -a value -i 5
```
Q-Learning: Write a Q-learning agent, which does very little on construction, but instead learns by trial and error from interactions with the environment through its update(state, action, nextState, reward) method.
```
$ python gridworld.py -a q -k 100 
```
Q-Learning and Pacman
```
$ python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid  
```
Approximate Q-Learning: Implement an approximate Q-learning agent that learns weights for features of states, where many states might share the same features. 
```
$ python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid
```

##HW3-Bonus Ghostbusters
In this project, you will design Pacman agents that use sensors to locate and eat invisible ghosts. You'll advance from locating single, stationary ghosts to hunting packs of multiple moving ghosts with ruthless efficiency.
```
$ python busters.py -l smallHunt -p GreedyBustersAgent -n 10 --frameTime=0  
```
##Credits
This is the homework project for the course Artificial Intelligence  (2016 Fall), at National Taiwan University
Arthur: Chien-Sheng Wu
