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

def multi_inverse(inv,mod):
    for i in range(99):
        if(((inv *i)%mod)==1):
            return i
            break

def result(request):
   p= int(request.POST['pval'])
   q=int(request.POST['qval'])
   h=int(request.POST['hval'])
   if(h!=0):
       h_t=h
   x=int(request.POST['xval'])
   y=int(request.POST['yval'])
   g=int(request.POST['gval'])
   k=int(request.POST['kval'])
   if(h==0):
       h=random.randint(2,p-1)
   if(x==0):
       x=random.randint(0,q)
   if(g==0):
       g=h**((p-1)/q)%p
   if(y==0):
       y=(g**x)%p
   #signature component:
   if(k==0):
      k=random.randint(1,q)
   r=((g**k)%p)%q
   k_inv=multi_inverse(k,q)
   s_split=h+(x*r)
   s=(k_inv*s_split)%q
   sig=[r,s]
   #verification functions:
   s_inv=multi_inverse(s,q)
   w=s_inv%q
   u1=(h*w)%q
   u2=(r*w)%q
   v=((g**u1)*(y**u2)%p)%q

   return render(request,'result.html',{'res':r,'res2':v,'res3':h_t})