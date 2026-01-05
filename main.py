import sys
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QAction, QIcon

def main():
    app = QApplication(sys.argv)

    tray = QSystemTrayIcon()
    tray.setIcon(QIcon())  # 没 icon 也能跑

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
