FileOption='Json'
import File_Handling.TextFileHandling as TH
import File_Handling.JsonFileHandling as JH

def RetriveUsersData():
    if FileOption=='Txt':
        return TH.RetriveUsersFileData()
    elif FileOption=='Json':
        return JH.GetUsersData()
    else:
        raise Exception
def RetriveProjectsData():
    if FileOption=='Txt':
        return TH.RetriveProjectsFileData()
    elif FileOption=='Json':
        return JH.GetProjectsData()
    else:
        raise Exception
    pass
def WriteUsersData(UsersData):
    if FileOption=='Txt':
        TH.RemoveUsersFileData()
        TH.AddUsersFileData(UsersData)
    elif FileOption=='Json':
        JH.AddUsersData(UsersData)
    else:
        raise Exception
    pass
def WriteProjectsData(ProjectsData):
    if FileOption=='Txt':
        TH.RemoveProjectsFileData()
        TH.AddProjectsFileData(ProjectsData)
    elif FileOption=='Json':
        JH.AddProjectsData(ProjectsData)
    else:
        raise Exception
    pass