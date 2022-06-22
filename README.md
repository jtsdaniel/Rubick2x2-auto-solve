# Rubick2x2-auto-solver-system

***Description:*** The project focuses on building a system that can figure out how many moves needed to solve a mixed 2x2Rubick, or shortest way to solve a mixed rubick. The project used [breadth first search](https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/) algorithm to solve the problem. The project is for my learning purpose of more understanding in algorithm and complexity

## Installation guide:

1. Install python to vscode - [follow this guide](https://code.visualstudio.com/docs/python/python-tutorial)
2. Clone the repo into your local machine
```bash
git clone https://github.com/jtsdaniel/Rubick2x2-auto-solve.git
```

## User guide:
1. For a valid input of mixed Rubick you should go to this [website](https://www.grubiks.com/puzzles/rubiks-mini-cube-2x2x2/) to generate a mixed Rubick by yourself. Then encode it into a string list of characters (have a look in [Instance Model section](https://github.com/jtsdaniel/Rubick2x2-auto-solve/blob/master/Report.pdf) in the report file.)
2. Then you can change *testData* variable in ***Rubick2x2Solve.py*** file:
```python
testData = (
    "G", "G", "W", "O",
    "Y", "G", "O", "Y",
    "R", "Y", "W", "G",
    "R", "W", "W", "O",
    "O", "B", "B", "B",
    "R", "Y", "B", "R")
```
3. Start debugging (F5) you can see the number of moves needed to solve the mixed Rubick:

```
Solving this cube...
   GG   
   OW   
OB YG RY RW
BB YO GW OW
   RY
   RB
Number of moves made to solve the cube:
6
```

Please follow instruction in this [report](https://github.com/jtsdaniel/Rubick2x2-auto-solve/blob/master/Report.pdf) to understand more about valid input and algorithm analysis
