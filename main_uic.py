from quina.widgets import MainWindow, GroupBox, Label, LineEdit, Widget, PushButton
from main_window import Ui_MainWindow


class MainWindowController(Ui_MainWindow):
    def __init__(self, parent=None):
        self.parent = parent
        self.ui = MainWindow()
        self.setupUi(self.ui)
        self.label.string.value = 'Label'

    def main(self):
        self.ui.exec()


if __name__ == '__main__':
    w = MainWindowController()
    w.main()
