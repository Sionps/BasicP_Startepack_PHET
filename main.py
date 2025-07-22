x = int(input())
y = 0
if x < 5:
    y += 0
elif x >= 5 and x <= 10:
    y += 10
elif x >= 51 and x <= 100:
    y += 15
elif x >= 101 and x <= 300:
    y += 25
elif x >= 301 and x <= 500:
    y += 35
else :
    y += 45

print(x + "กิโลเมตร")
print(y + "บาท")
print((y * 7) / 100 + "บาท")
print(((y * 7) / 100) + y + "บาท")