#!/usr/bin/python3
from AnyQt.QtGui import QIcon
from AnyQt.QtWidgets import QWidget
from AnyQt.QtDesigner import QPyDesignerCustomWidgetPlugin
from pysca.helpers import custom_widget_plugin,custom_widget

AUGER_PANEL = custom_widget_plugin('ui/AUGER_CTRL.ui','AUGER_CTRL',False,'PYSCA','customplugin')

