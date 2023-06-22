# Author: René Gyetvai
# Date: 2023-06-22
# License: MIT
# Description: Converts a text file with questions and answers to a text file formatted for importing into Anki.

import re
import io

input_file = 'assets/src1.txt'
output_file = 'out/output1.txt'

def convert_text(input_text):
    questions = re.findall(r'Frage: (.*?)\nAntwort: (.*?)\n', input_text, re.DOTALL)
    questions += re.findall(r'Vorderseite: (.*?)\nRückseite: (.*?)\n', input_text, re.DOTALL)
    output = []
    for q, a in questions:
        output.append(q + ';"' + a.replace('"', '""') + '"')
    return '\n'.join(output)

def read_input_file(filename):
    with io.open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_output_file(filename, text):
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

input_text = read_input_file(input_file)
converted_text = convert_text(input_text)
write_output_file(output_file, converted_text)
