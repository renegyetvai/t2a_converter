# t2a_converter
This repository contains some scripts to convert plain text created by [chatpdf.com](https://chatpdf.com) (and saved to an .txt-file) to an anki flashcard compatible .txt file for import. 
The format of the input file is as one of the following two options:

```
Frage: [...]
Antwort: [...]
```

or 

```
Vorderseite: [...]
Rückseite: [...]
```

The "[...]" can be any text and can also contain line breaks.
The output file will be in the format described in the [anki documentation](https://docs.ankiweb.net/importing.html).
