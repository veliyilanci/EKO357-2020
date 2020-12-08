#!/usr/bin/env python
# coding: utf-8

# In[1]:


def çift_sayı(sayı):
    if sayı%2==0:
        return "Sayı çifttir."
    else:
        return "Sayı tektir."


# In[2]:


çift_sayı(8)


# In[3]:


def çift(liste):
    for sayı in liste:
        if sayı%2==0:
            return sayı
        else:
            pass


# In[4]:


listem=[1,2,3,4,5,6,7,8]


# In[5]:


çift(listem)


# In[6]:


def çift(lis):
    sayı_listesi=[]
    for sayı in lis:
        if sayı %2==0:
            sayı_listesi.append(sayı)
        else:
            pass
    return sayı_listesi


# In[7]:


çift(listem)


# In[8]:


değerli_metaller=[("Altın",460),("Gümüş",5.95),("Platin",235)]


# In[9]:


for metal, fiyat in değerli_metaller:
    print(fiyat)


# In[11]:


başarı_notu=[("Ali",75),("Can",82),("Cem",88),("Ömer",48)]


# In[13]:


def başarı_kontrolü(liste):
    final_notu=0
    öğrenci=""
    for isim, notum in liste:
        if notum>final_notu:
            final_notu=notum
            öğrenci=isim
        else:
            pass
    return öğrenci, final_notu


# In[14]:


başarı_kontrolü(başarı_notu)


# In[15]:


#Fonksiyonlar Arasında Etkileşim


# In[16]:


# Bul karayı al parayı
# ["Kırmızı", "Kırmızı", "Kara"]


# In[17]:


örnek=[1,2,3,4,5,6,7]


# In[19]:


from random import shuffle


# In[22]:


shuffle(örnek)


# In[23]:


örnek


# In[24]:


def karıştır(kart_listesi):
    shuffle(kart_listesi)
    return kart_listesi


# In[25]:


karıştır(örnek)


# In[26]:


kart_listesi=["Kırmızı","Kara","Kırmızı"]


# In[27]:


def kullanıcı_tahmini():
    tahmin=""
    while tahmin not in ["1","2","3"]:
        tahmin=input("Lütfen 3 karttan birini seçiniz:")
    return int(tahmin)
     


# In[28]:


kullanıcı_tahmini()


# In[30]:


def karşılaştırma(kart_listesi,tahmin):
    if kart_listesi[tahmin-1]=="Kara":
        print("Tebrikler, kazandınız!")
        print(kart_listesi)
    else:
        print("Ne yazık ki, kazanamadınız!")
        print(kart_listesi)


# In[31]:





# In[36]:


yeni_liste=karıştır(kart_listesi)
tahmin=kullanıcı_tahmini()
karşılaştırma(yeni_liste,tahmin)


# In[38]:


# Geçici Argümanlar


# In[44]:


def yuzde(a,b):
    return sum((a,b))*0.05


# In[45]:


yuzde(10,12)


# In[46]:


yuzde(11,99)


# In[47]:


yuzde(4,5,1,3)


# In[48]:


yuzde(1)


# In[49]:


def yuzde(a,b):     return sum((a,b))*0.05


# In[50]:


yuzde(2,3)


# In[51]:


yuzde(12,3344,99)


# In[52]:


yuzde(2,3)


# In[55]:


def yuzde(a,b,c=0,d=0,e=0):
    return (a+b+c+d+e)*0.05


# In[56]:


yuzde(12,11,9)


# In[57]:


yuzde(12,12,3,3,1,2)


# In[58]:


def yuzde(*sayı):
    return sum(sayı)*0.05


# In[63]:


yuzde(2,33,22,100,9,11,9,22)


# In[ ]:




