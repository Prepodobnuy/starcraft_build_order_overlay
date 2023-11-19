import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QScrollArea, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor, QIcon

import os
from builds import find_builds, download_build


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Build Select")
        self.setWindowIcon(QIcon("../../assets/logo.png"))
        self.setGeometry(0, 0, 400, 300)
        self.setFixedWidth(540)
        self.setFixedHeight(220)

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.WindowText, QColor(200, 200, 200))
        palette.setColor(QPalette.Base, QColor(15, 15, 15))
        palette.setColor(QPalette.AlternateBase, QColor(40, 40, 40))
        palette.setColor(QPalette.ToolTipBase, QColor(200, 200, 200))
        palette.setColor(QPalette.ToolTipText, QColor(200, 200, 200))
        palette.setColor(QPalette.Text, QColor(200, 200, 200))
        palette.setColor(QPalette.Button, QColor(40, 40, 40))
        palette.setColor(QPalette.ButtonText, QColor(200, 200, 200))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

        self.setPalette(palette)

        # variables

        self.builds_path: str = "../../data/builds"
        self.installed_builds: list = []
        self.installed_build_names: list = []

        self.online_builds: list = []
        self.online_build_names: list = []

        self.your = "Any"
        self.enemy = "Any"

        # Создание виджета вкладок
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.get_installed_builds_list()

        self.place_offline_widgets()
        self.place_online_widgets()

    def get_installed_builds_list(self) -> None:
        self.installed_builds = []
        self.installed_build_names = []

        for build in os.listdir(self.builds_path):
            if '.txt' in build:
                self.installed_builds.append(build)
                self.installed_build_names.append(build.split('.')[0])

    def select_offline_build(self, index:int) -> None:
        for i in range(len(self.installed_build_names)):
            if self.installed_build_names[i] == "Selected":
                self.installed_build_names[i] = self.installed_builds[i].split('.')[0]
                break
        
        with open("../../data/selected_build", "w+") as file:
            file.write(self.installed_builds[index])

        self.installed_build_names[index] = "Selected"

        self.delete_tabs()

        self.place_offline_widgets()
        self.place_online_widgets()
    
    def delete_offline_build(self, index:int) -> None:
        if self.installed_builds[index] in os.listdir(self.builds_path):
            os.remove(self.builds_path + '/' + self.installed_builds[index])
            self.installed_builds.pop(index)
            self.installed_build_names.pop(index)

        self.delete_tabs()

        self.place_offline_widgets()
        self.place_online_widgets()

    def delete_tabs(self):
        self.tab_widget.removeTab(0)
        self.tab_widget.removeTab(0)

    def place_offline_widgets(self):
        # first tab creation
        self.offline_tab = QWidget()
        self.tab_widget.addTab(self.offline_tab, "Installed Builds")
        self.offline_layout = QVBoxLayout()
        self.offline_tab.setLayout(self.offline_layout)

        self.offline_scroll_area = QScrollArea()
        self.offline_scroll_area.setWidgetResizable(True)
        self.offline_tab.setLayout(QVBoxLayout())
        self.offline_tab.layout().addWidget(self.offline_scroll_area)
        self.scroll_content_widget = QWidget()
        self.offline_scroll_area.setWidget(self.scroll_content_widget)
        self.scroll_content_widget.setLayout(QVBoxLayout())

        if self.installed_build_names != []:
            for index, name in enumerate(self.installed_build_names):
                button_layout_offline = QHBoxLayout()
                button = QPushButton(name)
                delete_button = QPushButton("Delete")
                delete_button.setFixedSize(50,35)

                button.clicked.connect(lambda checked, i=index: self.select_offline_build(i))
                delete_button.clicked.connect(lambda checked, i=index: self.delete_offline_build(i))

                button_layout_offline.addWidget(button)
                button_layout_offline.addWidget(delete_button)

                self.scroll_content_widget.layout().addLayout(button_layout_offline)

    def place_online_widgets(self):
        # second tab creation
        self.online_tab = QWidget()

        self.tab_widget.addTab(self.online_tab, "Browse Builds")
        self.online_tab.setLayout(QHBoxLayout())

        self.online_scroll_area = QScrollArea()
        self.online_scroll_area.setWidgetResizable(True)
        self.online_tab.setLayout(QVBoxLayout())
        self.online_tab.layout().addWidget(self.online_scroll_area)
        self.scroll_content_widget = QWidget()
        self.online_scroll_area.setWidget(self.scroll_content_widget)
        self.scroll_content_widget.setLayout(QVBoxLayout())

        if self.online_build_names != []:
            for index, name in enumerate(self.online_build_names):
                button_layout_online = QHBoxLayout()
                button = QPushButton(name)

                button.clicked.connect(lambda checked, i=index: self.install_online_build(i))
                #button.setFixedWidth(220)

                button_layout_online.addWidget(button)

                self.scroll_content_widget.layout().addLayout(button_layout_online)

        def your_change_caption():
            print(self.your_race.text())
            if self.your_race.text() == "Zerg":
                self.your_race.setText("Any")
            elif self.your_race.text() == "Terran":
                self.your_race.setText("Zerg")
            elif self.your_race.text() == "Protoss":
                self.your_race.setText("Terran")
            elif self.your_race.text() == "Any":
                self.your_race.setText("Protoss")
            else:
                self.your_race.setText("Protoss")
            self.your = self.your_race.text()
            
        def enemy_change_caption():
            if self.enemy_race.text() == "Zerg":
                self.enemy_race.setText("Any")
            elif self.enemy_race.text() == "Terran":
                self.enemy_race.setText("Zerg")
            elif self.enemy_race.text() == "Protoss":
                self.enemy_race.setText("Terran")
            elif self.enemy_race.text() == "Any":
                self.enemy_race.setText("Protoss")
            else:
                self.enemy_race.setText("Protoss")
            self.enemy = self.enemy_race.text()
            print(self.enemy)

        matchupLayout = QVBoxLayout()

        self.your_race = QPushButton("Your race")
        self.your_race.clicked.connect(your_change_caption)
        self.your_race.setFixedWidth(100)

        self.enemy_race = QPushButton("Enemy race")
        self.enemy_race.clicked.connect(enemy_change_caption)
        self.enemy_race.setFixedWidth(100)

        self.load_online_builds_buttons = QPushButton("Find Builds")
        self.load_online_builds_buttons.clicked.connect(self.found_builds)
        self.load_online_builds_buttons.setFixedWidth(100)

        matchupLayout.addWidget(self.your_race)
        matchupLayout.addWidget(self.enemy_race)
        matchupLayout.addWidget(self.load_online_builds_buttons)

        self.online_tab.layout().addLayout(matchupLayout)
    
    def found_builds(self):
        self.online_builds, self.online_build_names = [], []
        self.online_build_names, self.online_builds = find_builds("Protoss", "Terran")

        self.delete_tabs()

        self.place_online_widgets()
        self.place_offline_widgets()
    
    def install_online_build(self, index):
        download_build(self.online_build_names, self.online_builds, self.builds_path, index)
        self.online_build_names.pop(index)
        self.online_builds.pop(index)

        self.delete_tabs()

        self.place_online_widgets()
        self.place_offline_widgets()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())