from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    return render(request, 'index.html')

def multi_inverse(request):
    return render(request, 'multi.html')

def about(request):
    return render(request, 'about.html')

def dsa_alg(request):
    return render(request,'dsa.html')

def multi_invers(inv,mod):
    for i in range(99):
        if(((inv *i)%mod)==1):
            return i
            break

def result(request):
   x_f=0
   g_f=0
   h_f=0
   k_f=0
   y_f=0
   p= int(request.POST['pval'])
   q=int(request.POST['qval'])
   h=int(request.POST['hval'])
   x=int(request.POST['xval'])
   y=int(request.POST['yval'])
   g=int(request.POST['gval'])
   k=int(request.POST['kval'])
   if(h==0):
       h_f=1
       h=random.randint(1,p-1)
   if(x==0):
       x_f=1
       x=random.randint(1,q-1)
   if(g==0):
         g_f=1
         g=round(h**((p-1)/q)%p)
   if(y==0):
         y_f=1
         y=round((g**x)%p)
   #signature component:
   if(k==0):
        k_f=1
        k=random.randint(1,q-1)
   r=round(((g**k)%p)%q)
   k_inv=multi_invers(k,q)
   s_split=h+(x*r)
   s=(k_inv*s_split)%q
   sig=[r,s]
   #verification functions:
   s_inv=multi_invers(s,q)
   w=s_inv%q
   u1=(h*w)%q
   u2=(r*w)%q
   v=round(((g**u1)*(y**u2)%p)%q)


   return render(request,'result.html',{'p':p,'q':q,'h':h,'g':g,'x':x,'y':y,'k':k,'r':round(r),'k_inv':k_inv,'s_sp':s_split,'s':s,'sig':sig,'s_inv':s_inv,'w':w,'u1':u1,'u2':u2,'v':v,'g_f':g_f,'h_f':h_f,'x_f':x_f,'k_f':k_f,'y_f':y_f})