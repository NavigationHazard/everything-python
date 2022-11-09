from PIL import Image
from os import listdir
import sys, os, os.path

def conv():
    '''define a path to open images inside the images/ folder as first argument
        and Output/ folder as second argument'''

    #Get arguments and defined input/output directory
    arguments = sys.argv[1:3]
    DIR = "./" + arguments[0]
    OUT = "./" + arguments[1]

    #count file in directory and create output folder if not already exists
    countfile = len([name for name in os.listdir(DIR)])
    if not os.path.exists(OUT):
        os.mkdir("./" + arguments[1])
    else:
        print("Folder {} has alreay been created".format(OUT))

    #get a list of files in the folder ending with .png and convert them to jpeg
    #as well as tuning them into a thumbnail

    listoffile = listdir(DIR)
    for i in range(0, countfile):
        if listoffile[i].endswith(".png"):
            im = Image.open(DIR+listoffile[i])
            im.thumbnail((400, 200))
            rgb_im = im.convert('RGB')
            rgb_im.save(OUT+listoffile[i].replace(".png", ".jpeg"))

    # Give feedback when done
    print("{} Files have been converted to thumbnails and turned into jpegs".format(countfile))

conv()
