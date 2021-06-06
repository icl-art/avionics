#This program takes in a music text file found in this git repo https://github.com/robsoncouto/arduino-songs
#and converts them into a list of frequencies and durations, then creates a binary file with the information.

import sys
import re
import struct

NOTE_DEFINITION = 0
TEMPO_DEFINITION = 1
IGNORE = 2

def parse(line: str):
    if len(line) != 0:
        if line[0] == "#":
            return (NOTE_DEFINITION, re.sub(r" +", " ", line).replace("#define ", "").split(" "))
        if line.startswith("int tempo"):
            return (TEMPO_DEFINITION, int(line[line.find("= ")+2:line.find(";")]))
    return (IGNORE, [])

def convert(raw: str):
    without_comments = re.sub(r"//.*", "", raw).replace("\r", "")

    note_defs = {}
    tempo = 0
    for line in without_comments.split("\n"):
        parsed = parse(line)
        if parsed[0] == NOTE_DEFINITION:
            definition = parsed[1]
            note_defs[definition[0]] = definition[1]
        elif parsed[0] == TEMPO_DEFINITION:
            tempo = parsed[1]
    
    notes = without_comments[without_comments.find("{")+1:without_comments.find("}")]
    notes = notes.replace("\n", "").replace(" ", "")
    notes = [note_defs.get(i, i) for i in notes.split(",")]
    notes = list(map(int, filter(lambda n: len(n) > 0, notes)))
    notes = [struct.pack("Hb", notes[i], notes[i+1]) for i in range(0, len(notes), 2)]
    buf = bytearray(struct.pack("B", tempo))

    for note in notes:
        buf += note
    return buf
    

if __name__ == '__main__':
    from os import listdir
    for filename in listdir("raw/"):
        with open("raw/"+filename, "r") as file:
            data = convert(file.read())

        with open("converted/"+filename, "wb") as file:
            file.write(data)