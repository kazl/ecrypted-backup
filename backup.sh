#!/bin/bash
# Скрипт требует для передачи 1 параметр - имя backup-файла

keyFile=/media/key/key
backupDir=~/.tmpbackup
backupFile=$1
ecryptedbackupDir=/media/VMs
ecryptedbackupFile=$backupFile.aes-256-cbc
export DISPLAY=:0.0; xhost +; kdialog --title "Backup file encryption" --yes-label "OK" --no-label "Cancel" --yesno "src: $backupFile
dst: $ecryptedbackupFile

Insert storage or press 'Cancel'"
answer=$?
case $answer in
    1)  kdialog  --title "Backup file encryption" --sorry "Operation cancelled" ;;
    0)  openssl enc -aes-256-cbc -pass file:$keyFile -in $backupDir/$backupFile -out $ecryptedbackupDir/$ecryptedbackupFile 
        errorcode=$?
        if [ $errorcode = 0 ];
            then files=`find $ecryptedbackupDir/ -name "*$(echo "$ecryptedbackupFile" | cut -d "-" -f2)*" -mmin +10 -print`
            kdialog --title "Backup file encryption" --msgbox "$files Done (with no errors: $errorcode). Unmount and remove storage"
            
        else kdialog --title "Backup file encryption" --error "An error $errorcode occured"
        fi                                                                      ;;
esac                                                                                        
