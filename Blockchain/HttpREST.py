import requests
import time
from multiprocessing.pool import ThreadPool
import math
from numba import cuda,jit

ACTUEL_BLOCKS_API = "https://blockchain.info/blocks/{}?format=json"
BLOCK_INFO_API = "https://blockchain.info/rawblock/{}?format=json"


class WebSocketBlockchain:
    def __init__(self):
        self.actuel_blocks_api = "https://blockchain.info/blocks/{}?format=json"
        self.block_info_api = "https://blockchain.info/rawblock/{}?format=json"
        self.list_of_blocks = []#List in python are thread_safe,concurrent lists.

    def start(self):
        self.running = True
        pool = ThreadPool(processes=100)
        pool.apply(self.scan)

    def stop(self):
        self.running = False


    def scan(self):
        while self.running:
            actuel_time = round(time.time() * 1000)
            print(actuel_time)
            list_of_blocks = requests.get(self.actuel_blocks_api.format(actuel_time)).json()
            pool = ThreadPool(processes=20)
            pool.apply(self.find, list_of_blocks[len(list_of_blocks) // 2:])
            pool.apply(self.find,list_of_blocks[:len(list_of_blocks)//2])# Start process to search in the first half and the other process for the next half

    @jit(target_backend='cuda')
    def find(self,*argv):
        for block in argv:
            block_informations = requests.get(self.block_info_api.format(block['hash'])).json()
            if('nonce' in block_informations):
                print(block_informations['nonce'])
            else:
                print("==================================> not mined")

client = WebSocketBlockchain()
client.start()