# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_analyzer.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(558, 739)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.signWords = QSpinBox(self.centralwidget)
        self.signWords.setObjectName(u"signWords")
        self.signWords.setMinimum(1)
        self.signWords.setMaximum(10)
        self.signWords.setValue(3)

        self.verticalLayout.addWidget(self.signWords)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.results = QSpinBox(self.centralwidget)
        self.results.setObjectName(u"results")
        self.results.setMinimum(1)
        self.results.setMaximum(10)
        self.results.setValue(5)

        self.verticalLayout_2.addWidget(self.results)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.formLayout.setLayout(2, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.listWidget)

        self.verticalSpacer = QSpacerItem(20, 138, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(4, QFormLayout.ItemRole.FieldRole, self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(self.centralwidget)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_2.addWidget(self.okBtn)


        self.formLayout.setLayout(5, QFormLayout.ItemRole.SpanningRole, self.horizontalLayout_2)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 558, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"longueur min", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"resulats", None))
        self.okBtn.setText(QCoreApplication.translate("MainWindow", u"OK", None))
    # retranslateUi

