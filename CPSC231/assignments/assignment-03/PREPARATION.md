# Assignment 3 Preparation Guide

Study plan for CPSC 231 Fall 2026 Assignment 3: Image Manipulation.

Focus on **functions, nested loops, and SimpleGraphics image pixels**. The relevant material comes mainly from **Weeks 2, 5, 6, and 7** of [Professor James Tam's course website](https://cspages.ucalgary.ca/~tam/2026/231F/).

This is a study recommendation based on the linked lecture PDFs and example programs, checked October 26, 2026. The [original assignment PDF](./specification.pdf), [assignment description](./README.md), and D2L updates remain authoritative.

## 1. Read these five lecture files in order

Page numbers below mean **PDF pages**, not individual slide numbers. Most pages contain two slides. The links go to the instructor's original files.

| Order | Lecture file | Sections to study | Connection to Assignment 3 |
| --- | --- | --- | --- |
| 1 | [Functional decomposition, Part I](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/functional_decomposition_Part1_basics.pdf), Week 7 | Pages **7-15**: defining and calling functions, the starting function, local variables, scope, and function style. | The program must contain five specified functions, with program logic inside functions. Learn how execution moves between them. |
| 2 | [Functional decomposition, Part II](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/functional_decomposition_Part2_advanced.pdf), Week 7 | Pages **1-14**: parameters, return values, and receiving several returned values. Pages **17-20**: program planning, scope, and why globals should be avoided. Default arguments and keyword arguments are lower priority for this assignment. | Pass images, coordinates, and the user's option into functions; return filenames, RGB values, or a resulting image. Understand the difference between parameters and return values. |
| 3 | [Repetition, Part II: FOR loops](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/repetition_Part2_for_loop.pdf), Week 5 | Pages **1-4**: counting with `for`, `range()`, and the excluded stopping value. The later list exercises are outside this assignment's preparation needs. | Image coordinates begin at zero and end at one less than the width or height. Correct loop boundaries prevent skipped pixels and out-of-range coordinates. |
| 4 | [Repetition, Part III: Nesting and other looping concepts](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/repetition_Part3_nesting_other_looping_concepts.pdf), Week 6 | Pages **2-10**, especially **8-10**, which trace nested loops through image pixels. Pages **18-19** provide additional nested-loop practice. | Visit every pixel and understand how conditions can be checked inside loops. Each iteration of the outer loop runs the inner loop from beginning to end. |
| 5 | [Ben's SimpleGraphics library](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/bens_simple_graphics.pdf), Week 2 | Page **5**: coordinates. Page **9**: RGB intensity. Pages **18-26**: image formats, loading and displaying images, reading and changing pixels, copying images, and grayscale. | Learn the image operations used throughout the assignment. Focus on the image section rather than revisiting arcs and pie slices. |

If `for` loops are unfamiliar, study item 3 before item 1. If they are already comfortable, treat item 3 as a quick review.

## 2. Read and trace these example programs

These are instructor teaching examples. Read them to understand the concepts before writing your own assignment.

| Order | Example file | What to learn |
| --- | --- | --- |
| 1 | [2firstExampleFunctionV2.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/decomposition/part1_examples/2firstExampleFunctionV2.py) | How a starting function calls another function and how the initial call starts execution. The example uses `start`; Assignment 3 specifically requires `main`. |
| 2 | [1temperature_parameters_arguments_inputs.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/decomposition/part2_examples/1temperature_parameters_arguments_inputs.py) | How information passes into functions through parameters, and how local variables are used. |
| 3 | [3interest_return_values.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/decomposition/part2_examples/3interest_return_values.py) | How a function returns several values and how the caller stores them in separate variables. Especially relevant to `handleInput` and `blendPixel`. Also inspect the function comments. |
| 4 | [4changing_viewing_pixel_colors.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/simpleGraphics/workingWithImages/4changing_viewing_pixel_colors.py) | How `getPixel`, `createImage`, and `putPixel` work on a small image before introducing loops. |
| 5 | [5copying_all_pixels_MODIFIED.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/repetition/part3_examples/5copying_all_pixels_MODIFIED.py) | How nested loops visit coordinates. The active example prints coordinates for a small image, making the traversal easier to trace. |
| 6 | [5copying_all_pixels.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/simpleGraphics/workingWithImages/5copying_all_pixels.py) | How nested loops read every source pixel and write it into a destination image. This is the closest foundational example to the image-processing work in Assignment 3. |
| 7 | [6making_grey_scale_images.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/simpleGraphics/workingWithImages/6making_grey_scale_images.py) | How arithmetic changes pixel colours. This example averages RGB channels within one pixel. Assignment 3 instead blends corresponding channels from two images. |

To run these examples, use the associated images from the [image examples folder](https://cspages.ucalgary.ca/~tam/2026/231F/examples/simpleGraphics/workingWithImages/) or [nested-loop examples folder](https://cspages.ucalgary.ca/~tam/2026/231F/examples/repetition/part3_examples/), as appropriate. Obtain the course's `SimpleGraphics.py` from D2L and follow the instructor's setup instructions.

## 3. Review these only if needed

| Topic | File and pages | When to review |
| --- | --- | --- |
| Repeated input validation | [Repetition, Part I: WHILE basics](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/repetition_Part1_while_basics.pdf), pages **3-8** | If you cannot yet keep asking until the user enters a permitted menu choice. |
| Boolean expressions and branching | [Branching, Part II](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/branching_Part2.pdf), pages **5-12** | If compound conditions or the difference between separate `if` statements and an `if/elif/else` chain are unclear. |
| Several returned values | [Functional decomposition, Part II](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/functional_decomposition_Part2_advanced.pdf), especially page **9** | If you can return a single value but cannot yet receive three values from a function. |

Lists, dictionaries, sets, general text-file input/output, classes, and recursion can be postponed when preparing specifically for Assignment 3. Image loading is handled through SimpleGraphics. The multiple-value return syntax needed here is already introduced in the functions material.

## 4. Connect the concepts to the required functions

| Required function | Inputs and results required by the specification | Main concepts to understand |
| --- | --- | --- |
| `handleInput` | No parameters; returns two image filenames and the combination option. | `input`, integer conversion, validation with a loop, and receiving several returned values. |
| `blendPixel` | Takes two images and coordinates `x` and `y`; returns the resulting red, green, and blue values. | Parameters, `getPixel`, channel arithmetic, and returning three values. |
| `combineAll` | Takes two images; returns the fully combined image. Must use `blendPixel`. | Creating an output image, nested loops, helper-function calls, and `putPixel`. |
| `combineParts` | Takes two images and the option; returns the partially combined image. Must use `blendPixel`. | Nested loops, coordinate comparisons, branching, and an exactly 100-pixel blend strip. |
| `main` | Performs the high-level work, including loading and drawing images and calling the appropriate functions. | Execution order, capturing returned values, local variables, and resizing the output window. |

Know the purpose and arguments of these SimpleGraphics functions: `loadImage`, `drawImage`, `createImage`, `getWidth`, `getHeight`, `getPixel`, `putPixel`, and `resize`. Their descriptions are provided in the [assignment's useful-functions section](./README.md#useful-functions).

## 5. Keep the assignment's restrictions in mind

- Use the five required function names and their specified parameters and return values. Do not define a function inside another function.
- Put program logic and variables inside functions. Outside them, only imports, constants, and the call to `main` are permitted.
- Use only the SimpleGraphics library. **Do not use lists.**
- Using global variables, using `break` or `continue`, or having more than one `return` statement in a function may each result in a **30-mark deduction**. Global constants are allowed.
- Document every function's purpose, all parameters, and its return values. Explicitly state when there are no parameters or no return values.
- Use actual GIF images. The specification allows you to assume the two files exist in the program's folder, have identical dimensions, and that the menu input is an integer. You still need to validate that the menu choice is between 1 and 3.
- The partial blend strip must be exactly **100 pixels** tall or wide, and the output window must match the original image dimensions.

Some teaching examples demonstrate constructs that this assignment restricts. Apply the assignment's rules when writing your own program.

## 6. Check your understanding before coding

- [ ] I can define a function, call it, and explain when its body executes.
- [ ] I can explain the difference between passing a value in, returning a value, and printing a value.
- [ ] I can receive three returned values in separate variables.
- [ ] I can explain why a local variable is not automatically available inside another function.
- [ ] I can trace the coordinates visited by two nested loops on a small image.
- [ ] I know that x increases to the right and y increases downward.
- [ ] I can explain how reading and writing pixels changes an image.
- [ ] I can validate a menu choice without `break` or `continue`.
- [ ] I can describe each required function's job, parameters, and results before implementing it.

## Sources

- [Assignment 3 specification](./specification.pdf) and its [GitHub-readable description](./README.md).
- [CPSC 231 Fall 2026 course website and weekly schedule](https://cspages.ucalgary.ca/~tam/2026/231F/).
- [Official course outline linked from the course website](https://cspages.ucalgary.ca/~tam/2026/231F/CPSC_231_fall_2026_outline.pdf).
- The instructor lecture PDFs and example programs linked above.

Preparation guide compiled with AI assistance. The recommendations are explanatory study notes; follow the original course materials and D2L for official requirements.
