#!/usr/bin/env python
# coding: utf-8

# In[1]:


#liste kavrama _ list comprehension


# In[2]:


kelime="ekonometri"
listem=[]
for harf in kelime:
    listem.append(harf)
print(listem)


# In[3]:


listem1=[harf for harf in kelime]
print(listem1)


# In[4]:


listem2=[x for x in "Merhaba"]


# In[5]:


print(listem2)


# In[6]:


listem3=[2 for eleman in "Sakarya"]


# In[7]:


print(listem3)


# In[8]:


listem4=[eleman for eleman in "Sakarya"]


# In[9]:


print(listem4)


# In[10]:


listem5=[1,2,3,4,5,6,7,8]
listem6=[x for x in listem5]
print(listem6)


# In[11]:


listem7=[1,2,3,4,5,6,7,8,9,10]
listem8=[x**2 for x in listem7]
print(listem8)


# In[13]:


listem9=[x**3 for x in [3,4,5,6]]
print(listem9)


# In[14]:


listem10=[(1,2),(3,4),(5,6)]
print(listem10)


# In[15]:


listem11=[b for a,b in listem10]
print(listem11)


# In[16]:


liste1=[a*b for a,b in listem10]
print(liste1)


# In[18]:


print(listem7)


# In[20]:


liste2=[x**3 for x in listem7 if x>5]
print(liste2)


# In[21]:


liste3=[sayı for sayı in range(0,50)]
print(liste3)


# In[23]:


liste3=[sayı for sayı in range(0,100) if sayı%2==0]
print(liste3)


# In[25]:


liste4=[sayı for sayı in range(0,1000) if sayı%13==0]
print(liste4)


# In[29]:


liste5=[]
for a in [1,3,5,7,9]:
    for b in [2,4,6,8,10]:
        liste5.append(a*b)
print(liste5)


# In[30]:


liste6=[x*y for x in [1,3,5,7,9] for y in [2,4,6,8,10]]
print(liste6)


# In[31]:


# Yöntemler / methods


# In[32]:


print(liste2)


# In[33]:


liste2.append(9999)


# In[34]:


print(liste2)


# In[35]:


liste2.count # shift + Tab


# In[36]:


help(liste2.count)


# In[37]:


#docs.python.org


# In[38]:


#FONKSİYONLAR


# In[39]:


# def fonksiyon.adı():
    #"bu fonk. ..."
    #....


# In[40]:


def karşılama():
    "Bu komut misafirleri karşılamak için oluşturulmuştur..."
    print("Otelimize Hoşgeldiniz.")


# In[41]:


karşılama()


# In[42]:


karşılama()


# In[47]:


def selamlama(isim):
    print("Sayın",isim,"otelimize hoşgeldiniz...")


# In[49]:


selamlama("veli")


# In[50]:


selamlama("ali")


# In[51]:


selamlama(222)


# In[52]:


def toplama(a,b,c,d):
    print(a+b+c+d)


# In[53]:


toplama(1,4,5,7)


# In[54]:


selamlama()


# In[55]:


def selamlama(isim="Müşteri"):
    print("Sayın", isim, "otelimize hoşgeldiniz.")


# In[56]:


selamlama("veli")


# In[57]:


selamlama()


# In[58]:


#faktöriyel


# In[59]:


# 4! = 4*3*2*1
# 12!= 12*11*10*9*8*7*6*5*4*3*2*1
#1!=1
#0!=1


# In[62]:


def faktöriyel(sayı):
    faktör=1
    if sayı==0 or sayı==1:
        print(faktör)
    elif sayı<0:
        print("Pozitif bir sayı giriniz.")
    else:
        while sayı >=1:
            faktör=faktör*sayı
            sayı=sayı-1
        print(faktör)


# In[63]:


faktöriyel(3)


# In[64]:


faktöriyel(11)


# In[65]:


faktöriyel(100)


# In[66]:


faktöriyel(0)


# In[67]:


faktöriyel(-1)


# In[68]:


faktöriyel(4)


# In[69]:


faktöriyel(4)*2


# In[73]:


type(faktöriyel(3))


# In[74]:


#return


# In[75]:


def toplama(sayı1,sayı2):
    print(sayı1+sayı2)


# In[76]:


toplama(3,2)


# In[77]:


toplama(3,4)*5


# In[78]:


def toplama1(sayı1,sayı2):
    return sayı1+sayı2


# In[81]:


toplama1(3,4)


# In[82]:


toplama1(3,4)*5


# In[83]:


def faktöriyel(sayı):
    faktör=1
    if sayı==0 or sayı==1:
        return faktör
    elif sayı<0:
        return "Pozitif bir sayı giriniz."
    else:
        while sayı >=1:
            faktör=faktör*sayı
            sayı=sayı-1
        return faktör


# In[84]:


faktöriyel(3)*4


# In[85]:


faktöriyel(-1)


# In[86]:


faktöriyel(5)**2


# In[87]:


faktöriyel(4)**0.5


# In[88]:


def çift(sayı):
    if sayı%2==0:
        return "Sayı çifttir."
    else:
        return "Sayı tektir."


# In[89]:


çift(12)


# In[90]:


çift(13)


# In[ ]:




