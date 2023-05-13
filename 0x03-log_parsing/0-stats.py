#!/usr/bin/python3
"""
Log parsing
"""
from sys import stdin


def print_stats(stats: dict, file_size: int) -> None:
    print("File size: {:d}".format(file_size))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    try:
        for line in stdin:
            count += 1
            data = line.split()

            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass

            try:
                filesize += int(data[-1])
            except BaseException:
                pass

            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)

    except KeyboardInterrupt as e:
        print_stats(stats, filesize)
        raise e
