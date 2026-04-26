def no(num1,num2):
    if num1%10 < num2%10:
        return num1
    elif num2%10 < num1%10:
        return num2
    else:
        return "Both numbers have the same last digit"