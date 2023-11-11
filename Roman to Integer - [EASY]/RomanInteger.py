############ INSTRUCTIONS ##############
########################################

#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.

 

#Example 1:

#Input: s = "III"
#Output: 3
#Explanation: III = 3.
#Example 2:

#Input: s = "LVIII"
#Output: 58
#Explanation: L = 50, V= 5, III = 3.
#Example 3:

#Input: s = "MCMXCIV"
#Output: 1994
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

#Constraints:

#1 <= s.length <= 15
#s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#It is guaranteed that s is a valid roman numeral in the range [1, 3999].

############### EXERCISE ###############
########################################

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    l = len(s)
    cpt = 0
    skip = False
    for i in range (0,l):
        if (skip):      # adding a skip line in case a double digit roman number is detected, as i cannot be manually incremented
            skip = False 
            continue

        if (i < l - 1):
            if ((s[i] == "I") and (s[i+1] == "V")):
                cpt += 4
                skip = True
                continue

            if ((s[i] == "I") and (s[i+1] == "X")):
                cpt += 9
                skip = True
                continue

            if ((s[i] == "X") and (s[i+1] == "L")):
                cpt += 40
                skip = True
                continue

            if ((s[i] == "X") and (s[i+1] == "C")):
                cpt += 90
                skip = True
                continue
            
            if ((s[i] == "C") and (s[i+1] == "D")):
                cpt += 400
                skip = True
                continue
            
            if ((s[i] == "C") and (s[i+1] == "M")):
                print("test")
                cpt += 900
                skip = True
                continue
        
        if (s[i] == "I"): cpt += 1
        if (s[i] == "V"): cpt += 5
        if (s[i] == "X"): cpt += 10
        if (s[i] == "L"): cpt += 50
        if (s[i] == "C"): cpt += 100
        if (s[i] == "D"): cpt += 500
        if (s[i] == "M"): cpt += 1000
        
    return cpt

print(romanToInt("MCMXCIV"))

### SECOND VERSION ###

def romanToIntV2(s: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    cpt = 0
    l = len(s)
    
    for i in range(l):
        if i < l - 1 and values[s[i]] < values[s[i+1]]:
            cpt -= values[s[i]]             #if the following roman digit is higher than the current one, then we remove the current one
        else:
            cpt += values[s[i]]
    
    return cpt

# the logic of removing a number if the next one is higher comes from the logic of roman numbers : IX = 9 because it's 10 - 1
# we just need to look at it in a mirrored way, 9 is as well -1 + 10

print(romanToIntV2("MCMXCIV"))