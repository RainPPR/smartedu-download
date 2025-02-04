import sys
import download

hints = {
    'default': '''这是默认提示
喵''',
    'id': '''id 的提示
喵''',
    'url': '''url 的提示
喵'''
}

def Main():
    argv = sys.argv
    if len(argv) == 1:
        print(hints['default'])
    elif len(argv) == 2:
        if argv[1] in hints:
            print(hints[argv[1]])
        else:
            print('错误：找不到该命令！')
            print(hints['default'])
    else:
        op = argv[1]
        data = argv[2:]
        if op == 'id':
            download.download_id(data)
        elif op == 'url':
            download.download_url(data[2])
        else:
            print('错误：找不到该命令！')
            print(hints['default'])

if __name__ == "__main__":
    Main()
