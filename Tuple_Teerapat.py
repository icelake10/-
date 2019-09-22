#!/usr/bin/env python
# coding: utf-8

# 1.กำหนดให้ brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
# 
# 1.1 ให้เขียนคำสั่งโปรแกรมแสดงตำแหน่งของ Benz, Ford และ Volvo
# 1.2 ให้เขียนคำสั่งโปรแกรมแสดงจำนวนข้อมูลทั้งหมดในทูเพิล
# 1.3 ให้เขียนคำสั่งโปรแกรมตรวจสอบมียี่ห้อรถ Suzuki, Ferrari, Ford อยู่ใน cars หรือไม่

# In[3]:


brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Tesla", "Ford", "KIA", "Volvo" )
print("ตำแหน่งของ Benz คือ",brand_cars.index("Benz"))
print("ตำแหน่งของ Ford คือ",brand_cars.index("Ford"))
print("ตำแหน่งของ Volvo คือ",brand_cars.index("Volvo"))
print("จำนวนข้อมูลทั้งหมดในทูเพิล คือ",len(brand_cars),"แบน")
print("มีแบนรถยน Suzuki อยู่ใน brand_cars หรือไม่ =","Suzuki" in brand_cars)
print("มีแบนรถยน Ferrari อยู่ใน brand_cars หรือไม่ =","Ferrari" in brand_cars)
print("มีแบนรถยน Ford อยู่ใน brand_cars หรือไม่ =","Ford" in brand_cars)


# In[ ]:




