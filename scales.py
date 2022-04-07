class Scale():
	def __init__(self, key):
		self.key = key.upper()
		self.allNotes = ["A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab",
						"A#","B","C","C#","D","D#","E","F","F#","G","G#"]

		# raw chromatic note sets
		flatsRawScale = ["A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab"]
		sharpsRawScale = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
		
		# Flats key or Sharp Key?
		if self.key in flatsRawScale:
			self.flatsOrSharps = "flats"
			self.rawscale = flatsRawScale
		if self.key in sharpsRawScale:
			self.flatsOrSharps = "sharps"
			self.rawscale = sharpsRawScale

		
	
	# Rangify adds a range note onto each note of the scale
	# ex: C4, D4, E4, F4 etc...
	def rangify(self, scaleRange):
		self.rangedScale = [] #clearing
		for r in range(scaleRange):
			for i in range(len(self.scale)):
				self.rangedScale.append(self.scale[i] + str(r))

	def assignMidiNums(self):
		lowestMidiNums = {"sharps":
							{'A': 21, 'A#': 22, 'B': 23, 
							'C': 24, 'C#': 25, 'D': 26, 
							'D#': 27, 'E': 28, 'F': 29, 
							'F#': 30, 'G': 31, 'G#': 32},
						"flats":{
							'A': 21, 'Bb': 22, 'B': 23, 
							'C': 24, 'Db': 25, 'D': 26, 
							'Eb': 27, 'E': 28, 'F': 29, 
							'Gb': 30, 'G': 31, 'Ab': 32}
						}
		
		# midiNumsDict is a little redundant, but easier to read for humans
		# ex: {"A1":21, "A#1":22, etc...
		self.midiNumsDict = {}
		for n in range(len(self.rangedScale)):
			note = self.rangedScale[n]
			theNote = note[:-1]
			theRange = note[-1]
			lowestMidiNumForNote = lowestMidiNums[self.flatsOrSharps][theNote]
			self.midiNumsDict[note] = lowestMidiNumForNote + (int(theRange) * 12)
		
		# Just the midi nums
		self.midiNums = list(self.midiNumsDict.values())

	# Build method to be inherited by all children scales
	def buildScale(self, range=5):
		self.scale = [self.scale[interval] for interval in self.intervals]
		self.rangify(range)
		self.assignMidiNums()


# Every class inherits from Chromatic
class Chromatic(Scale):
	def __init__(self,key):
		super().__init__(key)
		keyIndex = self.rawscale.index(self.key)
		offset = 0
		self.scale = []
		
		# Chromatic class sets the order of its inherited rawscale 
		# All children inherit <scale> from the Chromtic <scale>
		for i in range(len(self.rawscale)):
			try:
				self.scale.append(self.rawscale[keyIndex + i])
			except IndexError:
				self.scale.append(self.rawscale[0 + offset])
				offset += 1  
			
		self.rangify(9)
		self.assignMidiNums()	
		self.chromaticScale = [note for note in self.scale]


# Basic Scales #
class Major(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0, 2, 4, 5, 7, 9, 11]
		self.buildScale()
		
class Minor(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0, 2, 3, 5, 7, 9, 10]
		self.buildScale()	

class MelodicMinor(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0,2,3,5,7,8,11]
		self.buildScale()

# Penatonic Scales
class MajorPentatonic(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0,2,4,7,9]
		self.buildScale()

class MinorPentatonic(Chromatic):
	def __init__(self, key):
		super().__init__(key)
		self.intervals = [0,3,5,7,10]
		self.buildScale()