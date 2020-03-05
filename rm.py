import argparse
import os

parser = argparse.ArgumentParser(description='remove files and directories safely.')
parser.add_argument('files', metavar='N', type=str, nargs='+',
                    help='files or directories you want to remove')
parser.add_argument('--tb_dir', default=os.path.expanduser('~/TrashBin/'),
                    help='trash bin directory, default ~/TrashBin/')


def get_last_file_name(file: str):
    if not os.path.exists(file):
        raise OSError(f'{file} not exists.')
    if os.path.isdir(file):
        file = file.strip('/')
    return os.path.basename(file)


def do_rm(file, dst_dir):
    last_file_name = get_last_file_name(file)
    dst_file_name = os.path.join(dst_dir, last_file_name)
    if not os.path.exists(dst_file_name):
        print(f'moving {last_file_name} to {dst_file_name}')
    else:
        suffix = 1
        while os.path.exists(os.path.join(dst_dir, last_file_name + '.' + str(suffix))):
            suffix += 1
        dst_file_name = os.path.join(dst_dir, last_file_name + '.' + str(suffix))
        print(f'moving {last_file_name} to {dst_file_name}')
    command = f'mv {file} {dst_file_name}'
    ret = os.system(command)
    with open(os.path.join(dst_dir, '.rm-log.txt'), 'a') as f:
        f.write(command)
        if ret == 0:
            f.write('   success.\n')
        else:
            f.write('   fail.\n')


def main():
    args = parser.parse_args()
    for file in args.files:
        try:
            do_rm(file, dst_dir=args.tb_dir)
        except Exception as e:
            print(e)
            print(f'removing {file} failed.')


if __name__ == '__main__':
    main()
