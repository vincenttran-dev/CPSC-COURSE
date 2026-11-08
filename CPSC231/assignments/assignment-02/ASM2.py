# Name (ID): Vincent Tran (30313622)
# Tutorial: 09

from SimpleGraphics import *

# Colors

color = ["red", "orange", "yellow", "green", "blue", "purple"]

# Chart type selection

print("Chart creation menu: \n\t 1. Pie Chart \n\t 2. Bar chart")
chart_selection = int(input("Select your chart type >> "))


# Pie chart data collect

if chart_selection == 1:
    pie_name = input("Enter the title of the chart: ")
    num_sec = int(input("Enter the number of sectors (2 to 6): "))
    pie_total = int(input("Please enter the total amount of all sectors: "))
    pie_ratio = 360 / pie_total 
 

    # Store sector names, values and angles
    sec_names = []
    sec_values = []
    sec_angles = []

    # Track the total entered so far
    entered_total = 0

    counter = 1

    # Collect data for each sector
    while counter <= num_sec:

        pie_sec_name = input(f"Label sector {counter}: ")
        sec_names.append(pie_sec_name)

        # Ask for values except for the last sector
        if counter < num_sec:
            pie_sec_value = int(input(f"Enter the value of {sec_names[counter - 1]} sector: "))
            entered_total = entered_total + pie_sec_value

        else:
            # Calculate the last sector from the remaining total
            pie_sec_value = pie_total - entered_total

        # Store the value and its angle in degrees
        sec_values.append(pie_sec_value)
        sec_angles.append(sec_values[counter - 1] * pie_ratio)

        # Move to the next sector
        counter = counter + 1

# DRAW 


    # Circle centered in the 800 x 600 window
    pie_x = 200
    pie_y = 100
    pie_size = 400

    # Title above the circle
    setColor("black")
    setFont("Arial", 14, "bold")
    text(pie_x + pie_size / 2, pie_y - 20, pie_name, "s")

    # Starting angle and sector counter
    start_angle = 0
    counter_pie = 0

    # Position and spacing of the legend
    legend_x = 720
    legend_step = pie_size / num_sec + 10
    square_size = 50

    while counter_pie < num_sec:
        # Draw the sector clockwise
        setOutline("black")
        setFill(color[counter_pie])

        pieSlice(pie_x, pie_y, pie_size, pie_size,start_angle, -sec_angles[counter_pie])

        # Starting angle for the next sector
        start_angle = start_angle - sec_angles[counter_pie]

        # Position of this legend row
        legend_y = pie_y + counter_pie * legend_step - 30

        # Sector name: font size 10, close to the square
        setColor("black")
        setFont("Arial", 10)
        text(legend_x, legend_y + 25 ,sec_names[counter_pie], "s")

        # Draw the color square for this sector
        setFill(color[counter_pie])
        rect(legend_x - square_size / 2,legend_y + 25,square_size, square_size)

        counter_pie = counter_pie + 1

    # Restore normal black text
    setColor("black")
    setFont("Arial", 10)
        


             
                     


if chart_selection == 2:

    # Collect the title, number of bars, grid interval and Y-axis label
    bar_name = input("Enter the title of the chart: ")
    num_bar = int(input("Enter the number of bars (2 to 6):"))
    grid_interval = int(input("Enter the gridline interval (10 to 100): "))
    y_axis_name = input("Enter the lable for the Y-axis:")
   

    # Store bar names and values
    bar_names = []
    bar_values = []

    counter = 1

    # Collect data for each bar
    while counter <= num_bar:

        # Read and store the bar label
        chart_bar_name = input(f"Lable bar {counter}:")
        bar_names.append(chart_bar_name)

        # Read and store the bar value
        chart_bar_value = int(input(f"Enter the value of bar {bar_names[counter - 1]}:"))
        bar_values.append(chart_bar_value)

        # Move to the next bar
        counter = counter + 1
# DRAW

    x_COR_1 = 100
    x_COR_2 = 700
    y_VALUE = 400

    num_lines = y_VALUE // grid_interval

    setFill("white")
    rect(x_COR_1, 100, 600, y_VALUE)

    setColor("black")

    # Chart title
    setFont("Arial", 14, "bold")
    text((x_COR_1 + x_COR_2) / 2, 70, bar_name, "s")

    # Y-axis label
    setFont("Arial", 12, "bold")
    text(x_COR_1 - 30, 100 + y_VALUE / 2, y_axis_name, "e")

    # Return to normal text
    setFont("Arial", 12)


    # Draw Gridlines
    counter_bar = 1

    while counter_bar <= num_lines:
        y = 500 - counter_bar * grid_interval
        line(x_COR_1, y, x_COR_2, y)
        text(x_COR_2 + 30, y, str(counter_bar * grid_interval))


        counter_bar = counter_bar + 1

    # Divide the graph into equal slots
    graph_width = x_COR_2 - x_COR_1
    slot_width = graph_width / num_bar

    # Each bar occupies 60% of its slot
    bar_width = slot_width * 0.6

    counter_bar = 0

    while counter_bar < num_bar:
    # Leave 20% of the slot before each bar
        x = x_COR_1 + counter_bar * slot_width + slot_width * 0.2

        bar_height = bar_values[counter_bar]
        y = 500 - bar_height
    
        #Draw the bar
        setFill(color[counter_bar])
        rect(x, y, bar_width, bar_height)

        # Value inside the top of the bar
        setColor("black")
        setFont("Arial", 12, "bold")
        text(x + bar_width / 2, y + 13, f"{bar_values[counter_bar]}")

            # Text below the bar
        setFont("Arial", 12)
        text(x + bar_width / 2, 515, bar_names[counter_bar])

        counter_bar = counter_bar + 1

print("Your chart is completed")
    

