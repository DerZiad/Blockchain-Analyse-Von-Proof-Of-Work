import os,sys

# Falls python3 oder python2, müssen Sie python nach python{Version} verändern
python_cmd="python -m pip install {}"
python_check_cmd = "python -m pip show {}"

step = "[ + ] - Installing {}"

install_package = lambda x:os.system(python_cmd.format(x))
get_step = lambda x:step.format(x)


check = lambda package:os.system(python_check_cmd.format(package))

def checkOrInstall(packages):
    os.system("python -m pip install pip --upgrade")

    # Colorama check
    code = check("colorama")
    if code == 1:
        print("[ + ] - Install colorama")
        install_package("colorama")

    from globalconfig.Writer import Writer
    writer = Writer()

    for package in packages:
        code = check(package)
        if code == 1:
            writer.writeStep(get_step(package))
            installed = install_package(package)
            if installed == 0:
                writer.writeSuccess(f"[ + ] - {package} is Installed")
            else:
                writer.writeError(f"[ - ] - Error with {package} Installation")
                sys.exit(1)
        else:
            writer.writeSuccess(f"[ + ] - {package} already installed")

