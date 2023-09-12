import sys
from PyQt5 import QtWidgets
import math
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from matplotlib import pyplot as plt
from inter import Ui_MainWindow
import pandas as pd
df = pd.read_csv("Year_2016.csv", sep=",")
dfl=len(df)
dfc=len(df.columns)
dfd=df.describe()
srez=df.iloc[30:50]
sum1=df['Trust (Government Corruption)'].sum()
sort=df.head(100).sort_values(by='Lower Confidence Interval')
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Лабораторная 8")
        self.ui.Button1.clicked.connect(self.btnClick1)
        self.ui.Button2.clicked.connect(self.close_application)
        self.ui.Button3.clicked.connect(self.btnClick3)
        self.ui.Button4.clicked.connect(self.btnClick4)
        self.ui.Button5.clicked.connect(self.btnClick5)
        self.ui.Button6.clicked.connect(self.btnClick6)
        self.ui.Button7.clicked.connect(self.btnClick7)
        self.ui.Button8.clicked.connect(self.btnClick8)
    def btnClick3(self):
        self.ui.label_3.setText(str(dfd))
    def close_application(self):
        sys.exit()
    def btnClick8(self):
        x = df['Dystopia Residual']
        y = df['Generosity']
        plt.plot(x, y, color='red', marker='o', linestyle='', label='Соотнощение')
        plt.legend(loc='best')
        plt.title('График доверия', fontsize=14)
        plt.xlabel('Dystopia Residual', fontsize=14)
        plt.ylabel('Generosity', fontsize=14)
        plt.grid(True)
        plt.show()
    def btnClick1(self):
        self.ui.label.setText(str(dfl))
        self.ui.label_2.setText(str(dfc))
    def btnClick5(self):
        self.ui.label_3.setText(str(srez))
    def btnClick6(self):
        self.ui.label_3.setText(str(sort))
    def btnClick7(self):
        self.ui.label_3.setText(str(sum1))
    def btnClick4(self):
        self.ui.label_3.setText(str(df))
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())