#!/bin/bash

if [ $# -ne 1 ]; then
  echo "パラメータエラー" 1>&2
  echo "sh patch_naoqi_python_sdk_for_elcaptain.sh  naoqi_python_sdkのパス" 
  exit 1
fi

NAOQIDIR=$1 # "${HOME}/Documents/Job/J/python/software/python-sdk"

if [ ! -e ${NAOQIDIR}/naoqi.py ]; then
    echo "指定されたパスは naoqi python SDK ではないようです"
    exit 1
fi

cd ${NAOQIDIR}

for file in `ls *.dylib *.so`
do
    # patch all library internal cross references
    echo "Patching " $file "..."
    for fileother in `ls  *.dylib *.so ;ls qi *.dylib *.so`
    do
        # library
        echo "  Patching " $fileother " with " $file "..."
        install_name_tool  -change $file $NAOQIDIR/$file $fileother
    done
    # patch Python reference for the library
    install_name_tool -change /Library/Frameworks/Python.framework/Versions/2.7/Python /System/Library/Frameworks/Python.framework/Versions/2.7/Python $file
done

for file in `ls *.dylib *.so`
do
    # patch all library internal cross references
    echo "Patching " $file "..."
    fileother="qi/plugins/libqimodule_python_plugin.dylib"
    # library
    echo "  Patching " $fileother " with " $file "..."
    install_name_tool -change $file $NAOQIDIR/$file $fileother
    # patch Python reference for the library
    install_name_tool -change /Library/Frameworks/Python.framework/Versions/2.7/Python /System/Library/Frameworks/Python.framework/Versions/2.7/Python $file
done
