# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 17:50:59 2022

@author: Ogabek
"""

#son = -5
#while son<=5:
#    print(son, end=' ')
#    son = son + 1


#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
        
#print("Sonning kvadratini hisoblaydigan dastur")
#savol = "Istalgan son kiriting  "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#       ishora = False
#    else:
#        print(float(qiymat)**2)
        
        
#print("Sonning kvadratini hisoblaydigan dastur")
#savol = "Istalgan son kiriting  "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#while True:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#       break
#    else:
#        print(float(qiymat)**2) 

#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5     :
#        break
#    print(son)
#    print(f"{son} sonning kvadrati {son**2} ga teng")


#son = 0
#while son<10:
#   son += 1
#   if son%2!=0:
#       continue
#   else:
#       print(son)
    
    
    
#ismlar = []
#print("Yoqin do'stlaringiz ro'yxatini tuzmamiz")
#n=1
#while True:
#    savol = f"{n}-do'stingiz kim?"
#    ism = input(savol)
#    ismlar.append(ism)
#    javob = input("Yana ism kiritasizmi? (ha/yo'q)")
#    if javob == 'ha':
#        n+=1
#        continue
#    else:
#           break
#print("Do'stlaringiz ro'yxati") 
#for ism in ismlar:    
#   print(ism.title() )


#print("Do'stlaringiz ro'yxatini tuzamiz")
#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("Do'stingiz ismini kiritng")
#    yosh = input(f"{ism.title()}ni yoshini kiriting")
#    dostlar[ism] = int(yosh)
#    javob = input("Yana ism qo'shasizmi (ha/yo'q)")
#    if javob == "yo'q":
#        ishora = False
#   for ism,yosh in dostlar.items():
#        print(f"{ism.title()} {yosh} yoshda")

#cars = ['lacetti','nexia','toyota','nexia','audi','malibu']
#while 'nexia' in cars:
#     cars.remove('nexia')
#     print(cars)


#talabalar = ['hasan','husan','olim','botir']
#baholangan_talabalar = {}
#while talabalar:
#    talaba = talabalar.pop()
#    baho = input(f"{talaba.title()} ning bahosini kiritng: ")
#    print(f"{talaba.title()}  baholandi")
#    baholangan_talabalar[talaba] = baho
#print(baholangan_talabalar)    



print("Aylananning radiusi, diametri, perimetri va yuzsini aniqalaydi")
def hisobla(radius,pi=3.14159):
    aylana = {'radius':radius,
              'diametr':2*radius,
              'perimetr':2*radius*pi,
              'yuza':pi*radius**2}
    return aylana

son = hisobla(10)
print(son)