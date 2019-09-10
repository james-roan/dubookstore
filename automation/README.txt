DU Bookstore Tech Center Apple Kiosk Remote Management Scripts
Written by James Roan
Created 29 June 2019

File                          Description

scripts/shutdown-remote.sh    A test script to shutdown a computer over SSH.
                              There are a number of issues with this method, chiefly
                              that there is no way to easily change hosts or manage
                              passwords.

scripts/shutdown-all.sh       This script runs the Remote Power Utility with the ‘all’
                              option. The pwd is set to …/scripts.

automation.sublime-*          The Sublime Text 2 project files.

remote-power-utility/         Contains the src and config files for the Remote Power
                              Utility. (See README.txt in directory for utility 
                              documentation)