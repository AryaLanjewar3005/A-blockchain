import time 


class Block:
    #A block is a unit of storage

    def __init__(self,timestamp, last_hast, hash, data):
        self.data = data 
        self.last_hash = last_hast
        self.timestamp = timestamp
        self.hash = hash 

    def __repr__(self):
        return (
            'Block ('
                f'timestamp: {self.timestamp}, '
                f'timestamp: {self.last_hash}, '
                f'timestamp: {self.hash}, '
                f'timestamp: {self.data}, ) '
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
        return Block(1, "genesis_last_hash", 'genesis_hash', [])
    

def main():
    print(f'block.py __name__ : {__name__}')
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)

if __name__ == '__main__':
    main()

