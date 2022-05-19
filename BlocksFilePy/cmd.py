import cmd
from core import BlocksFileCore

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