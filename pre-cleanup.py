# Author: René Gyetvai
# Date: 2023-06-22
# License: MIT
# Description: Some text files contain artifacts that need to be removed before the text can be processed further. Therefore some functions were needed to remove these artifacts. The functions are not always needed, but useful for cleaning up the input text before processing it further with the main.py script.

import re
import io

input_file = 'assets/src1-pre.txt'
output_file = 'out/output1-pre.txt'

def remove_artifacts_from_text(text, artifact, replacement):
    # read given textfile and remove all artifacts found. An artifact is a sequence of characters that is not wanted in the text.
    occurances = re.finditer(artifact, text)
    # return the text without the artifacts
    for occurance in occurances:
        text = text.replace(occurance.group(), replacement)
    return text

    
def read_input_file(filename):
    with io.open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def write_output_file(filename, text):
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        

input_text = read_input_file(input_file)
# replace all '- ' at the beginning of a line with 'Antwort: ' but don't remove them inside the text of a line
artifact = "(^- )"
replacement = 'Antwort: '
converted_text = remove_artifacts_from_text(input_text, artifact, replacement)
write_output_file(output_file, converted_text)