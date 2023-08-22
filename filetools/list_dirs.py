import os
from argparse import ArgumentParser,BooleanOptionalAction

def list_dirs(directory:str,strip:bool):
    for dir in os.walk(directory):
        name = os.path.basename(dir[0])
        path = dir[0]
        has_subdirs = (len(dir[1]) > 0)

        if strip:
            path = path.removeprefix(directory)
        print(f'{path};{name};{has_subdirs}')

def list_files(directory:str,strip:bool):
    for dir in os.walk(directory):
        name = os.path.basename(dir[0])
        path = dir[0]
        has_subdirs = (len(dir[1]) > 0)

        if strip:
            path = path.removeprefix(directory)
        print(f'{path};{name};{has_subdirs};dir;')
        for file in dir[2]:
            print(f'{path};{name};{has_subdirs};file;{file}')

def main():
    parser = ArgumentParser(description=
        """Makes a list of all directories recursively and outputs a csv format with directory names.
        """
    )
    
    parser.add_argument("directory", help="Directory to list", type=str, default='./')
    parser.add_argument("-s","--strip", help="Remove the start directory from the full path", action=BooleanOptionalAction, type=bool, required=False,default=False)
    parser.add_argument("-f","--files", help="List filenames", action=BooleanOptionalAction, type=bool, required=False,default=False)

    args = parser.parse_args()

    if args.files:
        list_files(args.directory,args.strip)
    else:
        list_dirs(args.directory,args.strip)

if __name__ == '__main__':  
    main()
