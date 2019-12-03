import os #used for browsing files
import Image #used for changing pixel colors

"""I used this program to change all green pixels into a color closer to red but of course you can change that.
First we find find all files that contain the .png(this can be changed to .jpg for example) ,and then
we edit the colors of these files pixel by pixel"""

def changeColor(imageTitle) :
    pic = Image.open(imageTitle)
    wid ,hei= pic.size

    img = Image.new( pic.mode, pic.size)
    pixelsNew = img.load()
    for x in range(0, wid - 1):
        for y in range(0, hei - 1):
            r,g,b,s = pic.getpixel( (x,y) )
            #print("Red: {0}, Green: {1}, Blue: {2}".format(r,g,b)) #this was here for testing reasons
            if g>100 :  #here we choose to change the color of the pixels whose green value is above 100
                if g>225:
                    g=200
                pixelsNew[x,y] = (g+50,r-30,b-35,s)#modify this line to change the resulting color of each pixel
                #print pixelsNew[x,y] #this was here for testing reasons

    img.save(imageTitle)


imageFiles=[]#list of the directories of each file
imageNames=[]#list of the names of each file
for root, subdirs, files in os.walk('/home/garry/Desktop/yo/ExamplesAfter'): #change this, to the directory within which you want to alter the images
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.png'):
             #print os.path.join(root, file)
             imageFiles.append(os.path.join(root))
             imageNames.append(file)

for i in range(0,len(imageFiles)) :
    os.chdir(imageFiles[i])#change directory to the one of the file we are about to modify
    if imageNames[i][-1]=="g" :#necessary as non png files would often be listed,might not be enough in cases that I didn't encounter
        print imageNames[i]
        try: #this try was necessary as the program would fail to change the color of some pixels
            changeColor(imageNames[i])
        except:
            pass
