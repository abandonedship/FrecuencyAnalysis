import collections
import sys
import os

def Help():

	print('PYTHON CHARACTER FREQUENCY ANALYSIS')
	print('Usage python3 freqz_analysis.py -f file.txt\nor python3 freqz_analysis.py "String to analize"')

def OUTPUT():

	os.system("sed -i 's/:/ =/g' /tmp/freq.out")
	os.system("sed -i 's/,/\\n/g' /tmp/freq.out")
	os.system("sed -i 's/{/ /g' /tmp/freq.out")
	os.system("sed -i 's/}/ /g' /tmp/freq.out")
	os.system("sed -i \"s/' '/space/g\" /tmp/freq.out")
	os.system("sed -i \"s/' =/ =/g\" /tmp/freq.out")
	os.system("sed -i \"s/ '//g\" /tmp/freq.out")
	os.system("sed -i 's/ space/space/g' /tmp/freq.out")
	os.system('cat /tmp/freq.out')

def String_FREQ():

	string = sys.argv[1]

	frequencies = collections.Counter(string)

	repeated = {}

	for key, value in frequencies.items():

# iterate through frequencies dictionary

		if value > 0:

			repeated[key] = value

# if character repats, add to repeated dictionary)

	repeated=str(repeated)
	f = open("/tmp/freq.out","w")
	f.write(str(repeated))
	f.close()

#### Converting python dic to more readable
	OUTPUT()

def ReadFromFile_FREQ():

	f = open(sys.argv[2],"r")

	for i in f:

		string = i

		frequencies = collections.Counter(string)

		repeated = {}


		for key, value in frequencies.items():


			if value > 0:

				repeated[key] = value

		repeated=str(repeated)
		f = open("/tmp/freq.out","w")
		f.write(str(repeated))
		f.close()

		OUTPUT()

try:
	if sys.argv[1] == "-f":
		print("Reading from file " + sys.argv[2])
		ReadFromFile_FREQ()
	else:
		print("String " + sys.argv[1])
		String_FREQ()
except IndexError:

	Help()
