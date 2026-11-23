# What to study for Assignment 4

Start with **file input/output**, then **strings**, then **dictionaries**. Together they cover how the text enters the program, how to identify sentences and words, and how to find the most frequent words across the entire file. The page numbers below are **PDF viewer pages**. Most of the handouts show two slides per page.

[Assignment requirements](./README.md) · [Original assignment PDF](./specification.pdf) · [James Tam’s Fall 2026 course schedule](https://cspages.ucalgary.ca/~tam/2026/231F/)

## Read these three files first

| Priority | Lecture and PDF pages | What to look for | Where it matters in A4 |
| --- | --- | --- | --- |
| 1 | [Week 9 · file_input_output.pdf, pp. 5–6](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/file_input_output.pdf#page=5), [pp. 8–9](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/file_input_output.pdf#page=8), [pp. 11–13](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/file_input_output.pdf#page=11) and [p. 17](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/file_input_output.pdf#page=17) | Reading lines, recognizing newlines and end-of-file, opening in write mode, adding line breaks, closing files | Read the `.in` file, preserve paragraph boundaries and produce a fresh `.out` report each run. |
| 2 | [Week 8 · composites_strings.pdf, pp. 7–9](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/composites_strings.pdf#page=7) and [pp. 11–13](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/composites_strings.pdf#page=11) | Slicing, splitting on whitespace, case conversion, stripping characters and counting occurrences | Recognize the filename suffix, identify words, group spelling variants such as `Apple` and `apple`, and count sentence endings. |
| 3 | [Week 8 · composites_dictionaries.pdf, pp. 3–6](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/composites_dictionaries.pdf#page=3) | Creating entries, looking up and updating a value, testing membership, iterating through keys, values and items | A normalized word is a key and its occurrence count is the value. The finished dictionary gives you the information to report every tie. |

## Which example should I open?

| When you want to understand… | Instructor example | What to trace |
| --- | --- | --- |
| How Python sees the input | [2file_input_simple_read.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/file_basics/2file_input_simple_read.py) | Compare the single `readline()` with the later loop over the file. A paragraph can contain several nonempty lines. |
| Why a blank line matters | [3string_strip_methods.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/file_basics/3string_strip_methods.py) and [5file_read_while_implementation.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/file_basics/5file_read_while_implementation.py) | A raw empty separator line reads as `"\n"`. At end-of-file, `readline()` returns `""`. Stripping first makes both look empty. |
| How to separate the name and extension | [1string_slicing.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/composites/composites_strings/1string_slicing.py) | Study which characters a slice includes. Both `story` and `story.in` should lead to the same input and output names. |
| How to get words from text | [2string_spliting.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/composites/composites_strings/2string_spliting.py) and [4string_modification_functions.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/composites/composites_strings/4string_modification_functions.py) | The splitting example knows its number of fields in advance. A4 paragraphs can contain any number of words. String methods return a new string. |
| How to distinguish sentence and word counts | [5inspection_methods.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/composites/composites_strings/5inspection_methods.py) | The example counts occurrences of a substring. In A4, only `.`, `?` and `!` end sentences. Identify these before discarding punctuation from words. |
| How to track new words and repeated words | [2creating_modifying_elements.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/composites/composites_dictionaries/2creating_modifying_elements.py) | Trace the membership check, creation of a key, and change to an existing value. Follow what happens on a word’s first and second appearances. |
| How to find every tie | [4iterating_dictionaries.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/composites/composites_dictionaries/4iterating_dictionaries.py) | The example traverses keys, values and items. First identify the highest count, then look for every word with that count. |
| How the final report gets written | [1file_output_basics.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/file_output/1file_output_basics.py) and [4file_repeated_file_input_output.py](https://cspages.ucalgary.ca/~tam/2026/231F/examples/file_output/4file_repeated_file_input_output.py) | Look at write mode, explicit newlines and the two file handles. The second example numbers individual lines. A4 numbers paragraphs. |

## Earlier material to revisit if you get stuck

- **Best practice exercise.** Week 7, Part II, PDF p. 21, slide 41, Exercise 7 asks for a function that counts the words in one sentence. Slide 42 on the same page asks you to find the largest value and the mode of a list. The mode is the most frequent value. A4 extends this idea by requiring every word tied for the highest count. [functional_decomposition_Part2_advanced.pdf, p. 21](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/functional_decomposition_Part2_advanced.pdf#page=21)
- **Functions and scope.** Use the same idea as Assignment 3’s image functions. Give a function a specific job and decide which information it receives and returns. Review the main entry point, local variables and single-purpose functions in Part I, pp. 9–15. Look at parameter passing and return values in Part II, pp. 2–3 and 8–14. [Part I](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/functional_decomposition_Part1_basics.pdf#page=9) · [Part II](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/functional_decomposition_Part2_advanced.pdf#page=8)
- **Loops and conditions.** If scanning text character by character feels unfamiliar, Week 5, Part II, pp. 6–7 shows iteration over a string. Week 4, Part II, pp. 21–22 covers membership tests, useful for identifying punctuation. [Loop notes](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/repetition_Part2_for_loop.pdf#page=6) · [Character loop example](https://cspages.ucalgary.ca/~tam/2026/231F/examples/repetition/part2_examples/4for_iterating_string.py.py) · [Branching notes](https://cspages.ucalgary.ca/~tam/2026/231F/notes/acrobat/branching_Part2.pdf#page=21)

For this assignment, graphics, number representations, object-oriented programming and recursion can wait. The handout allows you to assume valid filenames, so the Week 9 exceptions lesson is a lower priority.

## Check your understanding before the TA tests

1. **Line versus paragraph.** Picture a paragraph spanning three nonempty lines with one period on its final line. Its report should show one paragraph and one sentence. An ordinary line break between two words still separates the words.
2. **Paragraph counts versus file counts.** When a paragraph ends, its sentence and word counts are complete. A word seen in two different paragraphs contributes twice to the same file-wide frequency.
3. **Punctuation and numbers.** For `Wait, wait; room 211!`, expect one sentence, four words and two appearances of `wait`. A digits-only word still counts.
4. **Ties and singular wording.** For `Red blue.` as a complete one-paragraph input, both words tie. Each needs its own frequency line with `1 time`.
5. **Output format and reruns.** Compare your generated report with the D2L sample in a plain text editor. Check spaces, blank lines, quotes and the total. Run the same input again. The output should still contain one report.

The Raven sample gives a final cross-check on [page 3 of the assignment](./specification.pdf#page=3). The additional official input/output pairs are in D2L under Assignments.
