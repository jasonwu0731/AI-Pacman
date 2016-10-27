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
DFS, BFS, UCS, A*, A* heuristic 
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
python pacman.py -l bigMaze -p SearchAgent -a fn=ucs
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
Corner problem, Corner heuristic
```
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

Eating all the dots
```
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```


