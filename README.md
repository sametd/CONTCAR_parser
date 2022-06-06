# CONTCAR parser for VASP


Don't use this for parsing POSCAR file as scaling and cartesian is not implemented. This is a very very simple class that can output CONTCAR to xyz, created for testing some tiny stuff, use with caution.  

It is very straight forward just supply the CONTCAR file location in the script.

Example output:

    $ python3 read_contcar.py
    AtomCount = 192  
    Symbols = ['La', 'Li', 'O', 'Zr']  
    Counts = [24, 56, 96, 16]  
    Cell =  
    [[13.021933 0. 0. ]  
    [ 0. 13.021933 0. ]  
    [ 0. 0. 13.021933]]
