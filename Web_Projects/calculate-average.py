# مثال على حساب متوسط درجات الطلاب باستخدام Python

def calculate_average(grades):
    return sum(grades) / len(grades)

# إدخال درجات الطلاب
grades = [85, 90, 78, 92, 88]

# حساب المتوسط
average = calculate_average(grades)

print("The average grades is:", average)
