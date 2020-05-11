if __name__ == '__main__' :
    from domain.control import Globals
    globals = Globals.Globals(debugStatus = True)

    import Editor, CourseRepository

    import numpy as np

    editor = Editor.Editor(globals,
        repository = CourseRepository,
        floor = True
    ).run()
