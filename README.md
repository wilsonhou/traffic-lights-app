# Traffic Lights App for Pathfinder

This app consists of 2 components:

- A script for parsing HSC syllabus files into CSV format, and
- A graphical web application for visualising and tracking traffic lights

## Syllabus to JSON Script

The script accepts a syllabus file in text format (.txt) and parses said text file.

#### Planned Steps:

In version 1, CSV may be skipped in favour of JSON.

- Copy Syllabus file into .txt document with some manual formatting
- Convert Syllabus into CSV file
- Read CSV file and convert into JSON for web application consumption

#### Format of CSV

Chemistry syllabus used as first test.

1. Big Modules Content _(e.g: Module 3: Reactive Chemistry)_
2. Smaller Topics _(e.g: Predicting Reactions of Metals)_
3. Specific Dot Points _(e.g: conduct practical ... in:)_

#### How to Mark Up A Syllabus:

Use the following signs to indicate beginning and end of content types:

- Big Modules Content: &&&
- Smaller Topics: ???
- Dot Point: \*\*\*

For example:

---

&&&
Module 1
???
Predicting Reactions of Metals:
\*\*\*

- Conduct Practical Investigations into...

\*\*\*
???
&&&

---

## Web Application

Building in process - more to come.

_Click image for a concept preview:_

[![Concept Preview](./current-concept.png)](https://drive.google.com/file/d/1Qg6NkmXbJBD62tex6Ju0b7NDtOok31_g/view?usp=sharing)

## Known Issues

- Currently script requires manual marking up of data to separate modules, sections and content. May be automated at a future date.
