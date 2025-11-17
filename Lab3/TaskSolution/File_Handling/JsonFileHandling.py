import json

UsersKeys=["Fname","Lname","Email","Password","Telephone"]
ProjectsKeys=["Title","Details","Target","StartDate","EndDate","Owner"]

def AddUsersData(UsersData):
    try:
        with open('Data.json', 'r') as f:
            data = json.load(f)
        data["Users"].clear()
        for user in UsersData:
            data["Users"].append(dict(zip(UsersKeys,user)))
        f.close()
        with open('Data.json', 'w') as f:
            json.dump(data,f,indent=4)
    except:
        print("JS.AddUsersData Error")

def AddProjectsData(UsersData):
    try:
        with open('Data.json', 'r') as f:
            data = json.load(f)
        data["Projects"].clear()
        for user in UsersData:
            data["Projects"].append(dict(zip(ProjectsKeys,user)))
        f.close()
        with open('Data.json', 'w') as f:
            json.dump(data,f,indent=4)
    except:
        print("JS.AddProjectsData Error")

def GetUsersData():
    try:
        with open('Data.json', 'r') as f:
            data = json.load(f)
        UsersData=[list(userdata.values()) for userdata in data["Users"]]
        return UsersData
    except:
        print("JS.GetUsersData Error")


def GetProjectsData():
    try:
        with open('Data.json', 'r') as f:
            data = json.load(f)
        UsersData=[list(userdata.values()) for userdata in data["Projects"]]
        return UsersData
    except:
        print("JS.GetProjectsData Error")

