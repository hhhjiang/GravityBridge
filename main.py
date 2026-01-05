import sys
import subprocess
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PySide6.QtGui import QIcon

APP_NAME = "GravityBridge"
ANTIGRAVITY_EXE = "Antigravity.exe"  # 你电脑里真实的 Antigravity 路径稍后再优化

def start_antigravity():
    try:
        subprocess.Popen([ANTIGRAVITY_EXE], shell=True)
    except Exception as e:
        print(e)

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

tray = QSystemTrayIcon()
tray.setToolTip(APP_NAME)
tray.setIcon(QIcon())  # 后面再加 Logo

menu = QMenu()

start_action = QAction("启动 Antigravity")
start_action.triggered.connect(start_antigravity)
menu.addAction(start_action)

exit_action = QAction("退出")
exit_action.triggered.connect(app.quit)
menu.addAction(exit_action)

tray.setContextMenu(menu)
tray.show()

sys.exit(app.exec())
