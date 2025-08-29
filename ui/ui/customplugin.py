#!/usr/bin/python3
from AnyQt.QtGui import QIcon, QPixmap
from AnyQt.QtCore import pyqtProperty, pyqtSignal, Qt, QDir
from AnyQt.QtWidgets import QWidget, QLabel, QPushButton, QApplication
from AnyQt.QtDesigner import QPyDesignerCustomWidgetPlugin
from pysca.helpers import custom_widget_plugin, custom_widget
import os


class TurnButton(custom_widget('ui/torn_button2.ui')):    
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

__tornbuttonplugin = custom_widget_plugin(TurnButton, 'TurnButton', False, 'DEMO', 'customplugin')