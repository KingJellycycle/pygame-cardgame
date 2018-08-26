import os.path
os.environ['TCL_LIBRARY'] = r'C:\\Users\\Morga\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Users\\Morga\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6'
import cx_Freeze
executables = [cx_Freeze.Executable("main.py")]


cx_Freeze.setup(
    name="Hexwar",
    options={"build_exe": {"packages":["pygame"],
                           "include_files": ["game.py","player.py","camera.py","cards.py","UI.py"]}},
    executables = executables

    )