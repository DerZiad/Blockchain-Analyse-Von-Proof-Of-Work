class Block:
    def __init__(self,bits,block_index,hash,height,main_chain,tx,nonce,prevBlockHash,receivedTime,relayed_by,size,time,version):
        self.hash = hash
        self.bits = bits
        self.block_index = block_index
        self.height = height
        self.main = main_chain
        self.tx = tx
        self.n_tx = len(tx)
        self.nonce = nonce
        self.prevBlockHash = prevBlockHash
        self.receivedTime = receivedTime
        self.relayed_by = relayed_by
        self.size = size
        self.time = time
        self.version = version

class Transaction:
    def __init__(self,block_height,hash,lock_time,relayed_by,size,tx_index,version,vin_sz,vout_sz,outs,inputs):
        self.block_height = block_height
        self.hash = hash
        self.lock_time = lock_time
        self.relayed_by = relayed_by
        self.size = size
        self.tx_index = tx_index
        self.version = version
        self.vin_sz = vin_sz
        self.vout_sz = vout_sz
        self.outs = outs
        self.inputs = inputs


class Out:
    def __init__(self,hash,script,value):
        self.hash = hash
        self.script = script
        self.value = value

class Input:
    def __init__(self,hash,n,script,tx_index,value):
        self.hash = hash
        self.n = n
        self.script = script
        self.tx_index = tx_index
        self.value = value

class MiningException(ValueError):
    def __init__(self,msg):
        super.__init__(msg)

def mine(block):
    pass