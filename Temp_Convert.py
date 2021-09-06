print("===============================================")
print("Program Konversi Suhu by Abdul Jabbar Ramadhani")
print("===============================================")

suhu = input("Masukan suhu (Misal: 100C/R/F/K)  : ")
To =   input("Convert To (C/R/F/K)              : ")
print("")
drjt = float(suhu[:-1])
inputan = suhu[-1]

message = "Pastikan Convert C/R/F/K !!!"
c = "Celcius"
f = "Fahrenheit"
k = "Kelvin"
r = "Reamur"

if inputan.upper() == "C":

    if To.upper()=="C":
        hasil0 = float(drjt)
        print(drjt,c,"=","{:.1f}".format(hasil0),c)

    elif To.upper()=="F":
        hasil1 = float((9 * drjt) / 5 + 32)
        print(drjt,c,"=","{:.1f}".format(hasil1),f)

    elif To.upper() == "K":
        hasil2 = float(drjt + 273.15)
        print(drjt,c,"=","{:.2f}".format(hasil2),k)

    elif To.upper() == "R":
        hasil3 = float(4/5 * drjt)
        print(drjt,c,"=","{:.1f}".format(hasil3),r)

    else:
        print(message)
                
elif inputan.upper() == "F":
    
    if To.upper()=="F":
        hasil0 = float(drjt)
        print(drjt,f,"=","{:.1f}".format(hasil0),f)

    elif To.upper()=="C":
        hasil1 = float((drjt - 32) * 5 / 9)
        print(drjt,f,"=","{:.1f}".format(hasil1),c)

    elif To.upper() == "K":
        hasil2 = float(((drjt - 32) * 5 / 9) + 273.15)
        print(drjt,f,"=","{:.2f}".format(hasil2),k)

    elif To.upper() == "R":
        hasil3 = float(4/9 * (drjt-32))
        print(drjt,f,"=","{:.1f}".format(hasil3),r)

    else:
        print(message)

elif inputan.upper() == "K":

    if To.upper()=="K":
        hasil0 = float(drjt)
        print(drjt,k,"=","{:.2f}".format(hasil0),k)

    elif To.upper()=="C":
        hasil1 = float(drjt - 273.15)
        print(drjt,k,"=","{:.2f}".format(hasil1),c)

    elif To.upper() == "F": 
        hasil2 = float(((drjt - 273.15) * 9 / 5)+32)
        print(drjt,k,"=","{:.2f}".format(hasil2),f)

    elif To.upper() == "R":
        hasil3 = float(4/5 * (drjt-273.15))
        print(drjt,k,"=","{:.2f}".format(hasil3),r)

    else:
        print(message)

elif inputan.upper() == "R":
    
    if To.upper()=="R":
        hasil0 = float(drjt)
        print(drjt,r,"=","{:.1f}".format(hasil0),r)

    elif To.upper()=="C":
        hasil1 = float((5/4) * drjt)
        print(drjt,r,"=","{:.1f}".format(hasil1),c)

    elif To.upper() == "F":
        hasil2 = float((9/4 * drjt) + 32)
        print(drjt,r,"=","{:.1f}".format(hasil2),f)

    elif To.upper() == "K":
        hasil3 = float((5/4 * drjt) + 273.15)
        print(drjt,r,"=","{:.2f}".format(hasil3),k)

    else:
        print(message)

else:
    print("Inputan tidak sesuai!! Perhatikan Penulisan Input")
print("===============================================")
