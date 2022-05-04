# Frog Game for CS4500

## Running Frog Game (NOT FOR DEVELOPERS)
### From compiled executable (WINDOWS ONLY)
1. Download the latest windows release zip from: https://github.com/Thomas-Hopkins/CS4500-FrogGame/releases
1. Extract and run `froggame.exe`

### From source (WINDOWS, MACOS, LINUX)
1. Download and install [Python 3.10.x](https://www.python.org/) If you don't already have it.
1. Download latest source release zip from: https://github.com/Thomas-Hopkins/CS4500-FrogGame/releases
1. Extract zip into a folder.
1. Run `start.bat` if on Windows or `start.sh` if on MacOS/Linux.
    - **If and only if** this has issues, please create a file named `PYTHON_PATH` with no file extension. Inside of it insert the full path to your python executable. Then retry this step.
    - Project will download dependencies and setup.
1. Game should start. Rerun `start.bat` or `start.sh` to re-launch game.

## Contributing (DEVELOPERS ONLY)
### Getting started
1. Download and install [Python](https://www.python.org/) If you don't already have it.
    -  I recommend going for 3.10.x for the latest language features but earlier versions as far back as 3.5.x may work. 
    - If you encounter issues please update to a more recent version.
1. Clone the repository onto your local computer.
    - Recommended to use: https://desktop.github.com/
    - Alternatively use Git CLI if you're familiar with git commands: https://git-scm.com/
    - Recurisvely clone to make sure to download submodules.
        - If using git CLI: `git clone --recursive https://github.com/Thomas-Hopkins/CS4500-FrogGame.git`
1. Create a Python virtual environment, and then pip install requirements-dev.txt
    - See the "[Setup & Running](#setup--running)" section for more information.
1. Never push directly to `main`. Please branch the repository, push your branch to remote, and submit a pull request.
    - This should help mitigate frequent merge conflicts.
    - Before/after you submit your pull request, if necessary, please pull and merge `main` into your branch and handle any merge conflicts. 

### Setup & Running
Automatic Steps (Recommended):
1. Run `start-dev.bat` if on Windows or `start-dev.sh` if on MacOS/Linux.

Manual Steps:
1. Create a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) to avoid dependency conflicts.
    1. Run `python -m venv .\.venv`
    1. Run `.\.venv\Scripts\activate.bat` on Windows or `source tutorial-env/bin/activate` on Mac/Linux
1. Run `python -m pip install -r requirements-dev.txt`
    - You may need to update pip `python -m pip install --upgrade pip`
1. Run `pre-commit install`
1. Run `cd source`
1. Run `python -m main`

### Building
1. Requires Nuitka, should be installed if you followed "[Setup & Running](#setup--running)."
1. Nuitka requires a C compiler to be installed and accessible. [Read more here.](https://pypi.org/project/Nuitka/)
1. Windows has a build script `build.bat` running this should produce an executable in `./build/`
    - This script's commands can be adapted for MacOS/Linux
    - By default the script produces a standalone executable and copies the resources to the folder. Including the resources directory to produce a single executable caused issues in file pathing.

### Code Style
If you are using the recommended method of running this will install and run the automatic code formatter ["Black"](https://black.readthedocs.io/en/stable/) on every commit, so that you don't have to worry about code style. If you wish to quickly auto-format your code before a commit, run `black .` in the root folder.

We will try and follow [PEP-8 style guide](https://peps.python.org/pep-0008/) as closely as possible. In particular:
- Use `snake_case` rather than `camelCase` for all identifiers and function defintions.
- Use `CapWord` for class names.
- Use `lowercase` for package/module/folder names, use `snake_case` if necessary. 
- Use **4 spaces** for indentation rather than tabs. (most code editors will automatically convert).
- Use double quotes `"` rather than single quotes `'` for strings.
- Use type hinting for function return types and parameter lists. Variable declaration type hinting is not required but encouraged.

## Team Members "Pythonic Four"
- Nilima Kafle
- Noah Gazaway
- Thomas Hopkins
- Wyatt Wolf
