#self created file
#return https response
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def analyze(request):
    txt = request.POST.get('text', 'default')
    print(txt)
    rmPunc = request.POST.get('removepunc', 'off')
    fullCaps = request.POST.get('fullcaps', 'off')
    newLineRm = request.POST.get('newlineremover', 'off')
    res = ""
    if rmPunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in txt:
            if i not in punctuations:
                res = res+i
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': res}
        txt = res
    if fullCaps=="on":
        for char in txt:
            res = res+char.upper()
        params = {'purpose': 'Convert in uppercase', 'analyzed_text': res}
        return render(request, 'analyze.html', params)
    if newLineRm == "on":
        for char in txt:
            if char !="/n":
                res+=char
        params = {'purpose': 'Convert in uppercase', 'analyzed_text': res}
        return render(request, 'analyze.html', params)
    if(rmPunc != "on" and newLineRm!="on"  and fullCaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
