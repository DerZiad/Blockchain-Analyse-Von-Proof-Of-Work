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

class Miner