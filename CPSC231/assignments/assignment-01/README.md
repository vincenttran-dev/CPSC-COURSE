# Assignment 1: Chart Drawing

**CPSC 231 · Fall 2026 · Due October 1, 2026**

A Python 3 program that reads a chart specification from the terminal and draws a three-column bar chart with the `SimpleGraphics` library.

## Files

| File | Description |
| --- | --- |
| [`bar_chart.py`](./bar_chart.py) | Program source |
| [`specification.pdf`](./specification.pdf) | Assignment specification |

## What the Program Does

1. Prompts for a chart title, three bar heights (in pixels), three bar colours, and the x and y coordinates of the chart's bottom-left corner.
2. Draws the x-axis (400 px) and y-axis (300 px) from that corner.
3. Draws three evenly spaced 80 px bars in the chosen colours.
4. Centres the title above the chart.

## Concepts Practised

- Reading and converting user input (`input`, `int`)
- Variables, named constants, and arithmetic for layout
- Calling functions from an external library (`line`, `rect`, `setFill`, `setFont`, `text`)

## How to Run

Place `SimpleGraphics.py` (from D2L) in this folder, then run:

```bash
python3 bar_chart.py
```

Example input:

```text
Enter the title: Sales by Quarter
Enter the value of bar 1: 150
Enter the value of bar 2: 250
Enter the value of bar 3: 200
Enter the colour of bar 1: steel blue
Enter the colour of bar 2: green
Enter the colour of bar 3: orange
Enter the x-coordinate: 100
Enter the y-coordinate: 450
```
