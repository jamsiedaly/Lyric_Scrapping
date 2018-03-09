import os
import re
from random import randint
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import io

try:
  from pathlib import Path
except ImportError:
  from pathlib2 import Path  # python 2 backport


def main():
    artists_names = ['eminem',
                   'aesop_rock',
                   'dre',
                   'kendrick_lamar',
                   'j_cole',
                   'kanye',
                   'rakim',
                   'nas']
    directory = 'bars/'
    shuffling = 100000
    number_of_paragraphs = 0
    file = create_files(directory)
    for artist in artists_names:
        artist = artist + '/'
        text_file = artist + 'raw.txt'
        paragraphs = create_paragraphs(text_file)
        number_of_paragraphs += len(paragraphs)
        refined_paragraphs = refine_paragraphs(paragraphs)
        output = mutate_data(refined_paragraphs, shuffling)
        write_paragraphs_to_file(output, file)
    print '\nCreated a total of ' + str(number_of_paragraphs) + ' bars'
    print 'Thats a total of ' + str(number_of_paragraphs*4) + ' lines'


def create_paragraphs(filename):
    my_file = open(filename, 'r')
    paragraphs = []
    new_paragraph = []
    for line in my_file.readlines():
        if valid_line(line):
            line = line.strip()
            if line:
                new_paragraph.append(line)
            elif new_paragraph:
                paragraphs.append(new_paragraph)
                new_paragraph = []
    return paragraphs


def refine_paragraphs(paragraphs):
    bar_paragraphs = []
    new_paragraph = []
    for paragraph in paragraphs:
        if len(paragraph) % 4 == 0:
            large_paragraph = []
            for line in paragraph:
                large_paragraph.append(line)
            number_of_bars = len(large_paragraph)/4
            for i in range(number_of_bars):
                new_paragraph.append(large_paragraph[0 + i])
                new_paragraph.append(large_paragraph[1 + i])
                new_paragraph.append(large_paragraph[2 + i])
                new_paragraph.append(large_paragraph[3 + i])
                bar_paragraphs.append(new_paragraph)
                new_paragraph = []
    return bar_paragraphs


def write_paragraphs_to_file(output, file):
    newline = '\n'
    for paragraph in output:
        for line in paragraph:
            l = line + newline;
            file.writelines(unicode(l))
        file.write(unicode(newline))


def create_files(directory):
    path = Path(directory)
    if path.exists() != True:
        Path(directory).mkdir()
    output_file_name = directory + 'raw.txt'
    output_file = io.open(output_file_name, 'w', encoding='utf8')
    return output_file

def mutate_data(my_input, steps):
    input_range = len(my_input) - 1
    for i in range(steps):
        first_index = randint(0, input_range)
        second_index = randint(0, input_range)
        if first_index != second_index:
            temp = my_input[first_index]
            my_input[first_index] = my_input[second_index]
            my_input[second_index] = temp
    return my_input



def valid_line(line):
    valid = True
    expression = re.compile('.*x\d+', re.IGNORECASE)
    result = expression.search(line)
    if result is not None:
        valid = False
    if line[:1] == '(':
        valid = False
    return valid


if __name__ == '__main__':
    main()
