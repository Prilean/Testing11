def backward_string_by_word(word):
    split_word = word.split()
    reverse_word = ""
    for i in split_word:
        reverse_word += i[::-1]
        reverse_word += " "
    else:
        return reverse_word

print(backward_string_by_word("hello world"))

