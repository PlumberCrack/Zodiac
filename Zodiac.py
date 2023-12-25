"""
,-------.          ,--.,--.               
`--.   /  ,---.  ,-|  |`--' ,--,--. ,---. 
  /   /  | .-. |' .-. |,--.' ,-.  || .--' 
 /   `--.' '-' '\ `-' ||  |\ '-'  |\ `--. 
`-------' `---'  `---' `--' `--`--' `---' 
"""
#Recive input from the user what there birthday is 

day = int(input("What is your Birthday?: "))
month = int(input("What is your birth month?: "))


zodiac_found = False

#Check the birthday 
#Aries ---------- ---------- ---------- ---------- 
if month == 3: #March
    if day >= 21 and day <=31:
        print("Your sign is Aries " )
        zodiac_found = True

elif month == 4: #April 
    if day >= 1 and day <= 19: 
     print("Your sign is Aries " )
     zodiac_found = True

#Taurus ---------- ---------- ---------- ---------- 
if month == 4: #April
    if day >= 20 and day <= 30:
        print("Your sign is Taurus " )
        zodiac_found = True

elif month == 5: #May
    if day >= 1 and day <= 20:  
        print("Your sign is Taurus " )
        zodiac_found = True

#Gemini ---------- ---------- ---------- ---------- 
if month == 5: #May
    if day >= 21 and day <= 31:
        print("Your sign is Gemini ")
        zodiac_found = True

elif month == 6: #June
    if day >= 1 and day <= 20:
        print("Your sign is Gemini ")
        zodiac_found = True

#Cancer ---------- ---------- ---------- ---------- 
if month == 6: #June
    if day >= 21  and day <= 30:
        print("Your sign is Cancer ")
        zodiac_found = True

elif month == 7: #July
    if day >= 1 and day <= 22:
        print("Your sign is Cancer ")
        zodiac_found = True

#Leo ---------- ---------- ---------- ---------- 
if month == 7: #July
    if day >= 23  and day <= 31:
        print("Your sign is Leo ")
        zodiac_found = True

elif month == 8: #August 
    if day >= 1 and day <= 22:
        print("Your sign is Leo ")
        zodiac_found = True

#Virgo ---------- ---------- ---------- ---------- 
if month == 8: #August
    if day >= 23  and day <= 31:
        print("Your sign is Virgo ")
        zodiac_found = True

elif month == 9: #Septemeber  
    if day >= 1 and day <= 22:
        print("Your sign is Virgo ")
        zodiac_found = True

#Libra ---------- ---------- ---------- ----------
if month == 9: #September
    if day >= 23  and day <= 30:
        print("Your sign is Libra ")
        zodiac_found = True

elif month == 10: #October  
    if day >= 1 and day <= 22:
        print("Your sign is Libra ")
        zodiac_found = True

#Scorpio ---------- ---------- ---------- ---------- 
if month == 10: #October
    if day >= 23  and day <= 31:
        print("Your sign is Sqoprio ")
        zodiac_found = True

elif month == 11: #November  
    if day >= 1 and day <= 21:
        print("Your sign is Scorpio ")
        zodiac_found = True

#Sagittarius ---------- ---------- ---------- ----------
if month == 11: #November
    if day >= 22  and day <= 30:
        print("Your sign is Sagittarius ")
        zodiac_found = True

elif month == 12: #December  
    if day >= 1 and day <= 21:
        print("Your sign is Sagittarius ")
        zodiac_found = True

#Capricorn ---------- ---------- ---------- ----------
if month == 12: #December
    if day >= 22  and day <= 31:
        print("Your sign is Capricorn ")
        zodiac_found = True

elif month == 1: #January  
    if day >= 1 and day <= 19:
        print("Your sign is Capricorn ")
        zodiac_found = True

#Aquarius ---------- ---------- ---------- ----------
if month == 1: #January
    if day >= 20  and day <= 31:
        print("Your sign is Aquarius ")
        zodiac_found = True

elif month == 2: #February  
    if day >= 1 and day <= 18:
        print("Your sign is Aquarius ")
        zodiac_found = True

#Pisces ---------- ---------- ---------- ----------
if month == 2: #February
    if day >= 19  and day <= 28:
        print("Your sign is Pisces ")
        zodiac_found = True

elif month == 3: #March  
    if day >= 1 and day <= 20:
        print("Your sign is Pisces ")
        zodiac_found = True

if not zodiac_found:
    print("Your input is not correct. Please check your formatting.")



#Zodiac signs ---------- ---------- ---------- ---------- 
"""
!Aries: March 21 - April 19 (3/21 - 4/19)
!Taurus: April 20 - May 20 (4/20 - 5/20)
!Gemini: May 21 - June 20 (5/21 - 6/20)
!Cancer: June 21 - July 22 (6/21 - 7/22)
!Leo: July 23 - August 22 (7/23 - 8/22)
!Virgo: August 23 - September 22 (8/23 - 9/22)
!Libra: September 23 - October 22 (9/23 - 10/22)
!Scorpio: October 23 - November 21 (10/23 - 11/21)
!Sagittarius: November 22 - December 21 (11/22 - 12/21)
!Capricorn: December 22 - January 19 (12/22 - 1/19)
Aquarius: January 20 - February 18 (1/20 - 2/18)
Pisces: February 19 - March 20 (2/19 - 3/20)
"""

#python3 zodiac.py in the terminal to re run this file over and over 

