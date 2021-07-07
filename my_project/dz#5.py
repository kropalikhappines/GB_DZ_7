import os
import math
import sys
from collections import defaultdict


def memory_files(path):
    # path = r'C:\Users\CNS_2020_2\Desktop\GBDZ'
    result = defaultdict(int)
    for root, dirs, files in os.walk(path):
        for f in files:
            res = os.path.getsize(os.path.join(root, f))
            ty = f.rsplit('.', maxsplit=1)[-1]
            # print(ty)
            if res:
                p = res // 10
                r = int(math.log10(p if p > 0 else 1)) + 1
                if not result[pow(10, r)]:
                    result[pow(10, r)] = (1, [ty])
                else:
                    val = result[pow(10, r)][0]
                    exten = result[pow(10, r)][1]
                    if ty not in exten:
                        exten.append(ty)
                    result[pow(10, r)] = (val + 1, exten)
    return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Sorry, not enough arguments')
    else:
        input_path = sys.argv[1]
        stats = memory_files(input_path)
        print(stats)
