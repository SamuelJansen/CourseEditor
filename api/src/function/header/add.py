import pygame as pg

import MenuAccessEvent, MenuNavigationEvent, Message
import settingFunction, imageFunction, textFunction

import coursePathFunction

from tokenRepository import *

GENERATE_THUMBS = 'Generate thumbs'
MAKE_BASIC_SCRIPT = 'Make basic script'

def add(event) :

    if event.application.session :

        pathMannanger = event.application.pathMannanger
        itemsPathTree = {
            GENERATE_THUMBS : {},
            MAKE_BASIC_SCRIPT : {}
        }

        MenuAccessEvent.MenuAccessEvent(
            event.object,
            itemsPathTree,
            onLeftClick = MenuNavigationEvent.MenuNavigationEvent,
            onMenuResolve = addResolve,
            itemSize = [textFunction.Attribute.WORD_WIDTH,26]
        )

    print(f'{event.name}.add()')

def addResolve(event) :
    if event.object.name == GENERATE_THUMBS :
        generateThumbs(event)
    if event.object.name == MAKE_BASIC_SCRIPT :
        makeBasicScript(event)
    print(f'{event.name}.addResolve()')

def generateThumbs(event) :
    message = Message.Message(event.application.session.desk,
        name = 'creatingThumbs',
        message = 'Creating thumbs',
        fontSize = 18
    )
    THUMB = 'thumb'
    application = event.application
    if event.application.session :
        deskItemSize = event.application.session.deskItemSize
        imageExtension = 'png'
        imageNames = settingFunction.getFileNames(f'{event.application.session.path}image\\',imageExtension)
        padding = event.application.session.desk.padding
        for imageName in imageNames :
            imagePath = f'{event.application.session.path}image\\{imageName}.{imageExtension}'
            imageThumbPath = f'{event.application.session.path}image\\{THUMB}\\{imageName}.{THUMB}.{imageExtension}'
            imageFunction.saveImage(
                imageFunction.getImage(imagePath,deskItemSize,application,
                    padding = padding
                ),
                imageThumbPath
            )
    message.close()
    print(f'{event.name}.generateThumbs()')

def makeBasicScript(event) :
    if event.application.session :
        audioExtension = 'mp3'
        imageExtension = 'png'
        backwardButton = f'{db_OPEN_SQUARE_BRACKETS}92x765 172x840{db_CLOSE_SQUARE_BRACKETS}'
        forwardButton = f'{db_OPEN_SQUARE_BRACKETS}1393x761 1500x844{db_CLOSE_SQUARE_BRACKETS}'
        audioNames = settingFunction.getFileNames(f'{event.application.session.path}audio\\',audioExtension)
        imageNames = settingFunction.getFileNames(f'{event.application.session.path}image\\',imageExtension)
        lessonScriptList = []
        for index in range(len(imageNames)) :
            scriptList = []
            if f'{index}' in audioNames :
                scriptList.append(f'audio{db_COLON}{index}')
            script = db_OPEN_SQUARE_BRACKETS
            for instruction in scriptList :
                script += f'{instruction} '
            script = f'{script.strip()}{db_CLOSE_SQUARE_BRACKETS}'
            lessonScriptList.append(f'{db_PAGE}{db_COLON}{index}{db_COMA}{db_IMAGE}{db_COLON}{imageNames[index]}{db_COMA}{db_BACKWARD_BUTTON}{db_COLON}{backwardButton}{db_COMA}{db_FOWARD_BUTTON}{db_COLON}{forwardButton}{db_COMA}{db_PAGE_SCRIPT}{db_COLON}{script}')
        lessonScriptPath = f'{event.application.session.path}{coursePathFunction.getLessonScriptName(event.application.session.path)}.{event.application.extension}'
        with open(lessonScriptPath,"w+",encoding="utf-8") as lessonScriptFile :
            lessonScriptFile.write('\n\n'.join(lessonScriptList))
    print(f'{event.name}.makeBasicScript()')
