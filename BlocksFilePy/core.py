# from BlocksFilePy.core import FTAffair

from abc import abstractclassmethod, abstractmethod


class BlocksFileCore(object):
    
    def __init__(self, mft: dict, blocks_root_path:str):
        self.mft = mft
        self.blocks_root_path = blocks_root_path

    def add_file(file, internal_path):
        pass
