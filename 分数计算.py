# 本作品需要安装hyc库（作者竟是我自己~）
from hyc.fraction import fra_ad, fra_sub, fra_divi, fra_mult
from ui_fra_cal import Ui_fra_cal
from PySide2.QtWidgets import *
import sys

class fra_cal(QMainWindow, Ui_fra_cal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        # 相对应的选择给出相对应的方法
        self.method_dict = {'加':fra_ad, '减':fra_sub, '乘':fra_mult, '除':fra_divi}

        # 信号与槽函数
        self.start.clicked.connect(self.calculate)

    # 开始计算
    def calculate(self):
        try:
            fra_list=[[int(self.deno1.text()),
                       int(self.numer1.text())],# 第一个分数
                     [int(self.deno2.text()),
                      int(self.numer2.text())]]# 第二个分数
            choose = self.method.currentText()
            method = self.method_dict[choose]
            if method == fra_ad or method == fra_mult:
                result = method(fra_list)
            else:
                result = method(fra_list[0], [fra_list[1]])

            # 更改文字内容
            self.result.setText('{}分之{}'.format(result[0], result[1]))
        except:
            QMessageBox.warning(self, '请注意', '请先填入两个分数的分子和分母或修改分子和分母为数字')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = fra_cal()
    sys.exit(app.exec_())