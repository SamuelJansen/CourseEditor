import MenuAccessEvent, MenuNavigationEvent

import pageSelection, textFunction

def openModule(event) :

    globals = event.application.globals
    itemsPathTree = globals.getPathTreeFromPath(f'''{globals.getApiPath('Courses')}resource\\modules\\''')

    MenuAccessEvent.MenuAccessEvent(
        event.object,
        itemsPathTree,
        onLeftClick = MenuNavigationEvent.MenuNavigationEvent,
        onMenuResolve = pageSelection.pageSelection,
        itemSize = [textFunction.Attribute.WORD_WIDTH,26]
    )

    print(f'{event.name}.openModule()')
