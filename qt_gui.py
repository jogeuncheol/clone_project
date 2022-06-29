import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 푸시 버튼 생성
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        # PyQt5에서 이벤트 처리는 시그널과 슬롯 메커니즘
        # 버튼을 클릭하면 'clicked' 시그널이 만들어짐
        # 'clicked' 시그널은 quit() 메서드에 연결됨
        # Sender 와 Receiver 두 객체 간에 커뮤니케이션이 이루어짐
        # 여기서 Sender 는 푸시버튼(btn),
        # Receiver 는 어플리케이션 객체 (app)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('My First Application')
        self.setGeometry(300, 300, 300, 200)
        # self.move(300, 300)
        # self.resize(400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
