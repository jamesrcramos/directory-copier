from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import shutil
import sys
import os

#global variables
TODAY = datetime.now()

#progress bar to track progress of main function
# mainProgressBar = Progressbar(
#     progWindow,
#     orient = 'horizontal',
#     mode = 'determinate',
#     length = 280
#     )
# mainProgressBar.grid(column = 0, row = 8, columnspan = 2, padx = 10, pady = 20)

def initializeUserVariables():  #run this function when interface isn't in use
    print("Enter call letters:") 
    callLettersOfPhotog = input()
    print("Enter destination in external hard drive:")
    hardDriveRootPath = input()
    print("Enter user's account name on laptop:")
    userAcctNameOnDevice = input()
    photogFolderRootPath = hardDriveRootPath + "\\" + callLettersOfPhotog + " - " + TODAY.strftime('%m-%d-%Y')
    return(callLettersOfPhotog, hardDriveRootPath, userAcctNameOnDevice, photogFolderRootPath)

def createFolders(photogRoot, acctName):
    os.makedirs(photogRoot, exist_ok=True)

    photogDesktop = photogRoot + "\\" + "_Desktop"
    photogDocuments = photogRoot + "\\" + "_Documents"
    photogDownloads = photogRoot + "\\" + "_Downloads"
    photogExports = photogRoot + "\\" + "_Exports"
    photogPictures = photogRoot + "\\" + "_Pictures"

    localDesktop = "C:\\Users\\" + acctName + "\\Desktop"
    localDocuments = "C:\\Users\\" + acctName + "\\Documents"
    localDownloads = "C:\\Users\\" + acctName + "\\Downloads"
    localExports = "C:\\2007fall\\exports"
    localPictures = "C:\\Users\\" + acctName + "\\Pictures"
    
    return(photogDesktop, photogDocuments, photogDownloads, 
    photogExports, photogPictures, localDesktop, 
    localDocuments, localDownloads, localExports,
    localPictures)

def transferData(src, dest):
    shutil.copytree(src, dest) 

# def increaseProgress():
#     mainProgressBar['value'] += 25

def main(CL, rootPath, userName):
    #input section
    callLetters = CL
    hardDriveRoot = rootPath
    userAcctName = userName 
    photogFolderRoot = hardDriveRoot + "\\" + callLetters + " - " + TODAY.strftime('%m-%d-%Y') 

    #callLetters, hardDriveRoot, userAcctName, photogFolderRoot = initializeUserVariables() #run this line when interface isn't in use

    #creating folders 
    (photogDesktopFolder, photogDocumentsFolder, photogDownloadsFolder, 
    photogExportsFolder, photogPicturesFolder, localDesktopFolder, 
    localDocumentsFolder, localDownloadsFolder, localExportsFolder,
    localPicturesFolder) = createFolders(photogFolderRoot, userAcctName)

    #copying data between folders
    #backing up local desktop folder 
    transferData(localDesktopFolder, photogDesktopFolder)
    #backing up local documents folder 
    transferData(localDocumentsFolder, photogDocumentsFolder)
    #backing up local downloads folder
    transferData(localDownloadsFolder, photogDownloadsFolder)
    #backing up local exports folder
    transferData(localExportsFolder, photogExportsFolder)
    #backing up local pictures folder
    transferData(localPicturesFolder, photogPicturesFolder)

    #output section
    print("The photographer's laptop has been backed up successfully.")

def runThroughInterface():
    def clickedStartBackup():
        #confirming click of button
        lbl2 = Label(progWindow, text = "Process has started")
        lbl2.grid(column = 0, row = 2)

        #displaying data entry boxes
        clTxt = Entry(progWindow, width = 20)
        clTxt.grid(column = 0, row = 3)
        rootTxt = Entry(progWindow, width = 20)
        rootTxt.grid(column = 0, row = 4)
        nameTxt = Entry(progWindow, width = 20)
        nameTxt.grid(column = 0, row = 5)

        #calling main() to initiate backup process
        def clickedSendArguments():  
            #gather input to send as arguments to main
            cl = clTxt.get()
            if len(cl) == 0:
                messagebox.showerror('Error', 'Entry is empty')
            else:
                pass
            root = rootTxt.get()
            if len(root) == 0:
                messagebox.showerror('Error', 'Entry is empty')
            else:
                pass
            name = nameTxt.get()  
            if len(name) == 0:
                messagebox.showerror('Error', 'Entry is empty')
            else:
                pass
            main(cl, root, name)

            #confirming process is completed
            lbl3 = Label(progWindow, text = "The photographer's laptop has been backed up successfully.")
            lbl3.grid(column = 0, row = 7)
        
        #button to start backup progress
        btn2 = Button(progWindow, text = "Send arguments", command = clickedSendArguments)
        btn2.grid(column = 0, row = 6)

    progWindow = Tk()
    progWindow.geometry('700x400')
    progWindow.title("SSI Photog. Directory Copier for Backups")
    lbl = Label(progWindow, text="A directory copier to backup photographer files from a laptop.")
    lbl.grid(column = 0, row = 0)
    btn = Button(progWindow, text = "Start backup", command = clickedStartBackup)
    btn.grid(column = 0, row = 1)

    progWindow.mainloop()

#running program
runThroughInterface()
#main() #run this line when interface isn't in use