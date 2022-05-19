class BlocksFileCore():
    
    def __init__(self, mft: dict, blocks_root_path:str):
        self.mft = mft
        self.blocks_root_path = blocks_root_path