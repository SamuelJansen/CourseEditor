import Application, Header, EditorSession
import surfaceFunction, headerFunction, settingFunction, applicationFunction

import ItemDto
import exit, openModule, closeModule, save, add, launch, update, unlaunch

print('Editor library imported')

class Editor(Application.Application):

    def __init__(self,*args,**kargs):

        Application.Application.__init__(self,*args,**kargs)

        headerPosition  = [0,0]
        headerSize = ['100%',20]
        headerFather = self.getFloor()

        headerItems = [
            ItemDto.ItemDto('exit',onLeftClick=exit.exit),
            ItemDto.ItemDto('openModule',onLeftClick=openModule.openModule),
            ItemDto.ItemDto('closeModule',onLeftClick=closeModule.closeModule),
            ItemDto.ItemDto('save',onLeftClick=save.save),
            ItemDto.ItemDto('add',onLeftClick=add.add),
            ItemDto.ItemDto('launch',onLeftClick=launch.launch),
            ItemDto.ItemDto('update',onLeftClick=update.update),
            ItemDto.ItemDto('unlaunch',onLeftClick=unlaunch.unlaunch)
        ]

        Header.Header(
            headerPosition,
            headerSize,
            headerFather,
            items = headerItems,
            itemSize = [surfaceFunction.Types.SQUARE,'100%'],
            padding = [1,1]
        )

        self.sessionClass = EditorSession.EditorSession
