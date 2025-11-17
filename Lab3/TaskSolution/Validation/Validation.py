import re

def ValidateName(Name):
    if Name and Name.isalpha():
        return True
    return False

def ValidatePassword(Pass,CPass):
    if Pass==CPass:
        return True

def ValidateEmail(Email,AllUsersData):
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', Email)
    if valid:
        for Data in AllUsersData:
            if Data[2]==Email:
                return False
        return True
    return False

def ValidateNumber(Number):
    valid = re.match( r"^01[0125]\d*$", Number)
    if valid and len(Number)==11:
        return True
    return False

def ValidateRegistrationData(UserData,AllUsersData):
    if ValidateName(UserData[0]) and ValidateName(UserData[1]) and ValidateEmail(UserData[2],AllUsersData) and ValidatePassword(UserData[3],UserData[4]) and ValidateNumber(UserData[5]):
        return True
    return False

def ValidateLogin(UserData,AllUsersData):
    for Data in AllUsersData:
        if Data[2] == UserData[0] and Data[3]==UserData[1]:
            return True
    return False

def ValidateTarget(Target):
    if Target.isnumeric():
        return True
    return False

def ValidateData(StartDate,EndDate):
    # use datatime here
    st=StartDate.split('/')
    en=EndDate.split('/')
    if len(st)!=3 or len(en)!=3:
        return False

    for i in range(0,3):
        if not st[i].isnumeric() or not en[i].isnumeric():
            return False
        st[i]=int(st[i])
        en[i]=int(en[i])

    if not st[0] in range(1,32) or not en[0] in range(1,32):
        return False

    if not st[1] in range(1, 13) or not en[1] in range(1, 13):
        return False

    for i in range(2,-1,-1):
        if en[i]>st[i]:
            return True
        elif en[i]<st[i]:
            return False
    return True
def ValidateProject(ProjectData):
    if ValidateData(ProjectData[3],ProjectData[4]) and ValidateTarget(ProjectData[2]):
        return True
    return False