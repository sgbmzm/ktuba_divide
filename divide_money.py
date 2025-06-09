#!/usr/bin/env python
# coding: utf-8


# פונקצייה שמחשבת כמה תקבל כל אחת. 
# הפונקצייה מקבלת שני ארגומנטים: 1. הנשים שצריכות להתחלק תוך פירוט כמה כתובתה של כל אחת 2. כמה כסף הבעל השאיר
def divide_money(debts, total_money_left):
    
    # הסכום המלא של החוב הכולל
    total_debt = sum(debt["ktuba"] for debt in debts)
    
    # אם הסכום שהשאיר הבעל גדול או שווה לסכום החוב הכולל
    if total_money_left >= total_debt:
        # כל אחת תקבל את סכום כתובתה בדיוק
        for debt in debts:
            debt["mekabelet"] = debt["ktuba"]
        return debts
    
    # הגדרת חצי מהחוב הכולל
    half_debt = total_debt / 2
    
    # הגדרת מספר כל הנשים שבאות לחלוק
    total_women_left = len(debts)
    
    # מייון החובות לפי סכום החייוב בסדר עולה מהנמוך לגבוה
    sorted_woman_and_ktubot = sorted(debts, key=lambda x: x['ktuba'])
        
    # בתחילה אנו מגדירים שהכסף שנותר לחלוקה הוא כל הכסף שהבעל השאיר ושמספר המקבלים הוא מספר כל הנשים
    remaining_money = total_money_left
    remaining_women = total_women_left
    
    # עבור כל אשה וכתובה מתוך המערך הממויין של נשים וכתובות
    for debt in debts:
        
        woman = debt["name"]
        ktuba = debt["ktuba"]

        # חישוב כמה זה חצי מהכתובה
        half_ktuba = ktuba / 2
         
        # משתנה שמגדיר האם זו האשה האחרונה לחלוקה
        # אם מספר הנשים שנשארו לחלוקה שווה ל-1 זה אומר שהיא האשה האחרונה
        is_she_the_last = True if remaining_women == 1 else False
        
         
        # חישוב כמה כסף נשאר אחרי שנתנו לה חצי מכתובתה
        # אם הכסף שנשאר לחלוקה פחות חצי מכתובתה של אשה זו לחלק למספר הנשים שיישארו אחריה, גדול או שווה לסכום חצי מכתובתה של האשה הנוכחית, היא תקבל חצי מכתובתה    
        # כל זה בתנאי שהיא לא האשה האחרונה בחלוקה
        if not is_she_the_last and ((remaining_money - half_ktuba) / (remaining_women-1)) >= half_ktuba: #or is_she_the_last and ((remaining_money - half_ktuba)) >= half_ktuba: 
            How_much_will_the_woman_get = half_ktuba # האשה תקבל חצי מכתובתה
            remaining_money = (remaining_money - half_ktuba) # הכסף שנשאר שווה לכסף שנשאר פחות חצי מכתובתה
            # יש להוריד אותה מרשימת הנשים שממתינות לקבל את חלקן
            remaining_women -= 1
            # הוספת הסכום שהיא מקבלת לתוך המילון
            debt["mekabelet"] += How_much_will_the_woman_get
            
        # בכל מקרה אחר שאין מספיק כסף כדי לתת לה חצי מכתובתה לפי הכללים
        else: 
            # הסכום שהיא תקבל שווה לסכום שנשאר חלקי מספר הנשים שנשארו
            How_much_will_the_woman_get = remaining_money / remaining_women
            # אם הסכום של חלוקה שווה גדול מחצי כתובה היא תקבל רק חצי כתובה זה פתרון לאשה האחרונה בחלוקה
            if How_much_will_the_woman_get > half_ktuba:
                How_much_will_the_woman_get = half_ktuba
            remaining_money = (remaining_money - How_much_will_the_woman_get) # הכסף שנשאר שווה לכסף שנשאר פחות מה שהיא מקבלת
            # יש להוריד אותה מרשימת הנשים שממתינות לקבל את חלקן
            remaining_women -= 1
            # הוספת הסכום שהיא מקבלת לתוך המילון
            debt["mekabelet"] += How_much_will_the_woman_get
    
    # אם הסכום שנותר לחלוקה גדול מאפס יש לחלק את השארית למספר הנשים המקורי לפי שיטת החלוקה המתאימה לסכום
    if remaining_money > 0:  
        for debt in debts:
            print(f'{debt["name"]} מקבלת {debt["mekabelet"]}')
        print("לאחר החלוקה הראשונה נשאר", remaining_money, "ולכן התבצע סיבוב חלוקה שני")
        return divide_money(debts, remaining_money)

    # בכל מקרה אחר, הכסף לחלוקה נגמר, והפונקצייה מחזירה את כל המידע
    else:
        return debts
              

# פירוט הנשים שצריכות להתחלק בכסף, ופירוט כמה כתובתה של כל אחת
debts = [
    {"name":"שרה", "ktuba":125, "mekabelet": 0}, 
    {"name":"רבקה", "ktuba":125, "mekabelet": 0}, 
    {"name":"רחל", "ktuba":200, "mekabelet": 0},
    {"name":"לאה", "ktuba":250, "mekabelet": 0}, 
    {"name":"פנינה", "ktuba":300, "mekabelet": 0},
]

# כמה כסף הבעל השאיר
total_money_left_by_husband = 500

# קריאה לפונקצייה שמחשבת כמה תקבל כל אחת. 
# הפונקצייה מקבלת שני ארגומנטים: 1. הנשים שצריכות להתחלק תוך פירוט כמה כתובתה של כל אחת 2. כמה כסף הבעל השאיר
debts = divide_money(debts, total_money_left_by_husband)

print("")
print("סיכום סופי  כדלהלן:")
for debt in debts:
    print(f'{debt["name"]} מקבלת {debt["mekabelet"]}')
    

print(debts)


