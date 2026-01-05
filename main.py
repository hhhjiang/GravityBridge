import sys
import os
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QCoreApplication


def resource_path(relative_path: str) -> str:
    """
    PyInstaller 运行时，资源会被解压到 _MEIPASS
    开发态 / 打包态 都能正确找到 icon
    """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def main():
    QCoreApplication.setApplicationName("GravityBridge")

    app = QApplication(sys.argv)

    icon_path = resource_path("icon.ico")
    if not os.path.exists(icon_path):
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.critical(None, "GravityBridge Error", f"icon.ico not found:\n{icon_path}")
        sys.exit(1)

    icon = QIcon(icon_path)

    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setToolTip("GravityBridge")

    menu = QMenu()

    action_start = QAction("启动 GravityBridge")
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
