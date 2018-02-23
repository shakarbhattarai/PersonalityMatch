# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render
from plot_digits_agglomeration import GetCompatibility
from .models import PersonalityDetails
from django.shortcuts import redirect
import pandas as pd

ColNames=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','B1','B2','B3','B4','B5','B6','B7','B8',
'B9','B10','B11','B12','B13','C1','C2','C3','C4','C5',
 'C6','C7','C8','C9','C10','D1','D2','D3','D4','D5','D6','D7','D8','D9',
 'D10','E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','F1','F2','F3',
 'F4','F5','F6','F7','F8','F9','F10','G1','G2','G3','G4','G5','G6','G7',
 'G8','G9','G10','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','I1',
 'I2','I3','I4','I5','I6','I7','I8','I9','I10','J1','J2','J3','J4','J5',
 'J6','J7','J8','J9','J10','K1','K2','K3','K4','K5','K6','K7','K8','K9',
 'K10','L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','M1','M2','M3',
 'M4','M5','M6','M7','M8','M9','M10','N1','N2','N3','N4','N5','N6','N7',
 'N8','N9','N10','O1','O2','O3','O4','O5','O6','O7','O8','O9','O10','P1',
 'P2','P3','P4','P5','P6','P7','P8','P9','P10']
# Create your views here.

def result(request):

    temp=request.GET.get('userName').replace(' ','')

    finalDict={}
    Compatibility=[]
    for question in ColNames:
        finalDict[question]=PersonalityDetails.objects.filter(userName=temp,question=question).values_list('answer',flat=True)

    df = pd.DataFrame.from_records(finalDict)
    usernames=PersonalityDetails.objects.filter(~Q(userName=temp)).order_by().values_list('userName',flat=True).distinct()
    finalDict = {}
    for user in usernames:
        for question in ColNames:

            finalDict[question] = PersonalityDetails.objects.filter(userName=user, question=question).values_list('answer',flat=True)

        df2 = pd.DataFrame.from_records(finalDict)
        Compatibility.append((user,GetCompatibility(df,df2)))

    return render(request, 'ViewResults.html',{'Compatibility':Compatibility})

def renew_book_librarian(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':

       # Check if the form is valid:
        if True:
            print "**********************"
            UserName=request.POST.get('FullName').replace(' ','')
            AnswerList=[]
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            for each_col in ColNames:
                AnswerList.append(request.POST.get(each_col))

            for (question,answer) in zip(ColNames,AnswerList):

                PeronalityInstance=PersonalityDetails.objects.create(
                     userName=UserName,
                     question=question,
                     answer=answer)
                PeronalityInstance.save()
            return redirect('/result?userName='+UserName)
    return render(request, 'PersonalityQuestions.html')

