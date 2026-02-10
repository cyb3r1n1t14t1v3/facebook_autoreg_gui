# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowfNWzfK.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QVariantAnimation, QAbstractAnimation, QParallelAnimationGroup, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, 
    QSize, QTime, QUrl, Qt, Signal, Property)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QMouseEvent, QHoverEvent)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QSizePolicy, QWidget)
from gui import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 600)
        MainWindow.setMinimumSize(QSize(980, 600))
        MainWindow.setMaximumSize(QSize(980, 600))
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/images/icons/account_24.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"* {\n"
"   font-family: Consolas;\n"
"   font-weight: bold;\n"
"   color: #dcdcdc;\n"
"   font-size: 15px;\n"
"}\n"
"\n"
"QMainWindow, QWidget {\n"
"   background-color: #111111;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #16e0ff;\n"
"    color: #111111;\n"
"   border: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00b3b3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #008080;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 4px;\n"
"    background-color: #dcdcdc;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #16e0ff;\n"
"    border: none;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #16e0ff;\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    background-color: #16"
                        "E0FF;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #16E0FF;\n"
"    border: 1px solid #16E0FF;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: #dcdcdc;\n"
"    border: 1px solid #16E0FF;\n"
"}\n"
"\n"
"QTextEdit, QLineEdit {\n"
"   background-color: #dcdcdc;\n"
"   font-size: 18px;\n"
"   border: none;\n"
"   color: #111111;\n"
"}\n"
"\n"
"QLineEdit {\n"
"   font-size: 15px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #dcdcdc;\n"
"    width: 15px;\n"
"    margin: 15px 0 15px 0;\n"
"}\n"
"    \n"
"QScrollBar::handle:vertical {\n"
"    background: #16e0ff;\n"
"    min-height: 20px;\n"
"}\n"
"    \n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #dcdcdc;\n"
"}\n"
"    \n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"   background: #dcdcdc;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #16E0FF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #16E0F"
                        "F;\n"
"    outline: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid #16E0FF;\n"
"    border-radius: 2px;\n"
"    background-color: #dcdcdc;\n"
"   color: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #16E0FF;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #16E0FF;\n"
"    border-top-right-radius: 2px;\n"
"   border-top-left-radius: 2px;\n"
"    padding: 2px;\n"
"    background-color: #dcdcdc;\n"
"    color: #111111;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #16E0FF;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #16E0FF;\n"
"    border-top-right-radius: 2px;\n"
"    background: #16E0FF;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/images/icons/plus_16.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #16E0FF;\n"
"    background-color: #dcdcdc;\n"
"    color: #111111;"
                        "\n"
"   outline: 0;\n"
"}\n"
"\n"
"QComboBox QListView::item:selected {\n"
"    background-color: #16E0FF;\n"
"    color: #111111;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #DCDCDC;\n"
"    color: #111111;\n"
"    padding: 2px 4px;\n"
"    border-bottom: 2px solid #16E0FF;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #16E0FF;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(860, 0, 120, 600))
        self.sidebar.setMinimumSize(QSize(120, 600))
        self.sidebar.setMaximumSize(QSize(120, 600))
        self.sidebar.setStyleSheet(u"#sidebar {\n"
"   background-color: #0a0a0a;\n"
"}\n"
"\n"
"#sidebar QLabel {\n"
"   background-position: center;\n"
"   background-repeat: no-repeat;\n"
"   background-origin: content;\n"
"   background-color: #0a0a0a;\n"
"}")
        self.gridLayout = QGridLayout(self.sidebar)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")

        self.start_label = SideBarMenu(self.sidebar)
        self.start_label.setObjectName(u"start_label")
        self.start_label.setMinimumSize(QSize(84, 84))
        self.start_label.setMaximumSize(QSize(84, 84))
        self.start_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_label.setAutoFillBackground(False)
        self.start_label.setStyleSheet(u"background-image: url(:/images/icons/star_64.png);")

        self.gridLayout.addWidget(self.start_label, 1, 0, 1, 1)

        self.exit_label = SideBarMenu(self.sidebar)
        self.exit_label.setObjectName(u"exit_label")
        self.exit_label.setMinimumSize(QSize(84, 84))
        self.exit_label.setMaximumSize(QSize(84, 84))
        self.exit_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.exit_label.setAutoFillBackground(False)
        self.exit_label.setStyleSheet(u"background-image: url(:/images/icons/block_64.png);")

        self.gridLayout.addWidget(self.exit_label, 5, 0, 1, 1)

        self.settings_label = SideBarMenu(self.sidebar)
        self.settings_label.setObjectName(u"settings_label")
        self.settings_label.setMinimumSize(QSize(84, 84))
        self.settings_label.setMaximumSize(QSize(84, 84))
        self.settings_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_label.setAutoFillBackground(False)
        self.settings_label.setStyleSheet(u"background-image: url(:/images/icons/setting_64.png);")

        self.gridLayout.addWidget(self.settings_label, 3, 0, 1, 1)

        self.logs_label = SideBarMenu(self.sidebar)
        self.logs_label.setObjectName(u"logs_label")
        self.logs_label.setMinimumSize(QSize(84, 84))
        self.logs_label.setMaximumSize(QSize(84, 84))
        self.logs_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.logs_label.setAutoFillBackground(False)
        self.logs_label.setStyleSheet(u"background-image: url(:/images/icons/file_64.png);")

        self.gridLayout.addWidget(self.logs_label, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SpectralX", None))
        self.start_label.setText("")
        self.exit_label.setText("")
        self.settings_label.setText("")
        self.logs_label.setText("")
    # retranslateUi

class SideBarMenu(QLabel):
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
            case "start_label":
                image_path = ":/images/icons/star_64.png"
            case "logs_label":
                image_path = ":/images/icons/file_64.png"
            case "settings_label":
                image_path = ":/images/icons/setting_64.png"
            case "exit_label":
                image_path = ":/images/icons/block_64.png"

        self.setStyleSheet("""
            QLabel{
                background-color: %s;
                border-radius: 42px;
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

    def mousePressEvent(self, event):
        if self.objectName() == "exit_label":
            self.window().close()
            return

        for elem in list(self.window().findChildren(QWidget)):
            if "window" in elem.objectName():
                elem.setFixedSize(0, 0)

        window = self.window().findChild(QWidget, f"{self.objectName().split('_')[0]}_window")
        window.setFixedSize(840, 580)