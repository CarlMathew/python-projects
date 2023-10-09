user_grade = int(input("What is your grades? "))
def smart_check(grades: int) -> bool:
    if grades > 75:
        smart = True
    elif 60 < grades < 75:
        smart = False
    else:
        return "Bobo Talaga"
    return smart

if smart_check(user_grade) == "Bobo Talaga":
    print("Wala Kana Atang Pagasa")
elif smart_check(user_grade):
    print("Matalino tong Batang to")
else:
    print("Kaya pa yan bawi ka next year")
