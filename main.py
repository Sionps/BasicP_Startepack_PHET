x = int(input())
y = 0

if x < 5:
    y = 0
elif 5 <= x <= 10:
    y = 10
elif 51 <= x <= 100:
    y = 15
elif 101 <= x <= 300:
    y = 25
elif 301 <= x <= 500:
    y = 35
else:
    y = 45

vat = (y * 7) / 100
total = y + vat

print(f"{x} กิโลเมตร")
print(f"{y} บาท")
print(f"ภาษีมูลค่าเพิ่ม 7%: {vat:.2f} บาท")
print(f"รวมเป็นเงิน: {total:.2f} บาท")
