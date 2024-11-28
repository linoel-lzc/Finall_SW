import sys

from code_sw.analysis import mul_thread

if __name__ == '__main__':
    mul_thread(int(sys.argv[1]), int(sys.argv[2]))
