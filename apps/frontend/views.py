from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request,'frontend/index.html')

def upload(request):
    context={}
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        print(uploaded_file.name)
        print(str(uploaded_file.size) + " bytes")
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name, uploaded_file)
        context['url']=fs.url(name)
        print(context['url'])
    return render(request,'frontend/upload.html',context)
