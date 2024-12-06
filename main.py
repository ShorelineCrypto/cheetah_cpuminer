#!/usr/bin/env python2.7
"""
Cheetahcoin (CHTA) blockchain has dynamic difficulty adjustment algorithm
which may trigger ASIC miners to get stuck on CHTA blockchain finding no blocks
from several minutes to several hours.

Cheetah_cpuminer will automatically start mining at local PC when ASIC miners get stuck.
Cheeta_cpuminer will stop mining when ASIC miners are smoothly generating blocks. 

A full node of Cheetahcoin is required to be running at local PC
"""



################################################################################
# Preamble.
################################################################################

# Python standard library imports.
import argparse
import time
import datetime
import itertools
import platform
import os.path
import re
import sys

# Modules in this package.
import cpuminer.cheetah as cheetah
import cpuminer.utils as utils


# Safety for cases when shebang is bypassed.
assert sys.version_info[0] == 2 and sys.version_info[1] >= 7, 'Python version 2.7 (or a later 2.x version) required; you have version: {}.{}.{}'.format(
    *sys.version_info[0:3])



################################################################################
# Main Function
################################################################################

class UserInputException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


def main(args):
    """Main execution functions.

    """
    osname = platform.system()
    print "Your Computer Platform is: {}".format(osname)
    if osname == 'Linux':
       tmpFile1 = os.path.join(os.path.expanduser("~"), '.cheetahcoin',  'cheetahcoin.conf')
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), 'cheetahcoin.conf')
    elif osname == 'Windows':
       tmpFile1 = os.path.join(os.path.expandvars("%userprofile%"), 'AppData\Roaming\Cheetahcoin','cheetahcoin.conf')
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), 'cheetahcoin.conf')
    elif osname == 'Darwin':
       tmpFile1 = os.path.join(os.path.expanduser("~"), 'Library/Application Support/Cheetahcoin',  'cheetahcoin.conf')
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), 'cheetahcoin.conf')
    else:
        assert False, "Error: unsupported operating system: {}".format(osname)

    if utils.isReadable(tmpFile1):
        NengConfigFile = tmpFile1
        print "config found: {}".format(tmpFile1)
    elif utils.isReadable(tmpFile2):
        NengConfigFile = tmpFile2
        print "config found: {}".format(tmpFile2)
    else:
        raise UserInputException(
            "Error in reading CHTA Config File. Please copy or create file 'cheetahcoin.conf' using example file")
        sys.exit(100)


    # Loading configuration file
    configFile = open(NengConfigFile, 'rU')
    config = dict([(k, None) for k in ['rpcuser', 'rpcpassword', 'rpcport']])
    config['rpcport'] = 8536 

    # TODO: Properly Loading config from file
    for line in configFile:
        if line.startswith('#') or re.match(r'^\s+$', line):
            continue
        m1 = re.search(
            r'^rpcuser=(\S+)\s*$', line, re.M)
        if m1 :
            config['rpcuser'] = m1.group(1)
        
        m2 = re.search(
            r'^rpcpassword=(\S+)\s*$', line, re.M)
        if m2:
            config['rpcpassword'] = m2.group(1)
        
        m3 = re.search(
            r'^rpcport=(\d+)\s*$', line, re.M)
        if m3:
            config['rpcport'] = int(m3.group(1))
        
    # window will crash on os.fync on read only file
    # a simple close
    configFile.close()

    assert config['rpcuser'] is not None, "rpcuser missing!"
    assert config['rpcpassword'] is not None, "rpcpassword missing!"
 
    print "Cheetahcoin (CHTA) is a cat meme coin on Bitcoin's SHA256\n"
    print "\nMobile Decentralization!\n"
    print "Cheetahcoin cheetah_cpuminer started!"
 
    blocknum = 0
    while True:
        blocknum = cheetah.run_cheetah(blocknum,config['rpcuser'], config['rpcpassword'], config['rpcport'], args.cpu)
        time.sleep(args.interval)


################################################################################
# Command Line executions - Argument Parsing.
################################################################################

if __name__ == '__main__':

    # ===============================================================================
    # Parse and validate command-line args and input config.
    # ===============================================================================

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--interval', type=int, nargs='?', default=120 , 
                        help='seconds to wait between each check on CHTA blockchain, [default: 120]')
    parser.add_argument('--cpu', nargs='?', type=int, default=1 ,
                        help='How many cpu cores to be used for mining [default: 1]')
    
    args = parser.parse_args()
    # running main function
    main(args)
    
