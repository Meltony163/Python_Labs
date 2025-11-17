import InputOutput.InputOutput as IO
import Validation.Validation as V
import File_Handling.FileHandling as FH

ChoosenIndex=None
LoggedUserData=None

AllUsersData=FH.RetriveUsersData()
AllProjectsData=FH.RetriveProjectsData()

MainMenu=["User","Projects"]
AuthenticationMenu=["Registration","Login"]
RegistrationMenu=["First Name:","Last Name:","Email:","Password:","Confirm Password:","Mobile Phone:"]
LoginMenu=["LoginEmail:","LoginPassword:"]
ProjectMenu=['CreateProject','ViewAllProjects','EditProjects','DeleteProject','SearchForProject']
ProjectData=['Title:','Details:','TotalTarget:','StartDate:','EndDate']
SearchForProject=['Enter Project End Data:']
DeleteProject=["Enter Project Title To Delete:"]
EditProject=['Details','TotalTarget','EndDate']

def RegistirationHandling():
    global AllUsersData
    NewUserData = IO.InputOutputScreen(RegistrationMenu)
    if V.ValidateRegistrationData(NewUserData, AllUsersData):
        NewUserData.pop(3)
        AllUsersData.append(NewUserData)
        IO.PrintMessage("Registration Is Completed Successfully", (0, 255, 0))
    else:
        IO.PrintMessage("Registration Fail", (255, 0, 0))

def LoggingHandling():
    global LoggedUserData
    global AllUsersData
    LoginData = IO.InputOutputScreen(LoginMenu)
    if V.ValidateLogin(LoginData, AllUsersData):
        IO.PrintMessage("Login Successfully", (0, 255, 0))
        LoggedUserData = LoginData
    else:
        IO.PrintMessage("Login Failed", (255, 0, 0))

def EditingProjectsHandling():
    global AllProjectsData
    global LoggedUserData
    UserProjects = []
    UserProjectsIndex = []
    if LoggedUserData==None:
        IO.PrintMessage("You Have To Log In",(255,0,0))
        return
    for ProjectIndex in range(len(AllProjectsData)):
        if AllProjectsData[ProjectIndex][5] == LoggedUserData[0]:
            UserProjects.append(AllProjectsData[ProjectIndex])
            UserProjectsIndex.append(ProjectIndex)
    if UserProjectsIndex:
        IO.PrintMessage("Choose Project To Edit", (0, 255, 0))
        ChoosenProjectIndex = IO.OutputScreen([project[0] for project in UserProjects])
        if ChoosenProjectIndex != -1:
            ChoosenIndex = IO.OutputScreen(EditProject)
            if ChoosenIndex != -1:
                ModifiedData = IO.InputOutputScreen(['Enter New Data:'])[0]
                if ChoosenIndex == 0:
                    UserProjects[ChoosenProjectIndex][1] = ModifiedData
                elif ChoosenIndex == 1:
                    if V.ValidateTarget(ModifiedData):
                        UserProjects[ChoosenProjectIndex][2] = ModifiedData
                elif ChoosenIndex == 2:
                    if V.ValidateData(UserProjects[ChoosenProjectIndex][3], ModifiedData):
                        UserProjects[ChoosenProjectIndex][4] = ModifiedData
                for i in range(len(UserProjectsIndex)):
                    AllProjectsData[UserProjectsIndex[i]] = UserProjects[i]
            else:
                return -1
        else:
            return -1

    else:
        IO.PrintMessage("You Have No Projects", (255, 0, 0))

def AddingProjectHandling():
    global LoggedUserData
    global AllProjectsData
    if LoggedUserData:
        NewProjectData = IO.InputOutputScreen(ProjectData)
        NewProjectData.append(LoggedUserData[0])
        if V.ValidateProject(NewProjectData):
            AllProjectsData.append(NewProjectData)
            IO.PrintMessage("Project Added Successfully", (0, 255, 0))
        else:
            IO.PrintMessage("Failed To Add Project", (0, 255, 0))
    else:
        IO.PrintMessage("You Have To Login", (255, 0, 0))


def DeletingProject():
    global LoggedUserData
    global AllProjectsData
    if not LoggedUserData:
        IO.PrintMessage("You Have To Login", (255, 0, 0))
        return
    ProjectTitleTodelete = IO.InputOutputScreen(DeleteProject)
    FoundedProjects = []
    for i in range(len(AllProjectsData)):
        if AllProjectsData[i][0] in ProjectTitleTodelete and AllProjectsData[i][5] == LoggedUserData[0]:
            FoundedProjects.append(i)
    if FoundedProjects:
        FoundedProjects.reverse()
        for i in FoundedProjects:
            AllProjectsData.pop(i)
        IO.PrintMessage("Projects Founded and deleted Successfully", (0, 255, 0))
    else:
        IO.PrintMessage("Failed To Find Project", (255, 0, 0))


def SearchingForProject():
    global AllProjectsData
    ProjectEndDate = IO.InputOutputScreen(SearchForProject)[0]
    FoundedProjects = []
    for Project in AllProjectsData:
        if Project[4] == ProjectEndDate:
            FoundedProjects.append(Project)
    if FoundedProjects:
        IO.PrintMessage("Projects Successfully Found", (0, 255, 0))
        IO.ListProject(FoundedProjects)
    else:
        IO.PrintMessage("Failed To Find Project", (255, 0, 0))

while ChoosenIndex!=-1:
    ChoosenIndex=IO.OutputScreen(MainMenu)
    if ChoosenIndex==0:
        ChoosenIndex=IO.OutputScreen(AuthenticationMenu)
        if ChoosenIndex==0:
            RegistirationHandling()
        elif LoggedUserData and ChoosenIndex==1:
            IO.PrintMessage("Already Logged", (0, 255, 0))
        elif ChoosenIndex==1:
            LoggingHandling()
    elif ChoosenIndex==1:
        ChoosenIndex=IO.OutputScreen(ProjectMenu)
        if ChoosenIndex==0:
            AddingProjectHandling()
        elif ChoosenIndex==1:
            IO.ListProject(AllProjectsData)
        elif ChoosenIndex==2:
            ChoosenIndex=EditingProjectsHandling()
        elif ChoosenIndex==3:
            DeletingProject()
        elif ChoosenIndex==4:
            SearchingForProject()


FH.WriteProjectsData(AllProjectsData)
FH.WriteUsersData(AllUsersData)

