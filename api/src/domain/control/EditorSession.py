import Session, Message
import sessionFunction

print('EditorSession library imported')

class EditorSession(Session.Session):

    GOLDEN_RATIO = 1.57

    def __init__(self,desk,navigationHistory):

        Session.Session.__init__(self,desk)

        self.globals = self.application.globals
        self.path = f'''{self.globals.getApiPath('Courses')}resource\\modules\\{navigationHistory}'''
        self.deskItemSize = [
            self.desk.size[0] // self.desk.itemsPerLine,
            int(self.desk.size[0] // self.desk.itemsPerLine / EditorSession.GOLDEN_RATIO)
        ]

    def save(self):
        Message.Message(self.desk,f'save_message',
            fontSize = 18
        )
