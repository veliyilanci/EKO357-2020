#!/usr/bin/env python
# coding: utf-8

# In[1]:


sozluk={"k1":1,"k2":2,"k3":3}


# In[2]:


for harf in sozluk:
    print(harf)


# In[3]:


for harf in sozluk.items():
    print(harf)


# In[4]:


for a,b in sozluk.items():
    print(b)


# In[5]:


for anahtar,değer in sozluk.items():
    print(değer)


# In[6]:


#Range fonksiyonu


# In[7]:


#range(başlangıç elemanı, bitiş elemanı, artış değeri)


# In[9]:


print(*range(0,10,1))


# In[10]:


print(*range(0,10))


# In[11]:


print(*range(10))


# In[12]:


print(*range(1,200,3))


# In[13]:


listem=list(range(0,200,4))


# In[14]:


print(listem)


# In[15]:


print(*range(200,8,-6))


# In[16]:


for sayı in range(0,25,3):
    print(sayı)


# In[18]:


for sayı in range(1,1001,1):
    if sayı%7==0:
        print(f'{sayı} 7 ile tam bölünür.')
    else:
        print(f'{sayı} 7 ile tam bölünmez.')
        


# In[26]:


for sayı in range(1,1001,1):
    if sayı%7==0:
        print(sayı)


# In[32]:


#Enumerate


# In[33]:


isim="Veli"


# In[34]:


for harf in enumerate(isim):
    print(harf)


# In[37]:


for indeks,harf in enumerate(isim):
    print(harf)
   


# In[38]:


#Zip


# In[39]:


listem1=[1,2,3,4,5,6,7,8,9,10]


# In[40]:


listem2=["a","b","c","d","e","f","g","h","i","j"]


# In[41]:


zip(listem1,listem2)


# In[42]:


print(*zip(listem1,listem2))


# In[43]:


for eko in zip(listem1,listem2):
    print(eko)


# In[44]:


listem3=[100,200,300,400,500]


# In[45]:


print(*zip(listem1,listem2,listem3))


# In[48]:


for x,y,z in zip(listem1,listem2,listem3):
    print(y)


# In[49]:


#in


# In[50]:


"a" in listem2


# In[51]:


"b" in listem3


# In[52]:


"v" in "veli"


# In[53]:


#min ve max


# In[54]:


min(listem1)


# In[55]:


max(listem3)


# In[56]:


#Break & Continue


# In[57]:


a=0
while a<15:
    print(a)
    a+=1


# In[58]:


a=0
while a<15:
    print(a)
    if a==8:
        break
    a+=1


# In[62]:


for sayı in listem1:
    if sayı==5:
        break
    print(sayı) #bu satıra geçmiyor komut


# In[63]:


a=0
while a<15:
    if a==8:
        break
    print(a)
    a+=1
    


# In[64]:


#Sonsuz Döngü


# In[68]:


while True:
    çıkış=input("Çıkmak için q harfine basınız!")
    if çıkış=="q":
        print("Programdan çıkış yapılıyor!")
        break


# In[70]:


for sayı in listem1:
    print("a",sayı)


# In[71]:


for sayı in listem1:
    if sayı==4 or sayı==5:
        continue
    print("a",sayı)


# In[73]:


while True:     
    çıkış=input("çıkmak için q harfine basınız")     
    if çıkış=="q":         
        print("programdan çıkış yapılıyor")         
        break


# In[74]:


#Kütüphane


# In[76]:


#from kütüphaneadı import fonksiyon


# In[77]:


from random import shuffle
shuffle(listem1)


# In[79]:


print(listem1)


# In[80]:


from random import randint
randint(0,100)


# In[81]:


randint(0,5000)


# In[82]:


#List Comprehension


# In[ ]:




