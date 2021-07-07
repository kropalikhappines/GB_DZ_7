import os
import math
import sys
from collections import defaultdict


def memory_files(path):
    # path = r'C:\Users\CNS_2020_2\Desktop\GBDZ\7 занятие'
    result = defaultdict(int)
    for root, dirs, files in os.walk(path):
        for f in files:
            res = os.path.getsize(os.path.join(root, f))
            # prev = res // 10
            if res > 1:
                p = res // 10
                r = int(math.log10(p if p > 0 else 1)) + 1
                result[pow(10, r)] += 1
    return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Sorry, not enough arguments')
    else:
        input_path = sys.argv[1]
        stats = memory_files(input_path)
        print(stats)
