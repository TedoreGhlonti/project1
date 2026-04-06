def word_counter(text):
    words = text.split()

    new_dict = {}

    for word in words:
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1
    return new_dict