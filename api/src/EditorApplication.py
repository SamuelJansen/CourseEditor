if __name__ == '__main__' :
    from domain.control import PathMannanger
    pathMannanger = PathMannanger.PathMannanger(printStatus = True)

    import Editor, CourseRepository

    import numpy as np

    editor = Editor.Editor(pathMannanger,
        repository = CourseRepository,
        floor = True
    ).run()
