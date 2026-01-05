import sys
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMessageBox
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QCoreApplication

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    tray = QSystemTrayIcon()

    # 🔥 使用 Qt 自带的空图标，100% 不报 No Icon set
    tray.setIcon(QIcon.fromTheme("application-exit"))

    if not tray.icon().isNull():
        tray.show()
    else:
        QMessageBox.critical(
            None,
            "GravityBridge Error",
            "Tray icon failed to load"
        )
        sys.exit(1)

    menu = QMenu()

    action_start = QAction("启动 Antigravity")
    action_exit = QAction("退出")

    action_exit.triggered.connect(QCoreApplication.quit)

    menu.addAction(action_start)
    menu.addSeparator()
    menu.addAction(action_exit)

    tray.setContextMenu(menu)

    sys.exit(app.exec())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        QMessageBox.critical(None, "Fatal Error", str(e))
