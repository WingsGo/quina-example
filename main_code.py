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
    
%LocalAppData%\pip\Cache

# 1. 过长的函数参数另起一行
# 2. 字符串连接使用join()
# 3. 在操作符之前换行
# 4. 多个包导入应该分开书写
# 5. 包导入次序: 标准库->三方库->本地库
# 6. 推荐使用绝对导入, 模块描述内容在import之前
# 7. 冗余的行尾逗号，在最后一行添加)或]等
# 8. 包名使用小写并尽量不适用下划线,类名使用驼峰命名, 函数名与变量名使用小写+下划线
# 9. 模块应该使用__all__属性显式声明它内部所有公开API, 避免不想外部访问的模块被import
# 10. 测试一个默认为None的变量是否被赋予了其他值使用if x: 而不是if x is not None:
# 11. 使用富比较符时，需要把6个比较符全部实现，可使用functools.total_ordering子宫生成缺失的比较运算符
# 12. 从Exception类中派生异常而不是BaseException中派生(这种不能让程序在捕获后还能执行)
# 13. 捕获异常时要指明异常类型
# 14. 多条返回语句要保持一致性，即使要显示声明return None

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_path = "database.db"
engine = create_engine("sqlite:///{}".format(database_path), echo=True)
Base = declarative_base()


def create_table():
    Base.metadata.create_all(engine)


def create_session():
    create_table()
    session = sessionmaker(bind=engine)
    return session()
