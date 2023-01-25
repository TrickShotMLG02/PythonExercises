import re


def parse_and_compute(text: str):
    # TODO implement
    # the 'eval' function might be helpful for this task
    return []


def main():
    # for debugging locally
    assert parse_and_compute('Please compute for us: 316 minus 695') == -379
    assert parse_and_compute('Please compute for us: 447 modulo 150') == 147
    assert parse_and_compute('Please compute for us: 643 plus 193') == 836
    assert parse_and_compute('Please compute for us: 626 times 361') == 225986
    assert parse_and_compute('Please compute for us: 394 divided by 475') == 0.8294736842105264
    assert parse_and_compute('Please compute for us: 573 divided by and floored 56') == 10


if __name__ == '__main__':
    main()
