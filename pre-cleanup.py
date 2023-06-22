import re
import io

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
        

input_text = read_input_file('src3-cleanup-01.txt')
# replace all '- ' at the beginning of a line with 'Antwort: ' but don't remove them inside the text of a line
artifact = "(^- )"
replacement = 'Antwort: '
converted_text = remove_artifacts_from_text(input_text, artifact, replacement)
write_output_file('src3-cleanup-02.txt', converted_text)