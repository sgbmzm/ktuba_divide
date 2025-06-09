#!/usr/bin/env python
# coding: utf-8

# In[2]:


# פונקצייה שמחשבת כמה תקבל כל אחת. 
# הפונקצייה מקבלת שני ארגומנטים: 1. הנשים שצריכות להתחלק תוך פירוט כמה כתובתה של כל אחת 2. כמה כסף הבעל השאיר
def divide_money(debts, total_money_left):
    
    # הסכום המלא של החוב הכולל
    total_debt = sum(ktuba for woman, ktuba in debts)
    
    # הגדרת חצי מהחוב הכולל
    half_debt = total_debt / 2
    
    # הגדרת מספר כל הנשים שבאות לחלוק
    total_women_left = len(debts)
    
    # מייון החובות לפי סכום החייוב בסדר עולה מהנמוך לגבוה
    sorted_woman_and_ktubot = sorted(debts, key=lambda x: x[1])
    
    # בתחילה אנו מגדירים שהכסף שנותר לחלוקה הוא כל הכסף שהבעל השאיר ושמספר המקבלים הוא מספר כל הנשים
    remaining_money = total_money_left
    remaining_women = total_women_left
    
    # עבור כל אשה וכתובה מתוך המערך הממויין של נשים וכתובות
    for woman, ktuba in sorted_woman_and_ktubot:
        
        # חישוב כמה זה חצי מהכתובה
        half_ktuba = ktuba / 2
        
        
        print("שם האשה",woman)
        print("חצי כתובתה",half_ktuba)
        #print("הסכום שנשאר לחלוקה לפני שהיא מקבלת",remaining_money)
        #print("מספר הנשים שנשארו לחלוקה לפני שהיא מקבלת",remaining_women)
        print("מספר הנשים שיישארו לחלוקה אחרי שהיא תקבל",remaining_women-1)
        print("סכום שיישאר לחלוקה אחרי שתקבל חצי מכתובתה",(remaining_money - half_ktuba))
        #print("כמה כל אחת תקבל אם יחלקו את מה שנשאר אחרי שהיא תקבל חצי כתובה לכל מי שנשארה אחריה",(remaining_money - half_ktuba) / (remaining_women-1))
        
        
        # משתנה שמגדיר האם זו האשה האחרונה לחלוקה
        # אם מספר הנשים שנשארו לחלוקה שווה ל-1 זה אומר שהיא האשה האחרונה
        is_she_the_last = True if remaining_women == 1 else False
        
         
        # חישוב כמה כסף נשאר אחרי שנתנו לה חצי מכתובתה
        # אם הכסף שנשאר לחלוקה פחות חצי מכתובתה של אשה זו לחלק למספר הנשים שיישארו אחריה, גדול או שווה לסכום חצי מכתובתה של האשה הנוכחית, היא תקבל חצי מכתובתה    
        if ((remaining_money - half_ktuba) / (remaining_women-1 if not is_she_the_last else remaining_women)) >= half_ktuba: 
            How_much_will_the_woman_get = half_ktuba # האשה תקבל חצי מכתובתה
            remaining_money = (remaining_money - half_ktuba) # הכסף שנשאר שווה לכסף שנשאר פחות חצי מכתובתה
            # יש להוריד אותה מרשימת הנשים שממתינות לקבל את חלקן
            remaining_women -= 1
            # הדפסה כמה היא תקבל
            print(f'{woman} תקבל סך {How_much_will_the_woman_get} שהוא חצי מכתובתה')
            #print("סכום שיישאר לחלוקה אחרי שתקבל חצי מכתובתה",((remaining_money - half_ktuba) / remaining_women))
        
        # בכל מקרה אחר שאין מספיק כסף כדי לתת לה חצי מכתובתה לפי הכללים
        else: 
            # הסכום שהיא תקבל שווה לסכום שנשאר חלקי מספר הנשים שנשארו
            How_much_will_the_woman_get = remaining_money / remaining_women
            remaining_money = (remaining_money - How_much_will_the_woman_get) # הכסף שנשאר שווה לכסף שנשאר פחות מה שהיא מקבלת
            # יש להוריד אותה מרשימת הנשים שממתינות לקבל את חלקן
            remaining_women -= 1
            if How_much_will_the_woman_get == half_ktuba:
                print(f'{woman} תקבל סך {How_much_will_the_woman_get} שהוא חצי מכתובתה')
            else:
                print(f'{woman} תקבל סך {How_much_will_the_woman_get} מפני שלא נשאר מספיק כדי לתת לה חצי מכתובתה לפי הכללים')
            
    print("הכסף שנשאר לחלוקה אחרי שכולם קיבלו", remaining_money)
        
# פירוט הנשים שצריכות להתחלק בכסף, ופירוט כמה כתובתה של כל אחת
debts = [("Sara", 100), ("rivka", 200), ("Rachel", 300)]

#debts = [('Sara', 125), ('rivka', 125), ('Rachel', 200), ('Leaa', 250), ('Pnina', 300)]

# כמה כסף הבעל השאיר

#########  כרגע יש בעייה בשארית של האשה האחרונה מתוך 3 נשים שמקבלת יותר מחצי בלי חלוקה שווה כשיש יותר מ-300 ופחות מ- 450  #############
total_money_left_by_husband = 300

# קריאה לפונקצייה שמחשבת כמה תקבל כל אחת. 
# הפונקצייה מקבלת שני ארגומנטים: 1. הנשים שצריכות להתחלק תוך פירוט כמה כתובתה של כל אחת 2. כמה כסף הבעל השאיר
divide_money(debts, total_money_left_by_husband)

