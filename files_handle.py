def read_in():
    words = []
    with open("wchain.in", "r") as file:
        amount_of_words = int(file.readline())
        for line in range(amount_of_words):
            words.append(file.readline().strip())
    return words


def write_out(answer):
    with open("wchain.out", "w") as file:
        file.write(str(answer))
