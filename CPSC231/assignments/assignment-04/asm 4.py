# Name: Vincent Tran
# Tutorial: TUT09

IN_EXTENSION = ".in"
OUT_EXTENSION = ".out"
SENTENCE_ENDINGS = ".!?"
PUNCTUATION = ".!?,;"


# Purpose: Ask the user for the input file name and make the names of the
#          input (.in) file and the output (.out) file.
# Parameters: No parameters
# Returns: in_name (str) - the name of the input file
#          out_name (str) - the name of the output file
def get_file_names():
    in_name = input("Enter the input filename: ").strip()
    cut = len(in_name) - len(IN_EXTENSION)

    # Add .in to the end if the user did not type it
    if in_name[cut:] != IN_EXTENSION:
        in_name = in_name + IN_EXTENSION
        cut = len(in_name) - len(IN_EXTENSION)

    # Take off .in and put .out on to get the output file name
    out_name = in_name[:cut] + OUT_EXTENSION
    return in_name, out_name


# Purpose: Read the input file and put the lines into paragraphs. An empty
#          line means the paragraph is over.
# Parameters: in_name (str) - the name of the input file
# Returns: paragraphs (list of str) - the text of each paragraph
def read_paragraphs(in_name):
    paragraphs = []
    para = ""
    in_file = open(in_name, "r")

    for line in in_file:
        line = line.strip()

        if line != "":
            # Add this line to the paragraph we are building
            para = para + " " + line
        elif para != "":
            # Empty line, so the paragraph is done
            paragraphs.append(para)
            para = ""

    # Add the last paragraph if the file does not end with an empty line
    if para != "":
        paragraphs.append(para)

    in_file.close()
    return paragraphs


# Purpose: Count the sentences in one paragraph by counting the . ! and ?
# Parameters: para (str) - the text of one paragraph
# Returns: count (int) - the number of sentences
def count_sentences(para):
    count = 0
    for char in para:
        if char in SENTENCE_ENDINGS:
            count = count + 1
    return count


# Purpose: Make a paragraph lowercase, change the punctuation into spaces and
#          split it into words.
# Parameters: para (str) - the text of one paragraph
# Returns: words (list of str) - the words in the paragraph
def get_words(para):
    new_text = ""

    # Copy each character, but use a space for punctuation marks
    for char in para.lower():
        if char in PUNCTUATION:
            new_text = new_text + " "
        else:
            new_text = new_text + char

    words = new_text.split()
    return words


# Purpose: Count the sentences and words in each paragraph, the total words,
#          and how many times each word shows up.
# Parameters: paragraphs (list of str) - the paragraphs from the file
# Returns: counts (list) - a [sentences, words] pair for each paragraph
#          total (int) - the number of words in the whole file
#          word_dict (dict) - each word and how many times it shows up
def count_everything(paragraphs):
    counts = []
    word_dict = {}
    total = 0

    for para in paragraphs:
        num_sentences = count_sentences(para)
        words = get_words(para)
        num_words = len(words)

        counts.append([num_sentences, num_words])
        total = total + num_words

        # Count each word (they are all lowercase already)
        for word in words:
            if word in word_dict:
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1

    return counts, total, word_dict


# Purpose: Find the highest word count and every word that has it.
# Parameters: word_dict (dict) - each word and how many times it shows up
# Returns: top_words (list of str) - the word(s) that show up the most
#          highest (int) - how many times those words show up
def find_top_words(word_dict):
    highest = 0

    # First loop: find the highest count
    for word in word_dict:
        if word_dict[word] > highest:
            highest = word_dict[word]

    # Second loop: get every word with that count (in case of a tie)
    top_words = []
    for word in word_dict:
        if word_dict[word] == highest:
            top_words.append(word)

    return top_words, highest


# Purpose: Write the report to the output file.
# Parameters: out_name (str) - the name of the output file
#             counts (list) - a [sentences, words] pair for each paragraph
#             total (int) - the number of words in the whole file
#             top_words (list of str) - the word(s) that show up the most
#             highest (int) - how many times those words show up
# Returns: No return values
def write_report(out_name, counts, total, top_words, highest):
    out_file = open(out_name, "w")

    out_file.write("# of paragraphs: " + str(len(counts)) + "\n\n")

    # Each paragraph gets its own block with an empty line after it
    para_num = 1
    for pair in counts:
        out_file.write("Paragraph " + str(para_num) + ":\n")
        out_file.write("  # of sentences: " + str(pair[0]) + "\n")
        out_file.write("  # of words: " + str(pair[1]) + "\n\n")
        para_num = para_num + 1

    out_file.write("Total # of words: " + str(total) + "\n")

    # "time" for 1, "times" for more than 1
    if highest == 1:
        time_word = "time"
    else:
        time_word = "times"

    for word in top_words:
        out_file.write('"' + word + '" occurs ' + str(highest) + " " + time_word + "\n")

    out_file.close()


# Purpose: Run the whole program.
# Parameters: No parameters
# Returns: No return values
def main():
    in_name, out_name = get_file_names()
    paragraphs = read_paragraphs(in_name)
    counts, total, word_dict = count_everything(paragraphs)
    top_words, highest = find_top_words(word_dict)
    write_report(out_name, counts, total, top_words, highest)


main()
