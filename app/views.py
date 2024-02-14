from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
import csv

def insert_bank(self):
    with open('C:\\Users\\dspsu\\OneDrive\\Desktop\\Djangoprojects\\Msb1\\Scripts\\projectnd19csv\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank data inserted successfully')



def insert_branch(self):
    with open('C:\\Users\\dspsu\\OneDrive\\Desktop\\Djangoprojects\\Msb1\\Scripts\\projectnd19csv\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifsc=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                ci=i[5]
                di=i[6]
                st=i[7]

                BRO=Branch(bank_name=BO[0],ifsc=ifsc,branch=br,address=ad,contact=co,city=ci,district=di,state=st)
                BRO.save()
    return HttpResponse('Branch data inserted successfully')