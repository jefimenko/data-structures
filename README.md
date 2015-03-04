# data-structures
Code Fellows Dev Accelerator: This repository will be for implementations of classic data structures in python.

[![Travis](https://travis-ci.org/jefimenko/data-structures.svg?branch=wtd_graph)](https://travis-ci.org/jefimenko/data-structures.svg?branch=wtd_graph)


parens.py:
Includes a function balanceness() that takes string and determines if it is 'open', 'balanced', or 'broken', depending on the sequence of parenthesis contained. 'Open', 'balanced', and 'broken' are respectively determined as more leading '('s than ')'s, equal number of leading '(' and ')', and any sequence including ')' that do not have a preceding '('. 'Open' strings are represented by returning a 1, 'balanced' by 0, and 'broken' by -1, with an emptry string being considered 'balanced'.

Shortest-path algorithms:
Making a decision regarding which algorithm to use to implement finding the 'shortest-path' between two vertices in a graph will probably be motivated by the nature of the use. For problems where edges represent either a cost, difficulty or some other deterrent of 'traveling' from one node to another, location or some state, then Djikstra's algorithm or some other which simply minimize the total weight of a single path, will do just fine. However, if perhaps you are interested in knowing the 'shortest-path' between all points, then perhaps the Floyd-Warshall would be more appropriate, or if speed of determination of path was important, than maybe yet another algorithm would be more appropriate.