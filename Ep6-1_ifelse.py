'''
condition ในการตรวจสอบอะไรบางอย่าง เข้าเง่ื่อนไขนี้ ทำอะไร เงื่อนไขนั้นทำอะไร
    - if else elif condition
    - while loop , for loop
    - loop in dictionary , loop in list
    - csv reader , writer

    แนะนำ หนังสือ python 101 chulal _ link : https://www.cp.eng.chula.ac.th/~somchai/python101/python101_workbook.html

'''
# if กับ ifelse คนละตัวกัน 
# ถ้า if เฉยๆ แล้วไม่เข้าเงื่อนไข จะไม่แสดงผล / ถ้า if แล้วไม่เข้าเงื่อนไขจะไป else ต่อ

money = 10
if money >= 300:
    print('ไปกินอาหารญี่ปุ่น')
elif money >= 50:
    print('ไปกินร้านป้าแดง')
elif money >= 0 and money < 50 : #ใส่แค่ >= 0: ก็พอเพราะมีการตรวจสอบใน code ก่อนหน้าแล้ว
    print('กลับไปกินที่บ้าน')
else:
     print('กรอกข้อมูลไม่ถูกต้อง')

print('go back to study python')