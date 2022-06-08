# from BlocksFilePy.core import FTAffair

from abc import abstractclassmethod, abstractmethod


class BlocksFileCore(object):
    
    def __init__(self, mft: dict, blocks_root_path:str):
        self.mft = mft
        self.blocks_root_path = blocks_root_path

    def add_file(file, internal_path):
        pass



class FileTableManager(object):
    
    def __init__(self, file_table:dict) -> None:
        self._file_table = file_table

    def allocation(self, size:int) -> 'FTAffair':
        affair = FTAffair(self)
        return affair

    def add(self, meta):
        pass

    # def delete(self,)


class FTAffairList(object):

    def __init__(self, ftm:'FileTableManager') -> None:
        self.file_table_manager = ftm

    def commit(self):
        pass


class FTAffair(object):

    def __init__(self, ftm:FileTableManager) -> None:
        self._ftm = ftm
    
    @abstractmethod
    def run(self):
        pass


class CreateFile(FTAffair):

    def __init__(self, ftm:FileTableManager) -> None:
        super().__init__(ftm)

    def run(self):
        self._ftm()

class DeleteFile(FTAffair):
    
    def __init__(self, ftm:FileTableManager) -> None:
        super().__init__(ftm)


class BlocksManager(object):
    
    def __init__(self, root_path:str) -> None:
        self.root_path = root_path

