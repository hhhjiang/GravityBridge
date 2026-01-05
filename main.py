import sys
import os
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QAction, QIcon


def resource_path(relative_path):
    """
    PyInstaller 打包后正确获取资源路径
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def main():
    app = QApplication(sys.argv)

    icon_path = resource_path("icon.ico")
    tray_icon = QSystemTrayIcon(QIcon(icon_path))

    menu = QMenu()

    action_start = QAction("启动 Antigravity")
    action_exit = QAction("退出")

    action_exit.triggered.connect(app.quit)

    menu.addAction(action_start)
    menu.addSeparator()
    menu.addAction(action_exit)

    tray_icon.setContextMenu(menu)
    tray_icon.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
