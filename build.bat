@echo off
rem Build script. Requires nuitka: python -m pip install nuitka
rem Creates a standalone executable in ./build

echo Activating Python virtual environment...

call .\.venv\Scripts\activate.bat

set output=.\build
set onefile=1==1

if %onefile% (
    python -m nuitka --standalone --output-dir="%output%" --include-module="source.localization" --enable-plugin="tk-inter" --windows-disable-console --windows-icon-from-ico=".\resources\frog.ico" --onefile .\source\main.py -o "%output%\froggame.exe"
    mkdir "%output%\resources"
    xcopy ".\resources" "%output%\resources" /Y /E
    DEL "%output%\resources\sun-valley-theme\DOCUMENTATION.pdf" 
    DEL "%output%\resources\sun-valley-theme\README.md"
    DEL "%output%\resources\sun-valley-theme\Screenshot.png"
) else (
    python -m nuitka --standalone --include-data-dir=".\resources=.\resources" --output-dir="%output%" --include-module="source.localization" --enable-plugin="tk-inter" --windows-disable-console --windows-icon-from-ico=".\resources\frog.ico" .\source\main.py -o "%output%\froggame.exe"
)
