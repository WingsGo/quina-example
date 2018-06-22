from quina.widgets import *
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide2.QtWidgets import QSizePolicy

pyside2_plugins = os.path.join(os.path.dirname(PySide2.__file__), "plugins")
QtWidgets.QApplication.addLibraryPath(pyside2_plugins)

class MainWindowController:
    def __init__(self, parent=None):
        self.setup_ui(parent)

    def setup_ui(self, parent):
        self.main_window = MainWindow(parent)
        self.main_window.resize(800, 600)
        self.main_widget = Widget(self.main_window)
        self.main_window.set_central_widget(self.main_widget)
        self.main_h_layout = QHBoxLayout(self.main_widget)

        self.group_box = GroupBox(self.main_widget)
        v_layout = QVBoxLayout(self.group_box)
        h_layout = QHBoxLayout()
        self.label = Label('test', self.group_box)
        self.edit = LineEdit(self.group_box)
        h_layout.addWidget(self.label)
        h_layout.addWidget(self.edit)
        v_layout.addLayout(h_layout)

        self.group_box2 = GroupBox(self.main_widget)

        self.group_v_layout = QVBoxLayout()
        self.group_v_layout.addWidget(self.group_box)
        self.group_v_layout.addWidget(self.group_box2)

        self.group_box3 = GroupBox(self.main_widget)
        self.group_box3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        self.main_h_layout.addLayout(self.group_v_layout)
        self.main_h_layout.addWidget(self.group_box3)

    def main(self):
        return self.main_window.exec()


if __name__ == '__main__':
    controller = MainWindowController()
    controller.main()
