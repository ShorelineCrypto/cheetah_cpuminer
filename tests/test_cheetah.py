import asyncio
import time
import unittest

from cpuminer.cheetah import run_cheetah


class FakeRPC:
    def __init__(self, height, block_time, generating):
        self.height = height
        self.block_time = block_time
        self.generating = generating
        self.calls = []

    async def getbestblockhash(self):
        return 'best-block-hash'

    async def getblock(self, block_hash):
        return {'height': self.height, 'time': self.block_time}

    async def getmininginfo(self):
        return {'generate': self.generating}

    async def acall(self, method, params):
        self.calls.append((method, params))


class RunCheetahTests(unittest.TestCase):
    def test_starts_mining_when_blockchain_is_stuck(self):
        rpc = FakeRPC(
            height=10, block_time=int(time.time()) - 200, generating=False)

        height = asyncio.run(run_cheetah(10, rpc, 2))

        self.assertEqual(height, 10)
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
