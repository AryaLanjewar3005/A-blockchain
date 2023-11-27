import time 

from backend.utils.crypto_hash import crypto_hash

GENESIS_DATA = {
    'timestamp' : 1, 
    'last_hash' : 'genesis_last_hash',
    'hash' : 'genesis_hash',
    'data' : []
}

class Block:
    #A block is a unit of storage

    def __init__(self,timestamp, last_hash, hash, data):
        self.data = data 
        self.last_hash = last_hash 
        self.timestamp = timestamp
        self.hash = hash
    def __repr__(self):
        return (
            'Block ('
                f'timestamp: {self.timestamp}, '
                f'last_hash: {self.last_hash}, '
                f'hash: {self.hash}, '
                f'data: {self.data}, ) '
        )
    
    @staticmethod 
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data .
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash 
        hash = f'{timestamp}-{last_hash}'
        return Block(timestamp, last_hash, hash, data)

    def genesis():
        #return Block(GENESIS_DATA['timestamp'], GENESIS_DATA['last_hash'], GENESIS_DATA['hash'], GENESIS_DATA['data'])
        return Block(**GENESIS_DATA) 

def main():
    print(f'block.py __name__ : {__name__}')
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)

if __name__ == '__main__':
    main()

