import sys
import os
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction

def resource_path(filename):
    # PyInstaller 兼容路径
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    icon_path = resource_path("icon.ico")
    tray = QSystemTrayIcon(QIcon(icon_path))

    menu = QMenu()

    action_start = QAction("启动 Antigravity")
    action_exit = QAction("退出")

    action_exit.triggered.connect(app.quit)

    menu.addAction(action_start)
    menu.addSeparator()
    menu.addAction(action_exit)

    tray.setContextMenu(menu)
    tray.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
