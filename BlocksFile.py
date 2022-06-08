import sys, argparse, os
import cmd
import logging
import traceback

# logger = logging.Logger('cmd')
# logger.setLevel(10)
LOGGING_FORMAT = '%(asctime)s %(filename)s %(funcName)s [%(levelname)s]: %(message)s'
LOGGING_LEVEL = logging.DEBUG
logging.basicConfig(format=LOGGING_FORMAT, level=LOGGING_LEVEL)


class BlocksFileCore():
    
    def __init__(self, mft: dict, blocks_root_path:str):
        self.mft = mft
        self.blocks_root_path = blocks_root_path


class BlocksFileCMD(cmd.Cmd):
    prompt = 'BLOCKSFILE> '
    
    def do_init(self, args):
        print(args)

    def do_open(self, args):
        print(args)
    
    def do_add(self, args):
        # try:
        #     args_parser = argparse.ArgumentParser(add_help=False, exit_on_error=False)
        #     args_parser.add_argument('path', help='the path of file/dir you want to add in')
        #     args_parser.add_argument('-r', '--recursive', 
        #         action='store_true', 
        #         help='directories and their contents recursively'
        #     )
        #     logging.debug(args.split())
        #     args = args_parser.parse_args(args.split())
        # except Exception as ex:
        #     traceback.print_exc()
        print(args)
    
    def do_reset(self, args):
        print(args)

    def do_rm(self, args):
        print(args)

    def do_commit(self, args):
        print(args)

    def do_status(self, args):
        print(args)
    
    def do_check(self, args):
        print(args)

    def do_export(self, args):
        print(args)
        
    def do_ls(self, args):
        print(args)

    def do_cd(self, args):
        print(args)
    
    def do_config(self, args):
        print(args)

    def do_quit(self, args):
        print('bye')
        return True

    def do_exit(self, args):
        return self.do_quit(args)


# def command_open(args):
#     BlocksFileCMD().cmdloop()


# command_dict = {
#     "open":command_open
# }

# def parse():
#     parser = argparse.ArgumentParser(prog="BlocksFilePy")
#     parser.add_argument('command')
#     args = parser.parse_args()
#     return args


# def main():
#     # print(sys.argv)
#     # cmd_args = parse(sys.argv)
#     cmd_args = parse()
#     if cmd_args.command in command_dict:
#         command_dict[cmd_args.command](cmd_args)
#     else:
#         print('Unknown command!')

def main():
    BlocksFileCMD.cmdloop()

if __name__ == '__main__':
    main()

