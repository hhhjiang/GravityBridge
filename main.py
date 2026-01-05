import sys
import os

from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QAction, QIcon


def resource_path(relative_path):
    """
    兼容 PyInstaller 的资源路径
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    icon_path = resource_path("icon.ico")

    if not os.path.exists(icon_path):
        # 最后兜底：直接退出并提示
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.critical(
            None,
            "GravityBridge Error",
            f"icon.ico not found:\n{icon_path}"
        )
        sys.exit(1)

    tray = QSystemTrayIcon()
    tray.setIcon(QIcon(icon_path))

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
