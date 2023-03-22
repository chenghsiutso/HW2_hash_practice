# count how many time each word in the input file appear by using hash or dictionary
input_file = open("hw2_data.txt")

# decalre dictionary variable
word_count_dict = {}

# calcaulte maximum word length for text formatting
max_word_length = 0

# read each line in the input file
for line in input_file.readlines():
    # remove ending newline character
    word = line.strip()

    # put the word in the dictionary if it does not exist in the dictionary yet
    if word not in word_count_dict:
        word_count_dict[word] = 0

    # increment the count of the word
    word_count_dict[word] += 1

    # assign the length of the word to current maximum word length variable if it is greater
    if len(word) > max_word_length:
        max_word_length = len(word)

separator = '+' + ('-'*max_word_length + '+') * len(word_count_dict)

header = "|"
word_counter = "|"
word_count_list = []
# print the word and count by descending order of word count
for word in sorted(word_count_dict, key=word_count_dict.get, reverse=True):
    header += word.ljust(max_word_length) + "|"
    word_counter += ("(" + str(word_count_dict[word]) + ")").ljust(max_word_length) + "|"
    word_count_list.append(word_count_dict[word])

# print the count of each word by using Chinese counting symbol for programming practicing
word_count_mark = ""
while True:
    word_count_mark += '1'
    for i in range(len(word_count_list)):
        if word_count_list[i] > 0:
            word_count_mark += "____".ljust(max_word_length) + '|'
        else:
            word_count_mark += ' '*max_word_length + '|'
    word_count_mark += '\n|'

    for i in range(len(word_count_list)):
        if word_count_list[i] > 2:
            word_count_mark += "  |_".ljust(max_word_length) + "|"
        elif word_count_list[i] > 1:
            word_count_mark += "  | ".ljust(max_word_length) + '1'
        else:
            word_count_mark += ' '*max_word_length + '|'
    word_count_mark += '\n|'

    for i in range(len(word_count_list)):
        if word_count_list[i] > 4:
            word_count_mark += "|_|_".ljust(max_word_length) + '|'
        elif word_count_list[i] > 3:
            word_count_mark += "| | ".ljust(max_word_length) + '|'
        elif word_count_list[i] > 2:
            word_count_mark += "  | ".ljust(max_word_length) + '|'
        elif word_count_list[i] > 1:
             word_count_mark += "  |".ljust(max_word_length) + '|'
        else:
            word_count_mark += ' '*max_word_length + '|'

        # decrement by 5 since a whole Chinese counting symbol contains 5 strokes
        word_count_list[i] -= 5

    # finish printing Chinese counting symbol if the biggest word count is less than or equal to 0
    # after decrementing by 5
    if word_count_list[0] <= 0:
        break

    word_count_mark += '\n'

print(separator)
print(header)
print(word_counter)
print(separator)
print(word_count_mark)
print(separator)
