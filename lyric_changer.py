import re


def main():
    artist_name = 'eminem'
    directory = artist_name + '/'
    text_file = directory + 'raw.txt'
    paragraphs = create_paragraphs(text_file)
    refined_paragraphs = refine_paragraphs(paragraphs)
    print paragraphs[5]


def create_paragraphs(filename):
    my_file = open(filename, 'r')
    paragraph_count = 0
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
    print 'nice'



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
