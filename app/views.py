from django.shortcuts import render

# Create your views here.
from app.models import *
from django.shortcuts import render
import csv
from django.http import HttpResponse

def insert_bank(self):
    with open('C:\\Users\\munep\\Desktop\\DE2\\vamsi\\Scripts\\Bank_Data\\app\\bank.csv') as FO:
        IOD=csv.reader(FO)
        for row in IOD:
            bn=row[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse("Bank data is inserted successfully")


def insert_branch(self):
    with open('C:\\Users\\munep\\Desktop\\DE2\\vamsi\\Scripts\\Bank_Data\\app\\branch1.csv') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for row in IOD:
            bn=row[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=row[1]
                br=row[2]
                ad=row[3]
                co=row[4]
                ci=row[5]
                d=row[6]
                s=row[7]
                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=d,state=s)
                BRO.save()
    return HttpResponse("Branch data is inserted successfully")




