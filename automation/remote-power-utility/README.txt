Remote Power Utility
Created by James Roan on 29 June 2019

Description:
    A simple command line utility to simplify power management of the
    apple kiosks remotely. The utility uses SSH to connect to the kiosks.

Example:
    $ python remote-power-utility.py all

    This command will send a shutdown request to all the kiosks in kiosks.json

Options:
    (None)  Print help string.
    all     Request shutdown of all kiosks over SSH one by one.

Confguration:
    Add kiosks to kiosks.json to add them to the utility.
