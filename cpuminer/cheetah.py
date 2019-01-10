import time
from datetime import datetime
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

def run_cheetah(prevheight, rpc_user,rpc_password,rpc_port, cpu):
   

   # rpc_user and rpc_password are set in the bitcoin.conf file
   rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%d"%(rpc_user, rpc_password, rpc_port))

   best_block_hash = rpc_connection.getbestblockhash()
   bestblock = rpc_connection.getblock(best_block_hash)

   cur_epoch = int(time.time()) 
   bcstucktime = cur_epoch - bestblock['time']

   if bcstucktime < 0:
      print "Height {} block Time is ahead of current time, miner cheating or wrong timestamp {}, current {} GMT".format(bestblock['height'], bestblock['time'], datetime.utcnow())
   mining_info = rpc_connection.getmininginfo()
   
   if ( bcstucktime > 120 ):
      print "ASIC miners got stuck on NENG blockchain for {} seconds".format(bcstucktime)
      print "block {}: {} {} GMT".format(bestblock['height'],bestblock['time'], datetime.utcnow())
      
      if not mining_info['generate']:
         print("NENG CPU Mining Started")
         rpc_connection.setgenerate(True, cpu)
      elif bestblock['height'] != prevheight:
         print("NENG CPU Mining Restarted")
         rpc_connection.setgenerate(False)
         rpc_connection.setgenerate(True, cpu)
   else:
      if mining_info['generate']:
         print "block {}: {} {} GMT".format(bestblock['height'],bestblock['time'], datetime.utcnow())
         print("NENG CPU Mining Stopped")
         rpc_connection.setgenerate(False)


   return bestblock['height']

   
   

         

