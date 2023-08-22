from argparse import ArgumentParser,BooleanOptionalAction


def make_dirs(input_file:str,replace:str):
    replace_fields = replace.split(',')
    if len(replace_fields) != 2:
        print("Error, expect 2 replace fields")

    with open(input_file) as file:
        for line in file:
            fields = line.rstrip().split(';')
            if fields[3] == 'dir':
                new_dir = fields[0].replace(replace_fields[0],replace_fields[1])
                print(f'mkdir "{new_dir}"')


def copy_files(input_file:str,filter:bool,replace:str):
    allowed_ext = set(["JPG","PNG"])
    replace_fields = replace.split(',')
    if len(replace_fields) != 2:
        print("Error, expect 2 replace fields")
    with open(input_file) as file:
        for line in file:
            fields = line.rstrip().split(';')
            if fields[3] == 'file':
                ext = fields[4][-3:].upper()
                if (filter and ext in allowed_ext) or not filter:
                    full_file = f"{fields[0]}/{fields[4]}"
                    target_file = full_file.replace(replace_fields[0],replace_fields[1])
                    print(f'cp -a -v "{full_file}" "{target_file}"')



def main():
    parser = ArgumentParser(description=
        """Makes from a list made by list_dirs a set of copy commands
        """
    )
    
    parser.add_argument("input_file", help="Input file", type=str, default='./')
    parser.add_argument("-r","--replace", help="Replace string from source in target", type=str, required=False,default='Elements2,Elements/joze/Elements')
    parser.add_argument("-d","--dirs_only", help="Make only the directory structure", action=BooleanOptionalAction, type=bool, required=False,default=False)
    parser.add_argument("-f","--filter", help="apply hard coded filter", action=BooleanOptionalAction, type=bool, required=False,default=False)

    args = parser.parse_args()

    if args.dirs_only:
        make_dirs(args.input_file,args.replace)
    else:
        copy_files(args.input_file,args.filter,args.replace)

if __name__ == '__main__':  
    main()