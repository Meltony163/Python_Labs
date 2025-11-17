def RetriveUsersFileData():
    try:
        F=open("UsersData.txt",'r')
        Ls=[]
        for line in F:
            Ls.append(line.replace('\n','').split(":"))

        F.close()
        return Ls
    except:
        print("TH.RetriveUsersFileData Error")
def RemoveUsersFileData():
    try:
        F=open("UsersData.txt",'w')
        F.close()
    except:
        print("TH.RemoveUsersFileData Error")
def AddUsersFileData(UserData):
    try:
        F=open("UsersData.txt",'a')
        for Data in UserData[:-1]:
            F.write(":".join(Data)+'\n')
        F.write(":".join(UserData[-1]))
        F.close()
    except:
        print("TH.AddUsersFileData Error")

def RetriveProjectsFileData():
    try:
        F = open("ProjectsData.txt", 'r')
        Ls = []
        for line in F:
            Ls.append(line.replace('\n','').split(":"))
        F.close()
        return Ls
    except:
        print("TH.RetriveProjectsFileData Error")

def RemoveProjectsFileData():
    try:
        F = open("ProjectsData.txt", 'w')
        F.close()
    except:
        print("TH.RemoveProjectsFileData Error")

def AddProjectsFileData(ProjectData):
    try:
        F = open("ProjectsData.txt", 'a')
        for Data in ProjectData[:-1]:
            F.write(":".join(Data) + '\n')
        F.write(":".join(ProjectData[-1]))
        F.close()
    except:
        print("TH.AddProjectsFileData Error")