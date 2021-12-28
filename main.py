import numpy

pianoKeyFrequencies = {}
print('Please type pitch:')
pitch = abs(int(input()))


def createKeyFrequenciesDictionary():
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    octave = 0
    frequencies = calculateFrequencies()
    i = 1
    while i <= 88:
        note = notes[(i % 12) - 1]
        if note == "C":
            octave += 1
        note += str(octave)
        pianoKeyFrequencies[note] = str(frequencies[i - 1]) + " Hz"
        i += 1


def calculateFrequencies():
    frequencies = [0] * 88
    frequencies[48] = pitch

    i = 49
    while i < 88:
        frequencies[i] = frequencies[i - 1] * numpy.power(2, 1 / 12)
        i += 1

    i = 47
    while i >= 0:
        frequencies[i] = frequencies[i + 1] / numpy.power(2, 1 / 12)
        i -= 1

    return frequencies


createKeyFrequenciesDictionary()
keyNames = pianoKeyFrequencies.keys()

for keyName in keyNames:
    print(keyName + ': ' + pianoKeyFrequencies[keyName])
