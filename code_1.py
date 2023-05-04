total = 0;
counter = 1;
while counter <= 10:
    grade = int(input("enter grade:"))
    total = grade + total;
    counter = counter + 1;
average = total / 10;
print("평균은",average),"입니다"

