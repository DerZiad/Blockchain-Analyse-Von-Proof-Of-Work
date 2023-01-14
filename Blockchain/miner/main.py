from globalconfig.Installer import checkOrInstall
from window import *

packages = ["psutil","gputil","tabulate","PyQt5","pyqt5-tools","pyqt5-plugins","sip","PyQtChart"]
checkOrInstall(packages)


if __name__ == "__main__":
    launch()
