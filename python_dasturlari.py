print("ASSALOMU ALYKUM, \n\t\t\tDO'STLAR UCHUN\n NOMLI DASTURLAR YIG'INDISI ISHGA TUSHDI!!!! ")


mehmonlar = ['Bunyod']
for mehmon in mehmonlar:
    print(f"Assalomu alaykum, {mehmon} sizni 1-iyul\n Farangizning tug'ilgan kuniga\n taklif qilaman\n. Bu kun uchun men sizlarga\n turli dasturlar tayyorlaganman ")
    print("Hurmat bilan Boltaev Yodgorbek\n")


ism = input("Ismingiz nima?\n>>>")
print("Assalomu alaykum "  + ism.upper())


t_yil = int(input(ism.title() + " tug'ilgan yilingizni kiriting\n>>>"))
yosh = 2022-t_yil
print(f"{ism.title()} siz {yosh} yoshda ekansiz")


t_vil = input(ism.title() + " tug'ilgan viloyatingizni kiriting\n>>>")
t_tum = input(ism.title() + " qaysi tumanda tug'ilgansiz\n>>>")
t_mah = input(ism.title() + " qaysi mahallada tug'ilgansiz\n>>>")
t_koch = input(ism.title() + " qaysi ko'chada yashaysiz\n>>>")
print(f" Shaxs xaqidagi ma'lumotlar: {ism.title()}  siz  {t_vil.title()} viloyati  {t_tum.title()} tumani  {t_mah.title()} mahallasi  {t_koch.title()} ko'chasida yashar ekansiz ")


print("Misollar dasturi")


savol = int(input("1-misol.\n 234ni kvadrati qancha?\n234**2="))
if savol == 54756:
    print("Javob to'g'ri\n")
    print("Sizni tabriklayman\n")
else:
    print("Javob xato")
    print("To'gri javob 54756 edi\n")
    
savol = int(input("2-misol.\n 900ni 2ga ko'paytiring\n900*2="))
if savol == 1800:
    print("Javob to'g'ri\n")
    print("Sizni tabriklayman\n")
else:
    print("Javob xato")
    print("To'gri javob 1800 edi\n")


print("Do'konimizga xush kekimsiz")
d_mahsulotlar = ['mevalar','piyoz','banan','non','suv','pomidor','muzqaymoq','qatiq','qand','tort','pechenya','sabzi','baliq','yog\'']


dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):      
      dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting: "))
print(dostlar)


for n in range(2):kinolar = []
print("5 ta sevimli kinolaringizni kiriting?")
for k in range(5):
     kinolar.append(input(f"{k+1}-kino:"))                        
print(f"{ism} sizni sevimli kinolaringiz {kinolar}")


print("Muzeyga marhamat!!!")
yosh = int(input("Yoshingiz nechada?"))
if yosh<10 or yosh>60:
    print('Muzeyga kirish bepul!')
elif yosh<18:
    print("Muzeyga kirish 10000 so'm")
elif yosh>18:
    print("Muzeyga kirish 20000 so'm")
else:
    print("Muzeyga kirish bepul!")


mahsulotlar = {
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'anjir': 25000,
    'shaftoli': 30000
    }
bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")


car0 = {
        'model':'lasetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
       'model':'nexia 3',
        'rang':'qora',
       'yil':2015,#
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
     'yil': 2019,
        'narh':13000,
        'km':20000,
        'korobka':'mexanika'}
car = car0
print(f"{car['model'].title()}, "
      f"{car['rang']} rang, "
      f"{car['yil']}-yil, {car['narh']} $$")

cars =[car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$$")


print(cars[0]['model'])        

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'km':0,
        'korobka':'auto'
        }
    malibus.append(new_car)
print(malibus)
for malibu in malibus[:3]:
    malibu['rang']='qizil'
for malibu in malibus[3:6]:
    malibu['rang']='qora'
for malibu in malibus[6:]:
    malibu['rang']='oq'

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],#
    }
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi tillarni biladi")
    for til in tillar:
        print(til.upper())
        
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi tillarni biladi")
    for til in tillar:
        print(til.upper(),  end= '')
  
print("Buyurtma berish dasturi\n")
savat = []
while True:
    mahsulot = input("\nBuyurtma kiriting:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo\'shasizmi? (ha/yo'q)\n")
    if javob != "ha":
       break
print(f"Siz buyurtma bergan \nmahsulotlar ro'yxati {savat}")                    

talabalar = ['hasan','husan','olim','botir']#
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = (baho)
print(baholangan_talabalar)