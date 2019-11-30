from django.shortcuts import render
from django.http import HttpResponse
from BlgApp.forms import SignupForms,UploadForm
from BlgApp.models import Upload
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):

    return render(request,'BlgApp/home.html')

def viewBlog(request):
    mydict={}
    images=Upload.objects.all().order_by('-upload_date')
    mydict['images']=images
    return render(request,'BlgApp/ViewBlog.html', context=mydict)



def signup(request):
    sform=SignupForms()
    mydict={'sform':sform}
    if request.method=='POST':
        sform=SignupForms(request.POST)
        user=sform.save()
        user.set_password(user.password)
        user.save()
        mydict['msg']="USer Successfully Registered"
    return render(request,'BlgApp/signup.html',context=mydict)


@login_required
def upload(request):
    uform=UploadForm()
    mydict={'uform':uform}
    if request.method=='POST':
        uform=UploadForm(request.POST,request.FILES)
        if uform.is_valid():
            data=uform.save(commit=False)
            data.author=request.user
            data.save()
            mydict['msg']='File uploaded Successfylly...'
    return render(request,"BlgApp/PostBlog.html",context=mydict)


def click(request,id):
    blog = Upload.objects.get(id=id)

    return render(request,'BlgApp/display.html',context={'blog':blog})
