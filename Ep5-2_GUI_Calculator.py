from tkinter import *  # star คือ import function main (package main) ทั้งหมด ใน tkinter  
from tkinter import ttk , messagebox  # < -- ttk , messagebox เป็น package ย่อย ใน tkinter จึงต้อง import เพิ่ม (นอกเหนือ *)

GUI = Tk() 
GUI.title('โปรแกรมคำนวณราคาปลา')

GUI.geometry('700x600') # กำหนดขนาดหน้าต่างโปรแกรม

# ใส่รูปภาพโดยใช้ image แนะนำ website : iconAchive (https://www.iconarchive.com/)
# ภาพต้องแลงเป็น PNG ที่สมบูรณ์ก่อนถึงจะใส่ได้


#bg = PhotoImage(file='icon_mart.png')
bg = PhotoImage(file=r'C:\Users\Thuwa\Desktop\Python\Uncle Engineer\Python for Beginners from Zero\Note code 2024\Ep.5\icon_mart.png')
# ใช้ Full directory ต้องมี r (raw text) หน้า 'Path file directory of photo'
BG = Label(GUI, image=bg)
BG.pack()


L = Label(GUI, text = 'กรุณากรอกจำนวนปลา(kg)' , font = (None, 20))
L.pack()  # pack เพื่อเอาคำสั่ง Label ตัวนี้ไปติดกับโปรแกรมของเรา

v_quantity = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเทื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable= v_quantity , font = (None, 20))
E1.pack()

def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 39 # 39 บาท ต่อ กิโล x จำนวนที่กรอกมา 
        messagebox.showinfo('ราคาทั้งหมด', 'ราคาปลาทังหมด {} บาท' .format(calc))
        v_quantity.set('')
        E1.focus() # เป็นการ focus ช่องที่ต้องการกรอกต่อเนื่อง 
    except:
        messagebox.showwarning('กรอกผิด' , 'กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set('')  # set ที่กรอกผิดให้เป็นว่างเปล่า
        E1.focus() 

B = ttk.Button (GUI, text = 'คำนวณ' , command = Cal)
B.pack(ipadx = 10  , ipady= 5 , pady = 10) # ipad ขยายความกว้าง x,y


GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา
