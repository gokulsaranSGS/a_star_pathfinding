# a_star_pathfinding
A Python implementation of the A* Pathfinding algorithm with Pygame visualization.

# A* Pathfinding Visualization with Pygame

This project is a Python implementation of the A* Pathfinding algorithm visualized using Pygame. It allows you to interactively set up barriers, start, and end points on a grid and visualize the shortest path calculated using the A* algorithm.

---

## Features
- **Interactive Grid**: Click to set the start, end, and barrier nodes.
- **A* Algorithm**: Visualizes the step-by-step pathfinding process.
- **Keyboard Controls**:
  - `SPACE`: Start the pathfinding.
  - `C`: Clear the grid.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <https://github.com/gokulsaranSGS/a_star_pathfinding.git>
   cd a_star_pathfinding
2. Install the required dependencies
	pip install pygame
3. Run the Script
	python main.py
How It Works
Node States:

Start Node: Orange
End Node: Turquoise
Barrier Node: Black
Open Node: Green
Closed Node: Red
Path Node: Purple
Algorithm Steps:

The grid is traversed using the A* heuristic.
The shortest path is visualized step by step.


