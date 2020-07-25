import sys
from PIL import Image
import os
from os import listdir
import glob
#don't touch the line below :) !!
print("#Created by iamharsh.dev")
print("\n")

#importing location
imageDir= input(" Enter the location of image folder  ")
if imageDir.endswith("/"):
    imageDir.replace("/","")
path =glob.glob(imageDir+"/"+'*')

print("\n")

#expoting location
outdir =input("Enter where to Export: ")
if outdir.endswith("/"):
    outdir.replace("/","")

def pngToWebp(path,outdir):
    for im in path:
        filename =os.path.basename(im)
        filename=filename.replace('png','webp')
        im =Image.open(im)
        im.save(outdir+"/"+filename,format="WebP", quality=60)

pngToWebp(path,outdir)
print("#Created by iamharsh.dev")
print("#K THANKS BYE#")

