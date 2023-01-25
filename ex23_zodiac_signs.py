def zodiac(year):
    # return the corresponding zodiac sign
    # Example: zodiac(2000) == 'Dragon'

    zodiac = {0: 'Monkey', 1: 'Rooster', 2: 'Dog', 3: 'Pig', 4: 'Rat', 5: 'Ox', 6: 'Tiger', 7: 'Rabbit', 8: 'Dragon', 9: 'Snake', 10: 'Horse', 11: 'Sheep'}

    return zodiac[year % 12]

def main():
    # Note: This is only for student-side debugging
    assert zodiac(2000) == 'Dragon'
    assert zodiac(2001) == 'Snake'
    assert zodiac(2002) == 'Horse'
    assert zodiac(2003) == 'Sheep'
    assert zodiac(2004) == 'Monkey'
    assert zodiac(2005) == 'Rooster'
    assert zodiac(2006) == 'Dog'
    assert zodiac(2007) == 'Pig'
    assert zodiac(2008) == 'Rat'
    assert zodiac(2009) == 'Ox'
    assert zodiac(2010) == 'Tiger'
    assert zodiac(2011) == 'Rabbit'

if __name__ == '__main__':
    main()