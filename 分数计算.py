# 本作品需要安装hyc库（作者竟是我自己~）
from hyc.fraction import *
from ui_fra_cal import Ui_fra_cal
from PySide2.QtWidgets import *
import sys

class fra_cal(QMainWindow, Ui_fra_cal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # 信号与槽函数
        self.start.clicked.connect(self.calculate)

    # 开始计算
    def calculate(self):
        fra1 = fraction(int(self.deno1.text()),int(self.numer1.text()))# 第一个分数
        fra2 = fraction(int(self.deno2.text()),int(self.numer2.text()))# 第二个分数
        choose = self.method.currentText()
        if choose == '加':
            text = fra1+fra2
        elif choose == '减':
            text = fra1+fra2
        elif choose == '乘':
            text = fra1+fra2
        elif choose == '除':
            text = fra1+fra2

        # 更改文字内容
        self.result.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = fra_cal()
    sys.exit(app.exec_())