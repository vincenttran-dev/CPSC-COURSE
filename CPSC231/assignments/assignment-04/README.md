# Assignment 4 · Text Analysis

**CPSC 231, Fall 2026** · **Due Thursday, November 26 at 23:59** · **15% of the course grade**

[Original assignment PDF](./specification.pdf) · [What to study before coding](./PREPARATION.md) · [Assignment index](../README.md)

## What the program produces

Write a Python 3 program that prompts once for a text file, analyzes it, and writes a report. For example, entering either `poem` or `poem.in` reads `poem.in` and creates `poem.out`. The assignment allows you to assume the user enters a valid name.

| Unit | What to count |
| --- | --- |
| Whole file | Number of paragraphs, total number of words, and every word tied for the highest frequency |
| Each paragraph, in order | Number of sentences and number of words |
| Each most frequent word | Print the word and its frequency using `1 time` or `2 times`, as appropriate |

Each paragraph ends with an empty line containing no spaces. A paragraph can span several lines. The text contains at least one word. The only punctuation marks are periods, exclamation marks, question marks, commas and semicolons. The first three can end a sentence. Count numbers as words. The input excludes numbers containing decimal points or grouping commas. Ignore case when counting repeated words.

Use the report layout on **page 3 of the PDF** and the additional sample pairs in **D2L → Assignments**. Match the labels, indentation, blank lines, and quotation marks. The handout allows singular or plural for the paragraph, sentence and word count labels. It specifically requires the correct `time` or `times` for frequency lines.

### Check against the Raven example

| Paragraph | Sentences | Words |
| --- | ---: | ---: |
| 1 | 1 | 11 |
| 2 | 2 | 31 |
| 3 | 1 | 15 |

The report opens with **3 paragraphs** and gives **57 words** overall. The three frequency lines report **a**, **i** and **and**, each occurring **3 times**.

## Marking and implementation requirements

| Component | Marks | What is assessed |
| --- | ---: | --- |
| Program | 125 | Required calculations, file handling, report layout, comments and style |
| TA test cases | 75 | How closely the generated output matches the expected reports on additional inputs |
| Tutorial demo | 30 | Your answers to questions about your own program |
| Total | 230 | |

- Start the program by calling the main function. Keep executable program logic inside functions and define each function at the top level. Global constants are allowed.
- Use only material covered in lectures and tutorials. Use appropriate conditions, loops and functions. The handout prohibits libraries.
- The handout lists four possible **30-mark deductions**. They concern material outside the course, global variables, `break` or `continue`, and more than one `return` in a function.
- Open and close both files properly. Match the output format in the examples.
- Include names, IDs and tutorial number at the top. For pair work, also record each partner’s approximate percentage. Document the purpose, parameters and returns of every function, including when it has no parameters or returns no value. Add inline comments where the logic needs explanation.

## Submission and rewards

Submit **one Python file** through the D2L dropbox. Students working in pairs must register in and attend the same tutorial. One partner submits and enters both names and IDs in the D2L comment box. The demo starts with the first tutorial after the deadline and continues as scheduled by the TA.

- **Early submission.** A final submission by **Wednesday, November 25 at 23:59** qualifies for 5 reward points.
- **Late submission.** The penalty is 10 marks per day, with a day as the smallest unit. Work more than two days late is not accepted. Ten reward points remove one day’s penalty, up to 20 points for two days.
- **Partner reward.** Each partner can earn up to 5 reward points. For each student, divide their share of the work by the larger partner share, multiply by 5, and round down. A 40/60 split gives 3 and 5 points. The percentages must appear in the program header.

The handout requires students to disclose assistance and to submit their own work. It prohibits viewing or exchanging other students’ solutions. Check D2L for amendments and your TA’s demo arrangements.
