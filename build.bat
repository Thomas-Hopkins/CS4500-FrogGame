@echo off
rem Build script. Requires nuitka: python -m pip install nuitka
rem Creates a standalone executable in ./build

echo Activating Python virtual environment...

call .\.venv\Scripts\activate.bat

set output=.\build
set onefile=1==1

if %onefile% (
    python -m nuitka --standalone --output-dir="%output%" --include-module="source.localization" --enable-plugin="tk-inter" --onefile .\source\main.py
    mkdir "%output%\resources"
    xcopy ".\resources" "%output%\resources" /Y /E
    DEL "%output%\resources\sun-valley-theme\DOCUMENTATION.pdf" 
    DEL "%output%\resources\sun-valley-theme\README.md"
    DEL "%output%\resources\sun-valley-theme\Screenshot.png"
) else (
    python -m nuitka --standalone --include-data-dir=".\source\gui\Sun-Valley-ttk-theme=.\gui\Sun-Valley-ttk-theme" --include-data-dir=".\resources=.\resources" --output-dir="%output%" --include-module="source.localization" --enable-plugin="tk-inter" .\source\main.py
)
