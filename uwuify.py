from owoify import owoify
import re, argparse, os, shutil

#Return a string between two characters. Stolen from https://stackoverflow.com/questions/3368969/find-string-between-two-substrings
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

#Function to edit a file given a name
def editFile(filename):
    newFileContents = ""
    excludeLines = [".include", "#include", "%MACRO", ".incbin"]
    #Open the file in readonly mode so can edit it later
    with open(filename, 'r') as file:
        #Go through file line by line
        for line in file:
            #excludes anything that shouldn't be owo'ified, such as include headers
            owo = False
            for exclude in excludeLines:
                if exclude in line:
                    owo = True
                    break
            if owo:
                newFileContents += line
                continue
                
            #don't try and owo'ify if there's not even a string there
            if '\"' in line:
                #Make a copy of the line
                newcontent = line

                #get everything between speech marks 
                uwu = find_between(newcontent, '"', '"')
                #get everything between { and } from the original
                dontreplace = find_between(newcontent, '{', '}')
                #remove anything between { and }
                uwu = uwu.replace(dontreplace, "")
                #owoify it
                owo = owoify(uwu)
                #put back anything between { and }
                owo = owo.replace("{}", "{" + dontreplace + "}")
                
                #replace non-owo with owo
                newcontent = line.replace("\""+ uwu + "\"", "\"" + owo + "\"")
                
                newFileContents += newcontent.replace(uwu, owo)
            else:
                #Nothing to edit, keep as original so add to edited file contents
                newFileContents += line

    #Make a copy of the file in case anything goes wrong

    #get the extension by splitting the filename into parts, reversing it and getting first element
    ext = os.path.splitext(filename)[-1:][0]
    editedFilename = filename.replace(ext, ".bak")
    shutil.copy2(filename, editedFilename)
    #Write edited data to file
    with open(filename, 'w') as file:
        file.write(newFileContents)

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file",   required=False , help="Optional path to edit single source manually")
args = vars(ap.parse_args())

print("Starting...")

#If single source file is specified, edit only that
if args["file"] is not None:
    editFile(args["file"])
#Otherwise, go through all files in current directory 
#If files has compatible extension, then edit them
else:
    fileExts = ["inc"]

    for root, dirs, files in os.walk("."):
        for file in files:
            for ext in fileExts:
                if file.endswith("." + ext):
                    editFile(os.path.join(root, file))

print("Finished")
