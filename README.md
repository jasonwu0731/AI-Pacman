#Artificial Intelligence Fall 2016
YU, TIAN-LI AI course

> In this project, Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. Try to build general search algorithms and apply them to Pacman scenarios.

Start a game by the command:
```
python pacman.py
```
You can see the list of all options and their default values via:
```
python pacman.py -h
```

##HW1
DFS, BFS, UCS, ASTAR
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
python pacman.py -l bigMaze -p SearchAgent -a fn=ucs
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
Corner problem, Corner: Heuristic
```
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
> Note: AStarCornersAgent is a shortcut for -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic.

Eating all the dots
```
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```


