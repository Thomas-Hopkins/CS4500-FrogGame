@echo off
rem Build script. Requires nuitka: python -m pip install nuitka
rem Creates a standalone executable in ./build

echo Activating Python virtual environment...

call .\.venv\Scripts\activate.bat

set output=.\build
set onefile=1==1

if %onefile% (
    python -m nuitka --standalone --output-dir="%output%" --include-module="localization" --enable-plugin="tk-inter" --onefile .\source\main.py
    mkdir "%output%\resources"
    xcopy ".\resources" "%output%\resources" /Y /E
    mkdir "%output%\gui\Sun-Valley-ttk-theme"
    xcopy ".\source\gui\Sun-Valley-ttk-theme" "%output%\gui\Sun-Valley-ttk-theme" /Y /E
) else (
    python -m nuitka --standalone --include-data-dir=".\source\gui\Sun-Valley-ttk-theme=.\gui\Sun-Valley-ttk-theme" --include-data-dir=".\resources=.\resources" --output-dir="%output%" --include-module="localization" --enable-plugin="tk-inter" .\source\main.py
)
