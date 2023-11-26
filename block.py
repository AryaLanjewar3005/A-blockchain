class Block:
    #A block is a unit of storage

    def __init__(self, data):
        self.data = data 

    def __repr__(self):
        return f'Block-data: {self.data}'
    

print(f'block.py __name__ : {__name__}')
