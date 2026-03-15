import subprocess
import winreg
import pathlib


def open_file_dialog():

    start_dir = None
    if start_dir is None: start_dir = "[System.IO.Directory]::GetCurrentDirectory()"
    else: start_dir = f'"{start_dir}\\data"'
    PS_Commands = ""
    PS_Commands += "Add-Type -AssemblyName System.Windows.Forms;"
    PS_Commands += "$fileBrowser = New-Object System.Windows.Forms.OpenFileDialog;"
    PS_Commands += "$fileBrowser.InitialDirectory =" + str(start_dir) + ";"
    PS_Commands += "$Null = $fileBrowser.ShowDialog();"
    PS_Commands += "echo $fileBrowser.FileName"
    file_path = subprocess.run(["powershell.exe", PS_Commands], stdout=subprocess.PIPE)
    file_path = file_path.stdout.decode()
    file_path = file_path.rstrip()
    return file_path


def from_path(p: pathlib.Path) -> str:
    return str(p.absolute())
