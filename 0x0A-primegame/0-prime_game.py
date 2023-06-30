#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Args:
        x - number of rounds
        nums - an array of n

    Return:
         The name of the player (Maria || Ben) that won the most rounds
         Or None if the winner cannot be determined
    """
    maria = 0
    ben = 0
    cur_round = 0

    def game_play(num):
        """
        Simulates each round of the game to determine winner
        """
        if num == 1:
            return 0

        moves = 0
        num_box = list(range(2, num + 1))
        for i, val in enumerate(num_box):
            for mul in num_box[i+1:]:
                if mul % val == 0:
                    # print(f"mul: {mul}, val: {val}")
                    num_box.remove(mul)
            moves += 1
        return moves

    for num in nums:
        if cur_round < x:
            moves = game_play(num)
            # print("moves:", moves)
            if moves % 2 != 0:
                maria += 1
            else:
                ben += 1

    if maria == ben:
        return None

    return "Maria" if maria > ben else "Ben"


if __name__ == "__main__":
    print(isWinner(5, [2, 5, 5, 4, 3]))
