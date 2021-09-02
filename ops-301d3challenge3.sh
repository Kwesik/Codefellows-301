#!/bin/bash
Script Name:        File Permissions
Autor:              KwesiK
Date:               20210901

#Variables

#Functions
    cd $path
    chom -r $per $path
    ls -l

#Main
echo "enter directory path"
read path
echo "enter desired permissions (e.g 777):.."
read per

#End
