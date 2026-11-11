import time
from datetime import datetime

from bitcoinrpc import BitcoinRPC


def create_rpc_client(url, rpc_user, rpc_password):
    """Create the async RPC client using credentials from the selected coin config."""
    return BitcoinRPC.from_config(url, (rpc_user, rpc_password))


async def run_cheetah(prevheight, rpc_connection, cpu, coin='NENG',
                      stuck_timeout=120):
    if coin == 'CHTA':
        block_height = await rpc_connection.getblockcount()
        best_block_hash = await rpc_connection.getblockhash(block_height)
    else:
        best_block_hash = await rpc_connection.getbestblockhash()
    bestblock = await rpc_connection.acall('getblock', [best_block_hash, True])

    cur_epoch = int(time.time())
    bcstucktime = cur_epoch - bestblock['time']

    if bcstucktime < 0:
        print("Height {} block Time is ahead of current time {} seconds, current {} GMT".format(
            bestblock['height'], bcstucktime, datetime.utcnow()))
    mining_info = await rpc_connection.getmininginfo()

    if bcstucktime > stuck_timeout:
        print("ASIC/GPU miners got stuck on {} blockchain for {} seconds".format(
            coin, bcstucktime))
        print("Cheetah running, block {}: {} {} GMT".format(
            bestblock['height'], bestblock['time'], datetime.utcnow()))

        if not mining_info['generate']:
            print("Cheetah accelerates, {} CPU Mining Started".format(coin))
            await rpc_connection.acall('setgenerate', [True, cpu])
        elif bestblock['height'] != prevheight:
            print("Cheetah jumps, {} CPU Mining Restarted".format(coin))
            await rpc_connection.acall('setgenerate', [False])
            await rpc_connection.acall('setgenerate', [True, cpu])
    elif mining_info['generate']:
        print("block {}: {} {} GMT".format(
            bestblock['height'], bestblock['time'], datetime.utcnow()))
        print("Cheetah rests, {} CPU Mining Stopped".format(coin))
        await rpc_connection.acall('setgenerate', [False])

    return bestblock['height']
