monster_hp = 100
equipment = {
    "sword": {"damage": 20,},
    "bow": {"damage": 15,},
    "staff": {"damage": 10,}}

while True:    
    choice = int(input("1. ออกจากเกม\n2. ต่อสู้กับมอนสเตอร์\nเลือก: "))
    
    if choice == "1":
        print("ออกจากเกม")
        break
    
    if choice == 2 :
        while monster_hp > 0:
            print(f"มอนสเตอร์ HP: {monster_hp}")
            weapon = input("เลือกอาวุธ (sword/bow/staff): ").strip().lower()
            if weapon in equipment:
                damage = equipment[weapon]["damage"]
                monster_hp -= damage
                print(f"โจมตีด้วย {weapon} ทำความเสียหาย {damage} HP")
                if monster_hp < 0:
                    monster_hp = 20
            else:
                print("อาวุธไม่ถูกต้อง")