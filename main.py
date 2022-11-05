from files_handle import read_in, write_out
from wchain import wchain

if __name__ == '__main__':
    words = read_in()
    result = wchain(words)
    write_out(result)
