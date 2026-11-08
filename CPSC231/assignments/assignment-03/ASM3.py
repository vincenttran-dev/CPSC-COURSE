
# Name (ID): Vincent Tran (30313622)
# Tutorial: 09


from SimpleGraphics import *

BLEND_SIZE = 100

# Purpose: Display the menu and read a choice.
# Parameters: None.
# Returns: The user's integer choice.
def option():
    print("1 - combine two whole images")
    print("2 - blend horizontally")
    print("3 - blend vertically")
    choice = int(input(">> "))
    return choice


# Purpose: Keep asking until the choice is valid.
# Parameters: choice - the integer choice to check.
# Returns: A valid choice from 1 to 3.
def invalid_choice(choice):
    while choice not in (1, 2, 3):
        print("Please enter 1, 2, or 3:")
        choice = option()
    return choice


# Purpose: Collect two GIF filenames and a valid blending choice.
# Parameters: None.
# Returns: The first filename, second filename, and valid choice.
def handleInput():
    first_image_name = input("Enter the name of the first image: ")
    second_image_name = input("Enter the name of the second image: ")

    print("\nChoose one of the following options:")
    choice = option()
    choice = invalid_choice(choice)
    return first_image_name, second_image_name, choice


# Purpose: Blend two pixels at the same coordinates.
# Parameters: 1. first_image, second_image: the two loaded images.
#             2. x, y: the coordinates of the pixels to blend.
# Returns: The blended red, green, and blue values.
def blendPixel(first_image, second_image, x, y):
    red_1, green_1, blue_1 = getPixel(first_image, x, y)
    red_2, green_2, blue_2 = getPixel(second_image, x, y)

    red = (red_1 + red_2) // 2
    green = (green_1 + green_2) // 2
    blue = (blue_1 + blue_2) // 2

    return red, green, blue


# Purpose: Blend two whole images.
# Parameters: first_image, second_image
# Returns: A new image containing the blended pixels.
def combineAll(first_image, second_image):
    width = getWidth(first_image)
    height = getHeight(first_image)

    result_image = createImage(width, height)

    for y in range(height):
        for x in range(width):
            red, green, blue = blendPixel(first_image, second_image, x, y)
            putPixel(result_image, x, y, red, green, blue)

    return result_image



# Purpose: Combine two images with a central 100-pixel blended strip.
# Parameters: first_image, second_image: two loaded images of the same size.
#             blend_style: 2 for horizontal or 3 for vertical.
# Returns: The partially blended image.
def combineParts(first_image, second_image, blend_style):
    width = getWidth(first_image)
    height = getHeight(first_image)

    result_image = createImage(width, height)

    if blend_style == 2:
        blend_start = (height - BLEND_SIZE) // 2
    else:
        blend_start = (width - BLEND_SIZE) // 2

    blend_end = blend_start + BLEND_SIZE

    for y in range(height):
        for x in range(width):
            if blend_style == 2:
                position = y
            else:
                position = x

            if position < blend_start:
                red, green, blue = getPixel(first_image, x, y)
            elif position < blend_end:
                red, green, blue = blendPixel(first_image, second_image, x, y)
            else:
                red, green, blue = getPixel(second_image, x, y)

            putPixel(result_image, x, y, red, green, blue)

    return result_image



# Purpose: 1. Get user input, load two images, call the selected combination
#          2. function, resize the window, and display the resulting image.
# Parameters: None.
# Returns: None.
def main():
    first_image_name, second_image_name, blend_style = handleInput()

    first_image = loadImage(first_image_name)
    second_image = loadImage(second_image_name)

    if blend_style == 1:
        result_image = combineAll(first_image, second_image)
        

    elif blend_style == 2 or blend_style == 3:
        result_image = combineParts(first_image, second_image, blend_style)
        
    resize(getWidth(result_image), getHeight(result_image))
    drawImage(result_image, 0, 0)
       
    
  
main()
