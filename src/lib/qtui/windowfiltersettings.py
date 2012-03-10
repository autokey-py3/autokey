#!/usr/bin/env python
# coding=UTF-8
#
# Generated by pykdeuic4 from windowfiltersettings.ui on Sat Mar 10 15:51:01 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(425, 120)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.triggerRegexLineEdit = KLineEdit(Form)
        self.triggerRegexLineEdit.setUrlDropsEnabled(False)
        self.triggerRegexLineEdit.setProperty("showClearButton", True)
        self.triggerRegexLineEdit.setObjectName(_fromUtf8("triggerRegexLineEdit"))
        self.horizontalLayout.addWidget(self.triggerRegexLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.recursiveCheckBox = QtGui.QCheckBox(Form)
        self.recursiveCheckBox.setObjectName(_fromUtf8("recursiveCheckBox"))
        self.verticalLayout.addWidget(self.recursiveCheckBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.detectButton = QtGui.QPushButton(Form)
        self.detectButton.setObjectName(_fromUtf8("detectButton"))
        self.horizontalLayout_2.addWidget(self.detectButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.kseparator = KSeparator(Form)
        self.kseparator.setObjectName(_fromUtf8("kseparator"))
        self.verticalLayout.addWidget(self.kseparator)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(kdecore.i18n(_fromUtf8("Form")))
        self.label_2.setText(kdecore.i18n(_fromUtf8("Regular expression to match:")))
        self.triggerRegexLineEdit.setToolTip(kdecore.i18n(_fromUtf8("Window title")))
        self.triggerRegexLineEdit.setWhatsThis(kdecore.i18n(_fromUtf8("Enter a regular expression that matches the title of windows in which you want this item to trigger.")))
        self.recursiveCheckBox.setText(kdecore.i18n(_fromUtf8("Apply recursively to subfolders and items")))
        self.detectButton.setText(kdecore.i18n(_fromUtf8("Detect Window Properties")))

from PyKDE4.kdeui import KSeparator, KLineEdit
