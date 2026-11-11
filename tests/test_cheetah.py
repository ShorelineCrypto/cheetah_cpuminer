import asyncio
import time
import unittest

from cpuminer.cheetah import run_cheetah
from main import COIN_SETTINGS, create_argument_parser


class FakeRPC:
    def __init__(self, height, block_time, generating):
        self.height = height
        self.block_time = block_time
        self.generating = generating
        self.calls = []
        self.getblock_params = None
        self.lookup_calls = []

    async def getbestblockhash(self):
        self.lookup_calls.append(('getbestblockhash', []))
        return 'best-block-hash'

    async def getblockcount(self):
        self.lookup_calls.append(('getblockcount', []))
        return self.height

    async def getblockhash(self, height):
        self.lookup_calls.append(('getblockhash', [height]))
        return 'best-block-hash'

    async def getmininginfo(self):
        return {'generate': self.generating}

    async def acall(self, method, params):
        if method == 'getblock':
            self.getblock_params = params
            return {'height': self.height, 'time': self.block_time}
        self.calls.append((method, params))


class RunCheetahTests(unittest.TestCase):
    def test_coin_argument_defaults_to_neng_and_accepts_chta(self):
        parser = create_argument_parser()
        self.assertEqual(parser.parse_args([]).coin, 'NENG')
        self.assertEqual(parser.parse_args(['--coin', 'CHTA']).coin, 'CHTA')

    def test_coin_defaults_preserve_neng_and_configure_cheetahcoin(self):
        self.assertEqual(COIN_SETTINGS['NENG']['default_port'], 6376)
        self.assertEqual(COIN_SETTINGS['NENG']['stuck_timeout'], 120)
        self.assertEqual(COIN_SETTINGS['CHTA']['default_port'], 8536)
        self.assertEqual(COIN_SETTINGS['CHTA']['stuck_timeout'], 240)
        self.assertEqual(COIN_SETTINGS['CHTA']['config_file'], 'cheetahcoin.conf')

    def test_starts_mining_when_blockchain_is_stuck(self):
        rpc = FakeRPC(
            height=10, block_time=int(time.time()) - 200, generating=False)

        height = asyncio.run(run_cheetah(10, rpc, 2))

        self.assertEqual(height, 10)
        self.assertEqual(rpc.getblock_params, ['best-block-hash', True])
        self.assertEqual(rpc.lookup_calls, [('getbestblockhash', [])])
        self.assertEqual(rpc.calls, [('setgenerate', [True, 2])])

    def test_uses_cheetahcoin_rpc_lookup_and_threshold(self):
        early_rpc = FakeRPC(
            height=10, block_time=int(time.time()) - 200, generating=False)
        asyncio.run(run_cheetah(
            10, early_rpc, 2, coin='CHTA', stuck_timeout=240))
        self.assertEqual(early_rpc.calls, [])

        rpc = FakeRPC(
            height=10, block_time=int(time.time()) - 300, generating=False)

        asyncio.run(run_cheetah(10, rpc, 2, coin='CHTA', stuck_timeout=240))

        self.assertEqual(rpc.lookup_calls, [
            ('getblockcount', []),
            ('getblockhash', [10]),
        ])
        self.assertEqual(rpc.getblock_params, ['best-block-hash', True])
        self.assertEqual(rpc.calls, [('setgenerate', [True, 2])])

    def test_restarts_mining_when_block_height_changes(self):
        rpc = FakeRPC(
            height=11, block_time=int(time.time()) - 200, generating=True)

        asyncio.run(run_cheetah(10, rpc, 2))

        self.assertEqual(rpc.calls, [
            ('setgenerate', [False]),
            ('setgenerate', [True, 2]),
        ])

    def test_stops_mining_when_blockchain_is_current(self):
        rpc = FakeRPC(
            height=10, block_time=int(time.time()) + 3600, generating=True)

        asyncio.run(run_cheetah(10, rpc, 2))

        self.assertEqual(rpc.calls, [('setgenerate', [False])])
