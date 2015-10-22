#!/usr/bin/python3
import sys
import os.path
import time
import datetime

#Print error and exit
def errorMessage(messsage):
    print("There was an error!")
    print("Error: ", messsage)

# This is for counting the args print(len(sys.argv))
if len(sys.argv) <= 1:
    errorMessage("You need to provide a file!")
    sys.exit()

fileName = (sys.argv[1])

#Test if file exists
if not os.path.isfile(fileName):
    errorMessage("File was not found!")

#Open file
fileOpen = open('%s' % fileName,'r')
fileRead = fileOpen.read()
fileOpen.close()
fileRead = fileRead.split("\n")

#Replace all spaces in file name with dash and remove any periods
fileName2 = fileName.split(".")[0]
fileName2 = fileName.replace(" ","-")

#Set the post name
postName = str(datetime.date.today()) + '-' + str(time.strftime("%H-%M-%S")) + "-" + fileName2.split(".")[0] + ".html"
postTime = str(datetime.date.today()) + " " + str(time.strftime("%H-%M-%S"))

#Find tags in file
tagsInFile = ''
with open("%s" % fileName) as f:
    for line in f:
        if "tags:" in line:
             tagsInFile = line
print(tagsInFile)
if len(tagsInFile) > 0:
    tagsInFile = tagsInFile.split(":")[1]
    print(tagsInFile)
#time to create the file
print("Post name " + postName)
print("File name2 " + fileName2)
fileWrite = open("%s" % postName, 'w+')
fileWrite.write("---\n")
fileWrite.write("layout: post\n")
fileWrite.write("name: " + (fileName2.split(".")[0]).replace("-"," ") + "\n")
fileWrite.write("title: " + (fileName2.split(".")[0]).replace("-"," ") + "\n")
fileWrite.write("time: %s\n" % postTime)
#Test if there's tags and write them into the post
if len(tagsInFile) > 0:
    fileWrite.write("tags:" + tagsInFile + "\n")
fileWrite.write("---\n")

#This will now write out the lines in the file, excluding tags
print(len(fileRead))
num = 0
for x in fileRead:
    if not "tags:" in fileRead[num]:
        fileWrite.write(x + "\n")
    num + 1

#Now it's time to move this file to the blog
if len(sys.argv) <= 2:
    errorMessage("No path to the blog provided. Will leave the post here.")
    sys.exit()

#Path provided, now test it
blogPath = sys.argv[2]
pathToSite = blogPath + "_posts"
print(pathToSite)
if not os.path.isdir(pathToSite):
    errorMessage("The blog path provided doesn't exist.")
    sys.exit()

#Move the file
newName = pathToSite + "/" + postName
os.rename(postName, newName)
