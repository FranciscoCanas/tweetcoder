import sys
import json
import re

TEMP_FILE = './dumps/temp'

def dump_to_json(j_file_name, out_file_name):
	'''
	Remove all of the header info from between the tweets in the db dump, then
	output all of the texts from the tweets.
	'''

	jsonfile = open(j_file_name)
	jsonstream = jsonfile.read() # Input json file with headers
	outstream = open(out_file_name,'w')

	# remove headers between jsons
	jsons = re.sub('Content-Type: .*{','',jsonstream) 
	jsons = re.sub('--==.*{','\n{',jsons)

	jsonarr = jsons.split( '\n' )

	for jsonstr in jsonarr:
		if jsonstr[0] =='{': 
			jsonobj = json.loads( jsonstr )
			#print jsonobj['text']
	   		outstream.write(json.dumps( jsonobj ).encode('ascii','ignore') + "\n")
	jsonfile.close()
	outstream.close()

def dump_texts(j_file_name, out_file_name):
	'''
	Takes the name of a file containing json tweet objects separated by space, extracts their body texts,
	and outputs them to a new file. 
	'''
	jsonstream=open(j_file_name,'r') # Input file
	jsons=jsonstream.read()

	outstream = open(out_file_name, 'w') # Output file

	#jtexts=jsons.split('\n')
	for jtext in jsons:
		if jtext[0]!='\n':
			jsonobj = json.loads(jtext)
			outstream.write(jsonobj['text'].encode('ascii','ignore') + "\n")

	jsonstream.close()
	outstream.close()

if __name__=="__main__":
	if len(sys.argv) < 2:
		print "Useage: python jtotext <inputfile> <outputfile>"
		sys.exit()

	dump_to_json(sys.argv[1], TEMP_FILE)
	dump_texts(TEMP_FILE,sys.argv[2])
	sys.exit()