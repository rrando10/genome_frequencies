'''
	Nucleotide and Dinucleotide Frequency Calculator
	By Ronald Randolph
	September 2019

	This program reports the nucleotide and dinucleotide
	frequencies of a given genome. The results are printed
	to the terminal.
'''
import sys

#argument check
if(len(sys.argv) != 2):
	print ('Usage: calc_freq.py [filename]')
	sys.exit(1)

#open file and split lines into a list
file = sys.argv[1]

with open(file) as f:
	data = f.read().splitlines()

#remove header
data.pop(0)

nA = 0.0
nT = 0.0
nC = 0.0
nG = 0.0

nAA = 0.0
nAT = 0.0
nAG = 0.0
nAC = 0.0

nTA = 0.0
nTT = 0.0
nTG = 0.0
nTC = 0.0

nCA = 0.0
nCT = 0.0
nCG = 0.0
nCC = 0.0

nGA = 0.0
nGT = 0.0
nGG = 0.0
nGC = 0.0

tot = 0
p = ''

#3. reverse and compliment  each line
for line in data:
	tmp = list(line)
	
	for c in tmp:
		
		if (c == 'A'):
			nA += 1
			tot += 1
			if(p == 'A'):
				nAA += 1
			elif(p == 'T'):
				nTA += 1
			elif(p == 'G'):
				nGA += 1
			elif(p == 'C'):
				nCA += 1
			p = 'A'
		
		elif (c == 'T'):
			nT += 1
			tot += 1
			if(p == 'A'):
				nAT += 1
			elif(p == 'T'):
				nTT += 1
			elif(p == 'G'):
				nGT += 1
			elif(p == 'C'):
				nCT += 1
			p = 'T'
		
		elif (c == 'C'):
			nC += 1
			tot += 1
			if(p == 'A'):
				nAC += 1
			elif(p == 'T'):
				nTC += 1
			elif(p == 'G'):
				nGC += 1
			elif(p == 'C'):
				nCC += 1
			p = 'C'
		
		elif (c == 'G'):
			nG += 1
			tot += 1
			if(p == 'A'):
				nAG += 1
			elif(p == 'T'):
				nTG += 1
			elif(p == 'G'):
				nGG += 1
			elif(p == 'C'):
				nCG += 1
			p = 'G'
		
		else:
			print("error: %c" % c)

print("Nucleotide Freqencies:")
print("A: %f" % (nA / tot))
print("T: %f" % (nT / tot)) 
print("G: %f" % (nG / tot)) 
print("C: %f" % (nC / tot))

dtot = tot-1
print("\nDinucleotide Frequencies:")
print("AA: %f" % (nAA / dtot))
print("AT: %f" % (nAT / dtot))
print("AC: %f" % (nAC / dtot))
print("AG: %f" % (nAG / dtot))
print("TA: %f" % (nTA / dtot)) 
print("TT: %f" % (nTT / dtot)) 
print("TC: %f" % (nTC / dtot)) 
print("TG: %f" % (nTG / dtot)) 
print("CA: %f" % (nCA / dtot)) 
print("CT: %f" % (nCT / dtot)) 
print("CC: %f" % (nCC / dtot)) 
print("CG: %f" % (nCG / dtot)) 
print("GA: %f" % (nGA / dtot))
print("GT: %f" % (nGT / dtot))
print("GC: %f" % (nGC / dtot))
print("GG: %f" % (nGG / dtot))


