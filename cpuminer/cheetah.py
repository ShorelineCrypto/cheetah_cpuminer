import time
from datetime import datetime

from bitcoinrpc import BitcoinRPC


def create_rpc_client(url, rpc_user, rpc_password):
    """Create the async RPC client using credentials from nengcoin.conf."""
    return BitcoinRPC.from_config(url, (rpc_user, rpc_password))


async def run_cheetah(prevheight, rpc_connection, cpu):
    best_block_hash = await rpc_connection.getbestblockhash()
    bestblock = await rpc_connection.acall('getblock', [best_block_hash, True])

    cur_epoch = int(time.time())
    bcstucktime = cur_epoch - bestblock['time']

    if bcstucktime < 0:
        print("Height {} block Time is ahead of current time {} seconds, current {} GMT".format(
            bestblock['height'], bcstucktime, datetime.utcnow()))
    mining_info = await rpc_connection.getmininginfo()

    if bcstucktime > 120:
        print("ASIC/GPU miners got stuck on NENG blockchain for {} seconds".format(
            bcstucktime))
        print("Cheetah running, block {}: {} {} GMT".format(
            bestblock['height'], bestblock['time'], datetime.utcnow()))

        if not mining_info['generate']:
            print("Cheetah accelerates, NENG CPU Mining Started")
            await rpc_connection.acall('setgenerate', [True, cpu])
        elif bestblock['height'] != prevheight:
            print("Cheetah jumps, NENG CPU Mining Restarted")
            await rpc_connection.acall('setgenerate', [False])
            await rpc_connection.acall('setgenerate', [True, cpu])
    elif mining_info['generate']:
        print("block {}: {} {} GMT".format(
            bestblock['height'], bestblock['time'], datetime.utcnow()))
        print("Cheetah rests, NENG CPU Mining Stopped")
        await rpc_connection.acall('setgenerate', [False])

    return bestblock['height']
