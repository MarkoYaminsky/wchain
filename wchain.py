def wchain(word_list):
    words = sorted(word_list, key=len)
    word_chain_lengths = {word: 1 for word in words}
    word_chain_words = {word: [word] for word in words}

    for word in word_chain_lengths.keys():
        if len(word) != 1:
            for i in range(len(word)):
                current_word = word[:i] + word[i + 1:]
                if current_word in words:
                    if word_chain_lengths[current_word] + 1 > word_chain_lengths[word]:
                        word_chain_lengths[word] = word_chain_lengths[current_word] + 1
                        word_chain_words[word].extend(word_chain_words[current_word])

    maximum_chain_length = max(word_chain_lengths.values())
    biggest_word_chain = words[list(word_chain_lengths.values()).index(maximum_chain_length)]
    print(word_chain_words[biggest_word_chain])
    return maximum_chain_length
