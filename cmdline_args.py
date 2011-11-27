#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GNU GPL
# Цель данного файла - добиться запуска kdialog с аргументами. 


def cmdline_to_x3():    
    import string
    inp_str = 'kdialog --title "Backup file encryption" --yes-label "OK" --no-label "Cancel" --yesno "Insert storage or press Cancel. src, dst:"'
    
    allpar = []
    command = string.split (inp_str)[0]                 # выделили команду
    allpar.append(command)
    params_and_vals = string.split (inp_str,' --')[1:]  # получили пары ключ-значение  
    for param_and_val in params_and_vals:
        param = ' --' + string.split(param_and_val)[0]   # ключ
        val = string.strip(string.join(string.split(param_and_val)[1:]),'"') # значение без кавычек
        #print (string.split(param_and_val))
        
        allpar.append(param)
        allpar.append(val)
        
         
        
    print (allpar)
    
def wtf():
    backup_file = 'Backup-test_set-2011-11-25_16-05.tar.gz'
    
    key_file                = '/media/key/key'
    #backup_dir              = '~/.tmpbackup/'
    backup_dir              = ''
    ecrypted_backup_dir     = '/media/VMs'
    ecrypted_backup_file    = backup_file + '.aes-256-cbc'
    kdialog_key_request     = 'kdialog --title "Backup file encryption" --yes-label "OK" --no-label "Cancel" --yesno "Insert storage or press Cancel"'
    kdialog_cancel          = 'kdialog  --title "Backup file encryption" --sorry "Operation cancelled"'
    kdialog_ecrypt_error    = 'kdialog --title "Backup file encryption" --error "An error occured"'
    kdialog_ecrypt_ok       = 'kdialog --title "Backup file encryption" --msgbox "$files Done (with no errors: $errorcode). Unmount and remove storage"'
    openssl_string          = ['openssl', 'enc', '-aes-256-cbc', '-pass', 'file:' + key_file, '-in', backup_dir + backup_file, '-out', ecrypted_backup_dir + ecrypted_backup_file]
    
    print(openssl_string)
    
wtf()