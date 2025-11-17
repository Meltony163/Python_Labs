import pygame
import time

HiglightedColor = (255, 0, 0)
DefaultColor = (255, 255, 255)
HiglightedIndex = 0

pygame.init()
pygame.display.set_caption('Crowd-Funding')
screen = pygame.display.set_mode((600, 600))
running = True
PressedKey = None
ChoosenIndex = None
BaseFont = pygame.font.SysFont("Arial", 20)

ProjectData=['Title:','Details:','TotalTarget:','StartDate:','EndDate']

def DrawText(Text, color, x, y):
    screen.blit(BaseFont.render(Text, True, color), (x, y))

def PrintMessage(Message, Color):
    screen.fill((0, 0, 0))
    DrawText(Message, Color, 200, 300)
    pygame.display.flip()
    time.sleep(3)

def PrintMenuItems(MenuItems):
    global HiglightedIndex
    for i in range(len(MenuItems)):
        if i == HiglightedIndex:
            DrawText(MenuItems[i], HiglightedColor, 200, 300 + 20 * i)
        else:
            DrawText(MenuItems[i], DefaultColor, 200, 300 + 20 * i)

def HandleNavigationKeys(mxsize):
    global HiglightedIndex
    global running
    global ChoosenIndex

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ChoosenIndex = -1
            running = False
            break

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                HiglightedIndex -= 1
                if HiglightedIndex < 0:
                    HiglightedIndex = mxsize - 1

            elif event.key == pygame.K_DOWN:
                HiglightedIndex += 1
                HiglightedIndex = HiglightedIndex % mxsize

            elif event.key == pygame.K_RETURN:
                ChoosenIndex = HiglightedIndex

def OutputScreen(menu):
    global ChoosenIndex
    global running
    global HiglightedIndex

    screen.fill((0, 0, 0))
    HiglightedIndex = 0
    ChoosenIndex = None

    while running:
        PrintMenuItems(menu)
        HandleNavigationKeys(len(menu))

        if ChoosenIndex is not None:
            return ChoosenIndex

        pygame.display.flip()

def HandleInputs(i, MenuLs):
    UserInput = ''
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ChoosenIndex = -1
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    break

                elif event.key == pygame.K_ESCAPE:
                    return False

                elif event.key == pygame.K_BACKSPACE:
                    UserInput = UserInput[:-1]

                else:
                    UserInput += event.unicode

        # Clear screen and redraw label
        screen.fill((0, 0, 0))

        # Draw label
        label_surface = BaseFont.render(MenuLs[i], True, HiglightedColor)
        screen.blit(label_surface, (200, 300))

        # Compute input start position (right after the label)
        label_width = label_surface.get_width()
        input_x = 200 + label_width + 10

        # Draw input text
        input_surface = BaseFont.render(UserInput, True, (255, 255, 255))
        screen.blit(input_surface, (input_x, 300))

        pygame.display.flip()

    return UserInput

def InputOutputScreen(MenuItems):
    UserData = []
    screen.fill((0, 0, 0))
    global HiglightedIndex
    HiglightedIndex = 0

    for i in range(len(MenuItems)):
        screen.fill((0, 0, 0))
        value = HandleInputs(i, MenuItems)
        UserData.append(value)

        if value is False:
            return False

    return UserData

def ListProject(ProjectsList):
    global ProjectData
    global HiglightedIndex
    HiglightedIndex = -1

    for Project in ProjectsList:
        screen.fill((0, 0, 0))
        running = True
        ProjectMenu = []

        for DataIndex in range(len(ProjectData)):
            ProjectMenu.append(ProjectData[DataIndex] + Project[DataIndex])

        PrintMenuItems(ProjectMenu)
        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False
