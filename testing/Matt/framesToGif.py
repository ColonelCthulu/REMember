import imageio, sys
from os import listdir
from os.path import isfile, join, walk

if(len(sys.argv) != 3):
	print "ERROR; Usage: python frameToGif.py folderWithFrames outputfile.gif"
	sys.exit(0)
path = sys.argv[1]
path = path.strip('\n')
output = sys.argv[2]
output = output.strip('\n')
files = [f for f in listdir(path) if isfile(join(path, f))]

print "Creating gif"

images = []
for filename in files:
	pathname = path + "/" + filename
	images.append(imageio.imread(pathname))
imageio.mimsave(output, images)
