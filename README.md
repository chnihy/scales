# Scales
Scales is a simple module for creation of scales for MIDI software.

It's very easy to work with
```python
import scales

cmajor = scales.Major('c')

```
Once you've created your scale object, you can get several outputs

You can get the notes of the scale...
```python
...
>>> cmajor.scale
['C', 'D', 'E', 'F', 'G', 'A', 'B']
```

Or return the corresponding Midi numbers (range can be adjusted via the .rangify() method)
```python
...
>>> cmajor.midiNums
[24, 26, 28, 29, 31, 21, 23, 36, 38, 40, 41, 
43, 33, 35, 48, 50, 52, 53, 55, 45, 47, 60, 
62, 64, 65, 67, 57, 59, 72, 74, 76, 77, 79, 69, 71]
```

You can also return a ranged scale...
```python
...
>>> cmajor.rangedScale
['C0', 'D0', 'E0', 'F0', 'G0', 'A0', 'B0', 
'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1', 
'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 
'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 
'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
```

You can return the intervals
```python
>>> cmajor.intervals
[0, 2, 4, 5, 7, 9, 11]
```

You can return the chromatic scale starting from the root of the current scale
```python
...
>>> cmajor.chromaticScale
['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
```

You can adjust the range of the scale via the .rangify() method

rangify() takes one argument: note range

Here we set the range to 8 octaves

```python
...
>>> cmajor.rangify(8)
>>> cmajor.rangedScale
['C0', 'D0', 'E0', 'F0', 'G0', 'A0', 'B0', 
'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1', 
'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 
'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 
'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 
'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 
'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6', 
'C7', 'D7', 'E7', 'F7', 'G7', 'A7', 'B7']
```

It's very simple to create your own scale, simply create a new class, subclassed from Chromatic, then set the correct scale intervals as self.intervals!
```python
...
class MyCustomScale(Chromatic):
	def __init__(self, key):
		self.intervals = [0,2,3,5,6,7] #must start with 0
		self.buildscale()
```

Currently supported scales:
```
-Chromatic
-Major
-Minor
-MelodicMinor
-MajorPentatonic
-MinorPentatonic 
```
MANY more scales/modes to come