#!/usr/bin/env python3
"""
Nengcoin (NENG) blockchain has dynamic difficulty adjustment algorithm
which may trigger ASIC miners to get stuck on NENG blockchain finding no blocks
from several minutes to several hours.

Cheetah_cpuminer will automatically start mining at local PC when ASIC miners get stuck.
Cheeta_cpuminer will stop mining when ASIC miners are smoothly generating blocks. 

A full node of Nengcoin is required to be running at local PC
"""



################################################################################
# Preamble.
################################################################################

# Python standard library imports.
import argparse
import asyncio
import platform
import os.path
import re
import sys

if sys.version_info < (3, 7):
    raise RuntimeError('Python 3.7 or later is required; you have version: {}.{}.{}'.format(
        *sys.version_info[0:3]))

# Modules in this package.
import cpuminer.cheetah as cheetah
import cpuminer.utils as utils



################################################################################
# Main Function
################################################################################

class UserInputException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


async def main(args):
    """Main execution functions.

    """
    osname = platform.system()
    print("Your Computer Platform is: {}".format(osname))
    if osname == 'Linux':
       tmpFile1 = os.path.join(os.path.expanduser("~"), '.nengcoin',  'nengcoin.conf')
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), 'nengcoin.conf')
    elif osname == 'Windows':
       tmpFile1 = os.path.join(
           os.path.expandvars("%userprofile%"), 'AppData', 'Roaming',
           'Nengcoin', 'nengcoin.conf')
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), 'nengcoin.conf')
    elif osname == 'Darwin':
       tmpFile1 = os.path.join(os.path.expanduser("~"), 'Library/Application Support/Nengcoin',  'nengcoin.conf')
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), 'nengcoin.conf')
    else:
        assert False, "Error: unsupported operating system: {}".format(osname)

    if utils.isReadable(tmpFile1):
        NengConfigFile = tmpFile1
        print("config found: {}".format(tmpFile1))
    elif utils.isReadable(tmpFile2):
        NengConfigFile = tmpFile2
        print("config found: {}".format(tmpFile2))
    else:
        raise UserInputException(
            "Error in reading NENG Config File. Please copy or create file 'nengcoin.conf' using example file")


    # Loading configuration file
    config = dict([(k, None) for k in ['rpcuser', 'rpcpassword', 'rpcport']])
    config['rpcport'] = 6376

    # TODO: Properly Loading config from file
    with open(NengConfigFile, 'r', encoding='utf-8') as configFile:
        for line in configFile:
            if line.startswith('#') or re.match(r'^\s+$', line):
                continue
            m1 = re.search(
                r'^rpcuser=(\S+)\s*$', line, re.M)
            if m1:
                config['rpcuser'] = m1.group(1)

            m2 = re.search(
                r'^rpcpassword=(\S+)\s*$', line, re.M)
            if m2:
                config['rpcpassword'] = m2.group(1)

            m3 = re.search(
                r'^rpcport=(\d+)\s*$', line, re.M)
            if m3:
                config['rpcport'] = int(m3.group(1))

    assert config['rpcuser'] is not None, "rpcuser missing!"
    assert config['rpcpassword'] is not None, "rpcpassword missing!"


    print("Bitcoin Digital Gold - HODL\nDogecoin to the Moon")
    print("Here comes Cheetah running with Neng\nMobile Decentralization!\n")
    print("Nengcoin cheetah_cpuminer started")

    url = 'http://127.0.0.1:{}'.format(config['rpcport'])
    async with cheetah.create_rpc_client(
            url, config['rpcuser'], config['rpcpassword']) as rpc_connection:
        blocknum = 0
        while True:
            blocknum = await cheetah.run_cheetah(
                blocknum, rpc_connection, args.cpu)
            await asyncio.sleep(args.interval)


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
                        help='seconds to wait between each check on NENG blockchain, [default: 120]')
    parser.add_argument('--cpu', nargs='?', type=int, default=1 ,
                        help='How many cpu cores to be used for mining [default: 1]')
    
    args = parser.parse_args()
    # running main function
    asyncio.run(main(args))
    
