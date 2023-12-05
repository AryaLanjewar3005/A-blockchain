import time 

from backend.utils.crypto_hash import crypto_hash
from backend.utils.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp' : 1, 
    'last_hash' : 'genesis_last_hash',
    'hash' : 'genesis_hash',
    'data' : [],
    'difficulty' : 3,
    'nonce' : 'genesis_nonce'
}

class Block:
    #A block is a unit of storage

    def __init__(self,timestamp, last_hash, hash, data, difficulty, nonce):
        self.data = data 
        self.last_hash = last_hash 
        self.timestamp = timestamp
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block ('
                f'timestamp: {self.timestamp}, '
                f'last_hash: {self.last_hash}, '
                f'hash: {self.hash}, '
                f'data: {self.data},  '
                f'difficulty : {self.difficulty},'
                f'nonce : {self.nonce} )'
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ 

    
    @staticmethod 
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data , until a block hash
        is found that meets the leading 0's proof of world requirement.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash 
        difficulty = Block.adjust_difficulty(last_block, timestamp) 
        nonce = 0
        hash = crypto_hash(timestamp, last_hash,data, difficulty, nonce)

        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce += 1 
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash,data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod 
    def genesis():
        #return Block(GENESIS_DATA['timestamp'], GENESIS_DATA['last_hash'], GENESIS_DATA['hash'], GENESIS_DATA['data'])
        return Block(**GENESIS_DATA)

    @staticmethod 
    def adjust_difficulty(last_block, new_timestamp):
        """
        Calculate the adjusted difficulty according to the MINE_RATE.
        Increase the difficulty for quickly mined blocks.
        Decrease the difficulty for slowly mined blocks.
            
        """
        if(new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1
        if(last_block.difficulty - 1 > 0):
            return last_block.difficulty - 1
        return 1
    @staticmethod 
    def is_valid_block(last_block, block):
        """
        Validate block by enforcing the following rules:
        - the block must have the proper last_hash reference 
        - the block must meet the proof of work requirement 
        - the difficulty must only adjust by 1
        - the block hash must be a valid combination of the block fields
        """
        if(block.last_hash != last_block.hash):
            raise Exception('The block last_hash must be correct')

        if hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty:
            raise Exception('The proof of requirement was not met')

        if abs(last_block.difficulty - block.difficulty) > 1:
            raise Exception("the block difficulty must only adjust by 1")
        
        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash, 
            block.data, 
            block.nonce, 
            block.difficulty
        )

        if block.hash != reconstructed_hash:
            raise Exception('The block hash must be correct')


def main():
    genesis_block = Block.genesis()
    good_block = Block.mine_block(Block.genesis(), 'foo')
    #bad_block.last_hash = 'evil_data'

    try: 
        Block.is_valid_block(genesis_block, good_block)
    except Exception as e: 
        print(f'is_valid_block : {e}')

if __name__ == '__main__':
    main()

