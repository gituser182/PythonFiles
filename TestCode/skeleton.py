#!/usr/bin/env python

"""
Begincommentaar
"""
#import

#--------------------------------------------------------------------
__author__     = "user182"
__copyright__  = "Copyright 2014, "
__credits__    = ["Guido"]
__license__    = "GPL"
__version__    = "1.0.0"
__maintainer__ = "user182"
__email__      = "user182@qet.be"
__status__     = "Alpha Mar 04, 2014"
#--------------------------------------------------------------------

def eenfunctie():
    """
    Beschrijving van de functie
    """
    pass

#steeds als voorlaatste
def main():
    """
    de main body
    """
    print "Programmed by %s" % __author__
    print eenfunctie.__doc__
    print "einde"
    
#steeds helemaal onderaan te plaatsen als app ipv module
if __name__ == '__main__':
    main()