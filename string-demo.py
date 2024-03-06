website = "www.aslankariyer.com"
course= "aslan kariyer ile iş bulma kolaylığın farkına var iki gün içerisinde mülakat!"

# karakter dizesinde kaç karakter bulunmaktadır?
result = len(course)
length = len(website)

# website'nin içinden www alın
result = website[0:3]

# websitesinden com alın
result = website[17:20]
result =  website[length-3:length]

 #course içinden ilk 15 ve son 15 karakteri alalım

result =course[:15]
result =course[-15:]

#course içindeki karakterleri tersten yazdır

result = course[::-1]

print(result)

""" 
 adım sayısı :: sonra 1-2-3-4 gibi değer atarsan ikişer ikişer atlayarak alır
s = "12345" * 5
print(s[::5])
"""

name, surname, age, job ="batuhan", "vural", 25, "kodcu"

print(f"my name is {name} and my surname is {surname} ı'am {age} years old and ı'am a {job}")


#hello world ifadesini değiştirin

s = "hello world"
s = s[0:6] + "W" + s[-4:]
s.replace("w","W")
print(s)

#abc 3 kere ard arda yazdır

x= "abc " * 3
print(x)

