import re


def extract_ips(text: str) -> list:
    # TODO implement
    return []


def main():
    # for debugging locally
    assert sorted(extract_ips('112162.26.33\n169.6.114.185\n7783.185.39.175')) == sorted(['169.6.114.185'])


if __name__ == '__main__':
    main()
