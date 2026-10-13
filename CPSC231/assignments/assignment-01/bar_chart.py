# Name (ID): Vincent Tran (30313622)
# Tutorial: 09

from SimpleGraphics import *


# Collect chart information from the user

title = input("Enter the title: ")

value_1 = int(input("Enter the value of bar 1: "))
value_2 = int(input("Enter the value of bar 2: "))
value_3 = int(input("Enter the value of bar 3: "))

color_1 = input("Enter the colour of bar 1: ")
color_2 = input("Enter the colour of bar 2: ")
color_3 = input("Enter the colour of bar 3: ")

x_coo = int(input("Enter the x-coordinate: "))
y_coo = int(input("Enter the y-coordinate: "))

#State the value of the chart
CHART_WIDTH = 400
CHART_HEIGHT = 300
BAR_WIDTH = 80
BAR_GAP = 40

#Draw the axes
line(x_coo, y_coo, x_coo + CHART_WIDTH, y_coo)
line(x_coo, y_coo, x_coo, y_coo - CHART_HEIGHT)

# Calculate the x-position of each bar
bar_1_x = x_coo + BAR_GAP
bar_2_x = bar_1_x + BAR_WIDTH + BAR_GAP
bar_3_x = bar_2_x + BAR_WIDTH + BAR_GAP


# Draw bar 1
setFill(color_1)
rect(bar_1_x, y_coo - value_1, BAR_WIDTH, value_1)


# Draw bar 2
setFill(color_2)
rect(bar_2_x, y_coo - value_2, BAR_WIDTH, value_2)


# Draw bar 3
setFill(color_3)
rect(bar_3_x, y_coo - value_3, BAR_WIDTH, value_3)


# Draw the title centered above the chart

setFont("Arial", 20, "bold")

title_x = x_coo + CHART_WIDTH / 2
title_y = y_coo - CHART_HEIGHT - 20

text(title_x, title_y, title)
