# Задача 1
#https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python
def past(h, m, s):
    ms = int(3600000 * h + 60000 * m + 1000 * s)
    return ms

print(past(0,1,1))

# Выполнено
