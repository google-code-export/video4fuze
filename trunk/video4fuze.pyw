#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Copyright 2009-2010 Adrián Cereto Massagué <ssorgatem@esdebian.org>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import sys
import info
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QTranslator, QString, QLocale
from GUI.MainWindow import MainWindow

def main():
    """
    Main function: starts video4fuze
    """
    translator = QTranslator() #Build the translator
    translator.load(QString("translations/v4f_%1").arg(QLocale.system().name())) #Path to v4f's translation files
    qttranslator = QTranslator()#A translator for Qt standard strings
    qttranslator.load(QString("qt_%1").arg(QLocale.system().name()))
    Vapp = QApplication(sys.argv[1:]) #Creating the app
    Vapp.setOrganizationName(info.ORGNAME) #Setting organization and application's
    Vapp.setApplicationName(info.NAME)#name. It's only useful for QSettings
    Vapp.setApplicationVersion(info.VERSION)
    Vapp.installTranslator(translator)#Install translators into the application.
    Vapp.installTranslator(qttranslator)
    VentanaP = MainWindow(sys.argv[1:]) #Now it's time to instantiate the main window
    VentanaP.show() #And show it
    sys.exit(Vapp.exec_()) #When the app finishes, exit.

#def Setup():
#    """
#    Setup the Qapplication, translators and properties used to load settings
#    """


if __name__ == "__main__":
    main()