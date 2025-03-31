from cx_freeze import*
includefiles = ["mana.ico"]
exclude = []
packages = []
base = None
if sys.platform == "Win32":
    base = "win32GUI"

shortcut_table = [
    ("Desktopshortcut",  # shortcut
     "DesktopFolder",  #Directory_
     "studentmanagementsystecomplete",  #Name
     "TARGETDIR",  #Component_
     "[TARGETDIR]\studentmanagementsystemcomplete.exe",  #Target
     None,  #Arguments
     None,  #Description
     None,  #Hotkey
     None,  #Icon
     None,  #IconIndex
     None,  #Showcmd
     "TARGETDIR",  #WkDir
     )

]

msi_data = {"shortcut": shortcut_table}

bdist_msi_options = {'data' : msi_data}
setup(
    version="0.1",
    description="student management system developed by shubham aarya",
    author="shubham aarya",
    options={'build_exe' :{'include_files' : includefiles}, "bdist_msi": bdist_msi_options,},
    executables=[
        Executable(
            script="studentmanagementsystemcomplete.py",
            base=base,
            icon='mana.ico',
        )
    ]
)
###########thank you
