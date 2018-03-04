import os


def main():
    artist_name = 'eminem'
    directory = artist_name + '/'
    for filename in os.listdir(directory):
        file_type = filename[-3:]
        if file_type == 'txt':
            read_file(filename)


def read_file(filename):
    my_file = open(filename, 'r')
    for line in my_file.readlines():
        if line[1:] == '(' and line[-1:] == ')':
            continue


if __name__ == '__main__':
    main()
