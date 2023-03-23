"""
这个库可以让我们直接在命令行中就可以向程序中传入参数并让程序运行。
https://zhuanlan.zhihu.com/p/56922793

"""


import argparse

parser = argparse.ArgumentParser(description='命令行中传入一个数字')
#type是要传入的参数的数据类型  help是该参数的提示信息
# parser.add_argument('integers', type=str, help='传入的数字')
parser.add_argument('integers', type=str, nargs='+',help='传入的数字')
args = parser.parse_args()

print(args.integers)

# args = parser.parse_args()

# #获得传入的参数
# print(args)

#获得integers参数
# print(args.integers)
# print(type(args.integers))