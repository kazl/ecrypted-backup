#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  backup.py
#  
#  Copyright 2011 nedrigaylov <nedr@is.arz.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  получаем в командной строке путь и имя шифруемого файла

import sys
import subprocess
import string
from PyQt4 import QtGui

class Center(QtGui.QMessageBox):             
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        #self.question(self, 'cryptbackup', "Insert key storage and press OK", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
        #self.setWindowTitle('cryptbackup')
        #self.resize(250, 150)
        #self.center()

#        reply = QtGui.QMessageBox.question(self, 'Insert key storage and press OK',
#           "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

"""    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)"""

app = QtGui.QApplication(sys.argv)
qb = Center()
qb.question(Center, 'cryptbackup', "Insert key storage and press OK", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
qb.show()

sys.exit(app.exec_())



def str_to_cmdline(inp_str):
    allpar = []
    command = string.split (inp_str)[0]                 # выделили команду
    allpar.append(command)
    params_and_vals = string.split (inp_str,' --')[1:]  # получили пары ключ-значение  
    for param_and_val in params_and_vals:
        param = '--' + string.split(param_and_val)[0]   # ключ
        val = string.strip(string.join(string.split(param_and_val)[1:]),'"') # значение без кавычек    
        allpar.append(param)
        allpar.append(val) 
    return(allpar)


"""try: 
    backup_file      = sys.argv[1]
except IndexError:
    sys.exit ('not enough arguments')"""

backup_file = 'Backup-test_set-2011-11-25_16-05.tar.gz'
    
key_file                = '/media/key/key'
backup_dir              = '/home/nedr/.tmpbackup/'
ecrypted_backup_dir     = '/media/VMs/'
ecrypted_backup_file    = backup_file + '.aes-256-cbc'
kdialog_key_request     = 'kdialog --title "Backup file encryption" --yes-label "OK" --no-label "Cancel" --yesno "Insert storage or press Cancel"'
kdialog_cancel          = 'kdialog  --title "Backup file encryption" --sorry "Operation cancelled"'
kdialog_ecrypt_error    = 'kdialog --title "Backup file encryption" --error "An error occured"'
kdialog_ecrypt_ok       = 'kdialog --title "Backup file encryption" --msgbox "Done. Unmount and remove storage"'
openssl_string          = ['openssl', 'enc', '-aes-256-cbc', '-pass', 'file:' + key_file, '-in', backup_dir + backup_file, '-out', ecrypted_backup_dir + ecrypted_backup_file]

if subprocess.call(str_to_cmdline(kdialog_key_request)):
    subprocess.call(str_to_cmdline(kdialog_cancel))
else:
    if subprocess.call(openssl_string):
        subprocess.call(str_to_cmdline(kdialog_ecrypt_error))
    else:
        subprocess.call(str_to_cmdline(kdialog_ecrypt_ok))
    
    



'''kdialog_str         = """kdialog --title "Backup file encryption" --yes-label "OK" --no-label "Cancel" --yesno "src: $backupFile"
dst: $ecryptedbackupFile

Insert storage or press 'Cancel'"""'''
