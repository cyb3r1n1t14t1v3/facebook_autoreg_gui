# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerjBOiSL.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QVariantAnimation, QAbstractAnimation, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_logs(QWidget):
    def setupUi(self, logs):
        if not logs.objectName():
            logs.setObjectName(u"logs_window")
        logs.resize(840, 580)
        self.logs_textEdit = QTextEdit(logs)
        self.logs_textEdit.setObjectName(u"logs_textEdit")
        self.logs_textEdit.setGeometry(QRect(0, 0, 840, 400))
        self.logs_textEdit.setMinimumSize(QSize(840, 400))
        self.logs_textEdit.setMaximumSize(QSize(840, 400))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setBold(True)
        self.logs_textEdit.setFont(font)
        self.logs_textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.logs_textEdit.setAutoFillBackground(False)
        self.logs_textEdit.setStyleSheet(u"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;")
        self.logs_textEdit.setReadOnly(True)
        self.logs_bar = QWidget(logs)
        self.logs_bar.setObjectName(u"logs_bar")
        self.logs_bar.setGeometry(QRect(0, 400, 840, 180))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logs_bar.sizePolicy().hasHeightForWidth())
        self.logs_bar.setSizePolicy(sizePolicy)
        self.logs_bar.setMinimumSize(QSize(840, 180))
        self.logs_bar.setMaximumSize(QSize(840, 180))
        self.logs_bar.setStyleSheet(u"#logs_bar {\n"
"   border-top: 4px solid #16e0ff;\n"
"   border-bottom-left-radius: 8px;\n"
"   border-bottom-right-radius: 8px;\n"
"   background-color: #0a0a0a;\n"
"}\n"
"\n"
"#logs_bar QLabel {\n"
"   background-position: center;\n"
"   background-repeat: no-repeat;\n"
"   background-origin: content;\n"
"   background-color: #0a0a0a;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.logs_bar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.delete_label = LogsBarLabel(self.logs_bar)
        self.delete_label.setObjectName(u"delete_label")
        self.delete_label.setMinimumSize(QSize(48, 48))
        self.delete_label.setMaximumSize(QSize(48, 48))
        self.delete_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_label.setAutoFillBackground(False)
        self.delete_label.setStyleSheet(u"background-image: url(:/images/icons/delete_32.png);")

        self.gridLayout_2.addWidget(self.delete_label, 0, 1, 1, 1)

        self.save_label = LogsBarLabel(self.logs_bar)
        self.save_label.setObjectName(u"save_label")
        self.save_label.setMinimumSize(QSize(48, 48))
        self.save_label.setMaximumSize(QSize(48, 48))
        self.save_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_label.setAutoFillBackground(False)
        self.save_label.setStyleSheet(u"background-image: url(:/images/icons/save_32.png);")

        self.gridLayout_2.addWidget(self.save_label, 0, 0, 1, 1)

        self.devider1 = QLabel(self.logs_bar)
        self.devider1.setObjectName(u"devider1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.devider1.sizePolicy().hasHeightForWidth())
        self.devider1.setSizePolicy(sizePolicy1)
        self.devider1.setMinimumSize(QSize(4, 150))
        self.devider1.setMaximumSize(QSize(4, 150))
        self.devider1.setStyleSheet(u"#devider1 {\n"
"   border-radius: 2px;\n"
"   background-color: #dcdcdc;\n"
"}")

        self.gridLayout_2.addWidget(self.devider1, 0, 2, 1, 1)

        self.status = QWidget(self.logs_bar)
        self.status.setObjectName(u"status")
        sizePolicy1.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy1)
        self.status.setMinimumSize(QSize(500, 0))
        self.status.setMaximumSize(QSize(420, 16777215))
        self.status.setStyleSheet(u"#status {\n"
"   background-color: #0a0a0a;\n"
"}\n"
"\n"
"#status QLabel {\n"
"   font-size: 19px;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.status)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.status_label = QLabel(self.status)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMinimumSize(QSize(230, 0))
        self.status_label.setMaximumSize(QSize(230, 16777215))
        self.status_label.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout.addWidget(self.status_label)

        self.passed_time_label = QLabel(self.status)
        self.passed_time_label.setObjectName(u"passed_time_label")
        self.passed_time_label.setMinimumSize(QSize(0, 0))
        self.passed_time_label.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout.addWidget(self.passed_time_label, 0, Qt.AlignLeft)

        self.label = QLabel(self.status)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.devider2 = QLabel(self.status)
        self.devider2.setObjectName(u"devider2")
        self.devider2.setMinimumSize(QSize(0, 2))
        self.devider2.setMaximumSize(QSize(16777215, 2))
        self.devider2.setStyleSheet(u"background-color: #dcdcdc;")

        self.verticalLayout.addWidget(self.devider2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.status_data = QLabel(self.status)
        self.status_data.setObjectName(u"status_data")
        self.status_data.setEnabled(True)
        self.status_data.setMinimumSize(QSize(230, 0))
        self.status_data.setMaximumSize(QSize(230, 16777215))
        self.status_data.setLayoutDirection(Qt.LeftToRight)
        self.status_data.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.status_data)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.status_value = QLabel(self.status)
        self.status_value.setObjectName(u"status_value")
        self.status_value.setEnabled(True)
        self.status_value.setMinimumSize(QSize(0, 0))
        self.status_value.setLayoutDirection(Qt.LeftToRight)
        self.status_value.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.status_value)

        self.status_changed_value = QLabel(self.status)
        self.status_changed_value.setObjectName(u"status_changed_value")
        self.status_changed_value.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.status_changed_value)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.status, 0, 3, 1, 1)


        self.retranslateUi(logs)

        QMetaObject.connectSlotsByName(logs)
    # setupUi

    def retranslateUi(self, logs):
        logs.setWindowTitle(QCoreApplication.translate("logs", u"Form", None))
        self.logs_textEdit.setHtml(QCoreApplication.translate("logs", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px; font-weight:800;\"><br /></p></body></html>", None))
        self.delete_label.setText("")
        self.save_label.setText("")
        self.devider1.setText("")
        self.status_label.setText(QCoreApplication.translate("logs", u"STATUS", None))
        self.passed_time_label.setText(QCoreApplication.translate("logs", u"ELAPSED TIME", None))
        self.label.setText(QCoreApplication.translate("logs", u"00:00:00", None))
        self.devider2.setText("")
        self.status_data.setText(QCoreApplication.translate("logs", u"ALL     EMAILS\n"
"ALL     ACCOUNTS\n"
"VALID   ACCOUNTS\n"
"INVALID ACCOUNTS", None))
        self.status_value.setText(QCoreApplication.translate("logs", u"0\n"
"0\n"
"0\n"
"0", None))
        self.status_changed_value.setText(QCoreApplication.translate("logs", u"-0\n"
"+0\n"
"+0\n"
"+0", None))
    # retranslateUi

class LogsBarLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self._animation = QVariantAnimation(
            startValue=QColor("#1a1a1a"),
            endValue=QColor("#0a0a0a"),
            duration=250,
        )
        self._animation.valueChanged.connect(self._update_stylesheet)

    def _update_stylesheet(self, color):
        match self.objectName():
            case "save_label":
                image_path = ":/images/icons/save_32.png"
            case "delete_label":
                image_path = ":/images/icons/delete_32.png"

        self.setStyleSheet("""
            QLabel{
                background-color: %s;
                border-radius: 24px;
                background-image: url(%s);
            }
        """
            % (color.name(), image_path)
        )

    def enterEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Backward)
        self._animation.start()

        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QAbstractAnimation.Forward)
        self._animation.start()

        super().leaveEvent(event)