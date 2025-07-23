#!/usr/bin/python3
from AnyQt.QtGui import QIcon
from AnyQt.QtWidgets import QWidget
from AnyQt.QtDesigner import QPyDesignerCustomWidgetPlugin
from pysca.helpers import custom_widget_plugin,custom_widget

# class CtlGen(custom_widget('ui/ctlgen.ui')):
__ctlgenplugin = custom_widget_plugin('ui/ctlgen.ui','CtlGen',False,'DEMO','customplugin')

