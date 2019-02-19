from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')
def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    listlength = len(word_list)

    worddict={}


    for word in word_list:
         if word in worddict:
            worddict[word]+=1
         else:
            worddict[word]= 1    
            sorted_list = sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, 'count.html',{'fulltextarea':data,'word_list':listlength,'worddict':sorted_list})
def about(request):
    return render(request,'about.html')
