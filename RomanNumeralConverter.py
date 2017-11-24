def roman_numeral_from_string(numeral):
    """
    Converts a roman numeral string into an integer
    :param string: Roman numeral as a string
    :returns int: integer value of string or None if failed to convert
    """
    the_answer = 0
    fail = False
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    broken_numerals = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC']
    
    numeral_chars = 'MDCLXI'
    
    # valid numerals
    if not any((numeral_char in numeral_chars) for numeral_char in numeral):
      return None

    # A Roman numeral longer than 50 would appear to be invalid
    if len(numeral) > 50:
      return None

    # test for incorrect Roman Numerals
    if any(broken_numeral in broken_numerals for broken_numeral in numeral):
      return None

    # test for precedence
    scanpos = 0
    while scanpos < len(numeral) - 1:
      first = numeral[scanpos]
      second = numeral[scanpos + 1]
      if first + second in numerals:
        break
      
      if numerals[second] > numerals[first]:
        fail = True      
      scanpos += 1

    if fail:
      return None

    # calculate value
    pos = 0
    while pos < len(numeral):
      first_two_chars = numeral[pos:pos + 2]
      if first_two_chars in numerals:
        the_answer += numerals[first_two_chars]
        pos += 2  
      else:
        the_answer += numerals[numeral[pos:pos + 1]]
        pos += 1
        
    return the_answer
