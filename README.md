# 分数计算介绍

## 介绍
分数计算是根据hyc库中有关分数计算的内容进行优化使用体验产生的软件

## 使用方法

### 请注意：使用之前请安装PySide2库，并下载该目录下的ui_fra_cal.py文件

#### 1.
点击运行之后，看到这个界面
```
分母                分母
 [   ]   [加 > ]   [    ]
分子                分子
 [   ]   [开始计算] [    ]
```
#### 2.
输入两个分数的分子以及分母

#### 3.
点击“[ 加> ]”选择运算方法

#### 4.
点击“开始计算”，如有报错，请根据报错内容进行修改。具体见“报错可能”

## 报错可能

#### 1.减法出错
可能是被减数<减数

#### 2.填入类型错误
可能是填入的元素为浮点数（小数）或字符串以及其它类型

#### 3.有关0的错误
可能是在填入的四个数字里面有至少一个为0

#### 4.未填入数字错误
可能是有至少一个数字未填入