import os
from _winreg import *


def returnDir():
    dirs=['C:\\Recycler\\', 'C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for r in dirs:
        if os.path.isdir(r):
            return r
    return None


def sid2use(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList\\"+ sid)
        (vaule, typ) = QueryValueEx(key, 'ProfileImagePath')
        user = vaule.split("\\")[-1]
        return user
    except:
        return sid

def findRecycled(Rdir):
    dirList = os.listdir(Rdir)
    for sid in dirList:
        files = os.listdir(Rdir + sid)
        user = sid2use(sid)
        print "[+] Listing Files for: "+ user
        for file in files:
            print "[+] found this file" + file
if __name__ == '__main__':
    dict = returnDir()
    findRecycled(dict)