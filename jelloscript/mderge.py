import sys
import glob
import os

def process_line(folder, line):
	if line.lower().startswith("!include"):
		return process_file(folder, folder + "\\" + line[8:].strip())
	return line


def process_file(folder, filename):
	out = ""
	with open(filename, 'r') as f:
		for line in f:
			out += process_line(folder, line)
	return out

if len(sys.argv) < 3:
	print("Usage: {INPUT FOLDER} {OUTPUT FOLDER}")
	exit(1)

infolder = sys.argv[1]
outfolder = sys.argv[2]

if not os.path.exists(outfolder):
	os.mkdir(outfolder)

#for f in glob.glob(outfolder + "*/**", recursive=True):
#	try:
#		os.remove(f)
#	except OSError as e:
#		print("Error: %s : %s" % (f, e.strerror))

files = [os.path.relpath(f) for f in glob.glob(infolder + "/**/*.md", recursive=True)]

for f in files:
	content = process_file(infolder, f)
	outfilename = ".\\" + outfolder + f[(len(infolder)):]
	outfilefolder = os.path.dirname(outfilename)
	if not os.path.exists(outfilefolder):
		os.makedirs(outfilefolder)
	out = open(outfilename, 'w')
	out.write(content)