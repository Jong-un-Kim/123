
def f(money,interest,month):
    result = 0
    month=int(month)
    for i in range (month):
        result+=money*((interest+100)/100)**(month-i)
    return result
print(f(1000,10,12))