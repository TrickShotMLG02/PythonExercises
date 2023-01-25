import re


def extract_emails_matching(text: str) -> list:
    # TODO implement, ensure that nothing that ends with '(do not contact)' (case-insensitive) is included
    pass


def main():
    # for debugging locally
    assert sorted(extract_emails_matching('VnD55gWzB3BGye@QGocn8QJnRf3qGimIL7DZQ.ir (Voluptatem '
                                          'qua)\nDSBHYDe6TDfCWKMnH2in.gzCqj@B1eoB69dTTINcHy3ca7nTb61ZT.org'
                                          '\nBFhNKR9ndaP_jx05Z@41M3sMOiK-nmla.ir (dO nOt '
                                          'coNTAcT)\nkf1aMUEEDGG2Bios61a_qGGpEa@Pz9iSzT7waKZsJvrNL36h8EM.ca (Dolor '
                                          'sed volu)\n')) == \
           sorted(['VnD55gWzB3BGye@QGocn8QJnRf3qGimIL7DZQ.ir',
                   'DSBHYDe6TDfCWKMnH2in.gzCqj@B1eoB69dTTINcHy3ca7nTb61ZT.org',
                   'kf1aMUEEDGG2Bios61a_qGGpEa@Pz9iSzT7waKZsJvrNL36h8EM.ca'])


if __name__ == '__main__':
    main()
