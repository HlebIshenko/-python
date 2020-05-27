import os
import shutil
import gui

class Moover:

    Exts = {
        "audio": ['.mp3'],
        "video": ['.mp4'],
        "documents": ['.txt', '.pdf', '.docx', '.xlsx'],
        "def": ['.cpp', '.js', '.html', '.php'],
        "ExeAndOther": ['.exe', '.msi'],
        "archiws": ['.rar', '.zip', '.tgz'],
        "images": ['.jpeg', '.jpg', '.png'],
    }

    CreatedFolders = {
        "video": 'video',
        "audio": 'audio',
        "documents": 'documents',
        "def": 'SourcesFiles',
        "ExeAndOther": "ExeFolder",
        "archiws": "archiws",
        "images": "Images",
    }

    

    def __init__(self, dir):
        self.dir = dir
    


    def loadAll(self):
        self.files = os.listdir(self.dir)
        self.dir += '\\'
        for folder in self.CreatedFolders:
            self.CreatedFolders[folder] = self.dir + self.CreatedFolders[folder]
        


    def initFolder(self, folder):
        if(not os.path.exists(self.CreatedFolders[folder])): 
            os.mkdir(self.CreatedFolders[folder])



    def pushInAFolder(self, name, ext):
        for thisExt in self.Exts:
            if(ext in self.Exts[thisExt]):
                self.initFolder(thisExt)
                shutil.move(self.dir + name, self.CreatedFolders[thisExt])



    def sort(self):
        for file in self.files:
            ext = os.path.splitext(file)[1]
            if(ext != ""): self.pushInAFolder(file, ext)


    def main(self):
        self.loadAll()
        self.sort()


def main():
    move = Moover(gui.window())
    move.main()

main()
