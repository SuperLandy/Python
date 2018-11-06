from django.contrib.auth import authenticate
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, render_to_response




def index(request):
    if request.session.get('is_login',True):
        return render_to_response('index.html')
    return render_to_response('login.html')




# 处理登录数据
def login(request): 
    if request.method == 'POST':
        if request.session.get('is_login') == True:
            return  render_to_response('login.html')
        else:
            username = request.POST.get('form-tel_phone')
            password = request.POST.get('form-password')
            auth_data = authenticate(username=username,password=password)
            if auth_data is not None and auth_data.is_active:
            
                request.session['username'] = username
                request.session['is_login'] = True
                request.session.set_expiry(3600)
                return render_to_response('login.html')
            else:
                return render_to_response('index.html')
    elif request.method == 'GET':
	    return render(request, 'index.html')



# 处理下载数据

def download(request):
    if request.session.get('is_login') == True:
   
        filename = open(
            '/opt/HelloWord/templates/assets/download/Awakening_of_the_force.rmvb', 'rb')
        response = FileResponse(filename=filename)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="Awakening_of_the_force.rmvb"'
        return response
    else:
	    return render(request, 'index.html')