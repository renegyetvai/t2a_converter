import re
import io

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

input_text = read_input_file('assets/src4.txt')
converted_text = convert_text(input_text)
write_output_file('output4.txt', converted_text)
