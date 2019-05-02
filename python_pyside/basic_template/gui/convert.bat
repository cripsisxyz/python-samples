SET mypath=%~dp0
cmd.exe /c "pyside-uic.exe %mypath%ventana.ui -o %mypath%ventana.py"