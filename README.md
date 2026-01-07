# TSP Explorer
## Demo
🎥 Video walkthrough and execution demo:  
https://youtu.be/JwmGNzn1d6g

TSP Explorer is an interactive game and AI-based simulation built around the
Travelling Salesman Problem (TSP), a classic combinatorial optimization problem
in computer science.

## Problem Overview
The Travelling Salesman Problem aims to find the shortest possible route that
visits a set of cities exactly once and returns to the starting point. Despite its
simple definition, TSP is an NP-hard problem, meaning it becomes computationally
intractable as the number of cities increases.

This problem appears in real-world applications such as:
- Logistics and delivery route planning
- Network and data transmission optimization
- Manufacturing and tool-path optimization

## Project Description
This project implements **TSP Explorer**, a game where a human player competes
against an AI agent to solve the Travelling Salesman Problem.

- The **player** manually selects a route that visits all cities.
- The **AI agent** computes its route using a **greedy nearest-neighbour
  heuristic**.
- Both routes are evaluated and compared based on total distance.
- The shortest route wins.

The project demonstrates how heuristic algorithms can efficiently approximate
solutions to complex optimization problems.

## AI Agent Classification
The AI agent used in TSP Explorer can be classified as:
- **Optimization-focused agent** – designed to minimise total route distance
- **Goal-based agent** – its objective is to find the shortest possible tour
- **Reactive agent** – makes decisions based on the current state by selecting
  the nearest unvisited city without long-term planning

## Technologies Used
- Programming Language: Python
- Algorithm: Greedy Nearest-Neighbour Heuristic
- Concepts: Combinatorial Optimization, NP-hard Problems, Heuristic Algorithms

## How to Run
1. Clone the repository
2. Compile/run the main file according to the language used


## Author
Basani Milondzo
