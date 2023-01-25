import re


def extract_emails(text: str) -> list:
    # TODO implement
    pass


def main():
    # for debugging locally
    assert sorted(extract_emails('He asked:eKyce39H2OEwh3i_eLQ0GdIYl@2YF3A6cHjAAar.ru. '
                                 'He asked:UA_D9Ab5RKka5ukyHfzUko9.qsoZ-@-vNJy61H6nLjYCFQw.ca. '
                                 'He asked:_KlD-kD9loANfR0dm6JQ8Jy_AHth@4POm8i3wYkA92fgmo.org. '
                                 'Sit magnam quaerat dolor. P0Nntdh0AnFaSoXxzGD0KwF8vOe@p6ybbs0JAdmiMq.ru? '
                                 'Aliquam consectetur adipisci voluptatem sit magnam neque '
                                 'mLdRF6FCJBVw668F@vCQukhDoyunMlvB2g7kmTAa.de. He '
                                 'asked:1Vazeu8XqhqEBo4WphYRF5x@ZhJVnmrc5a.ir. He '
                                 'asked:lHy5aKCgZOl8XpO_@vWfpH21eypOqdR2o2.net. Tempora ipsum labore modi dolorem '
                                 'adipisci. KhR80A.vDNl.RLm.CGhN_a33Dd@OFEGnvg1fBtWCua.ru?')) == \
           sorted(['eKyce39H2OEwh3i_eLQ0GdIYl@2YF3A6cHjAAar.ru', 'UA_D9Ab5RKka5ukyHfzUko9.qsoZ-@-vNJy61H6nLjYCFQw.ca',
                   '_KlD-kD9loANfR0dm6JQ8Jy_AHth@4POm8i3wYkA92fgmo.org',
                   'P0Nntdh0AnFaSoXxzGD0KwF8vOe@p6ybbs0JAdmiMq.ru',
                   'mLdRF6FCJBVw668F@vCQukhDoyunMlvB2g7kmTAa.de', '1Vazeu8XqhqEBo4WphYRF5x@ZhJVnmrc5a.ir',
                   'lHy5aKCgZOl8XpO_@vWfpH21eypOqdR2o2.net', 'KhR80A.vDNl.RLm.CGhN_a33Dd@OFEGnvg1fBtWCua.ru']
                  )


if __name__ == '__main__':
    main()
