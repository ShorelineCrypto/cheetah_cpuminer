#!/usr/bin/env python3
"""
Cheetah monitors Nengcoin (NENG) or Cheetahcoin (CHTA) and starts local CPU mining
when the selected blockchain's blocks stop arriving.

Cheetah_cpuminer will automatically start mining at local PC when ASIC miners get stuck.
Cheeta_cpuminer will stop mining when ASIC miners are smoothly generating blocks. 

A full node for the selected coin must be running on the local PC.
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


COIN_SETTINGS = {
    'NENG': {
        'config_dir': '.nengcoin',
        'config_file': 'nengcoin.conf',
        'app_dir': 'Nengcoin',
        'default_port': 6376,
        'stuck_timeout': 120,
    },
    'CHTA': {
        'config_dir': '.cheetahcoin',
        'config_file': 'cheetahcoin.conf',
        'app_dir': 'Cheetahcoin',
        'default_port': 8536,
        'stuck_timeout': 240,
    },
}



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
    coin_settings = COIN_SETTINGS[args.coin]
    osname = platform.system()
    print("Your Computer Platform is: {}".format(osname))
    if osname == 'Linux':
       tmpFile1 = os.path.join(
           os.path.expanduser("~"), coin_settings['config_dir'],
           coin_settings['config_file'])
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), coin_settings['config_file'])
    elif osname == 'Windows':
       tmpFile1 = os.path.join(
           os.path.expandvars("%userprofile%"), 'AppData', 'Roaming',
           coin_settings['app_dir'], coin_settings['config_file'])
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), coin_settings['config_file'])
    elif osname == 'Darwin':
       tmpFile1 = os.path.join(
           os.path.expanduser("~"), 'Library', 'Application Support',
           coin_settings['app_dir'], coin_settings['config_file'])
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), coin_settings['config_file'])
    else:
        assert False, "Error: unsupported operating system: {}".format(osname)

    if utils.isReadable(tmpFile1):
        config_file = tmpFile1
        print("config found: {}".format(tmpFile1))
    elif utils.isReadable(tmpFile2):
        config_file = tmpFile2
        print("config found: {}".format(tmpFile2))
    else:
        raise UserInputException(
            "Error in reading {} config file. Please copy or create '{}' using the example file".format(
                args.coin, coin_settings['config_file']))


    # Loading configuration file
    config = dict([(k, None) for k in ['rpcuser', 'rpcpassword', 'rpcport']])
    config['rpcport'] = coin_settings['default_port']

    # TODO: Properly Loading config from file
    with open(config_file, 'r', encoding='utf-8') as configFile:
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


    if args.coin == 'NENG':
        print("Bitcoin Digital Gold - HODL\nDogecoin to the Moon")
        print("Here comes Cheetah running with Neng\nMobile Decentralization!\n")
        print("Nengcoin cheetah_cpuminer started")
    else:
        print("Cheetahcoin (CHTA) is a cat meme coin on Bitcoin's SHA256\n")
        print("\nMobile Decentralization!\n")
        print("Cheetahcoin cheetah_cpuminer started!")

    url = 'http://127.0.0.1:{}'.format(config['rpcport'])
    async with cheetah.create_rpc_client(
            url, config['rpcuser'], config['rpcpassword']) as rpc_connection:
        blocknum = 0
        while True:
            blocknum = await cheetah.run_cheetah(
                blocknum, rpc_connection, args.cpu, args.coin,
                coin_settings['stuck_timeout'])
            await asyncio.sleep(args.interval)


def create_argument_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--interval', type=int, nargs='?', default=120 , 
                        help='seconds to wait between blockchain checks [default: 120]')
    parser.add_argument('--cpu', nargs='?', type=int, default=1 ,
                        help='How many cpu cores to be used for mining [default: 1]')
    parser.add_argument(
        '--coin', choices=COIN_SETTINGS, default='NENG',
        help='Coin to monitor: NENG or CHTA (default: NENG)')

    return parser


################################################################################
# Command Line executions - Argument Parsing.
################################################################################

if __name__ == '__main__':
    args = create_argument_parser().parse_args()
    # running main function
    asyncio.run(main(args))
    
