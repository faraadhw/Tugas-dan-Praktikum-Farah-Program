print('Tugas Praktikum 4'.center(35))
nama = 'Farah Diyanah Adhwa'
nim  = '231031046'
prodi= 'Sistem Informasi B'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''

print()
str1 = 'duFort Frankel Von Neumann'
#output: NEUMANN DUFORT FRANKEL VON
print("str1 =",str1)
a = str1.upper()           
b = a.strip("NEUMANN")     
c = "NEUMANN " + b.upper() 
print("output =",c)
print()

str2 = 'duFort Frankel Von Neumann'
print("str2 =",str2)
#output: dfv neumann
a = str2.lower() 
b = a[19:]       
c = "dfv " + b   
print("output =",c) 

print()
str3 = 'duFort Frankel Von Neumann'
print("str3 =",str3)
#output: DUFORT F V N
a = str3.upper() 
b = a[0:6] 
c = a[7]   
d = a[15]  
e = a[19]  
print("output =",b,c,d,e) 

print()
str4 = 'duFOrt Frankel Von Neumann'
print("str4 =",str4)
#output: N duFort f v
a = str4.title()       
b = a.replace("D","d") 
c = b.replace("f","F") 
d = b.lower()    
e = a[19]     
f = c[0:6]    
g = d[7]      
h = d[15]     
print("output =",e,f,g,h) 

print()
str5 = 'DuFort Frankel Von Neumann'
print("str5 =",str5)
#output: NEUMANN d f v
a = str5.replace(str5,"Neumann") 
b = str5.lower() 
c = a.upper() 
d = b[0]    
e = b[7]   
f = b[15]  
print("output =",c,d,e,f)

print()
str6 = 'duFort Frankel Von Neumann'
print("str6 =",str1)
#output: NEUMANN DFV
a = str5.replace(str5,"Neumann") 
b = str5.upper() 
c = a.upper() 
d = b[0]    
e = b[7]   
f = b[15]  
print("output =",c,d+e+f)

print()
str7 = '@duFort Frankel Von Neumann$'
print("str7 =",str7)
#output: duFort Frankel Von NEUMANN
a = str7.strip("@$") 
b = a.strip("Neumann") 
c = str7.replace(str7,"Neumann") 
d = c.upper()  
print("output =",b+d)   

print()
str8 = '#duFort@Frankel@Von@Neumann$'
print("str8 =",str8)
#output: duFort Frankel Von Neumann
a = str8.strip("#$") 
b = a.replace("@"," ") 
print("output =",b)

print()
str9 = '@duFort@#^Frankel*#(Von(#(Neumann$'
print("str9 =",str9)
#output: duFort Frankel Von Neumann
a = str9.strip("@$") 
b = a.replace("@#^", " ") 
c = b.replace("*#(", " ") 
d = c.replace("(#(", " ") 
print("output",d) 

print()
str10 = '@DUFort@!^FraNkel!1(VoN(!(NeuMann^'
print("str10 =",str10)
#output: duFort Frankel Von Neumann
a = str10.strip("@^") 
b = a.replace("@!^"," ") 
c = b.replace("!1("," ") 
d = c.replace("(!("," ") 
e = d.title()            
f = e.replace("D","d")   
g = f.replace("f","F")   
print("output =",g)
