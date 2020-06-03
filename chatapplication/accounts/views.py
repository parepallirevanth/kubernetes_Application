from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from accounts.tokens import Token
from chatapp.settings import EMAIL_HOST_USER
from django.contrib.auth import  authenticate

def index(request):
    """
    Desc:Functions used call the homepage
    params: Http request
    return: redirects to homepage
    """
    return redirect('/')

# Create your views here.
def register(request):
    """
    Desc: Function is to register the user information and store in the database
    input: HTTPRequest
    return: 
    """
    #checks the method is post or not if yes fetches the data
    if request.method=='POST':
        first_name=request.POST['First_Name']
        last_name=request.POST['Last_Name']
        username=request.POST['User_Name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
      
        #Checks whether the two passwords are the same which have entered
        if password1==password2:
            #check the username is existed in database using the filter object by django
            if User.objects.filter(username=username).exists():
                messages.info(request,'User-Name taken')
                return redirect('register')
            #checks the email is existed in database using the filter object by django
            elif User.objects.filter(email=email).exists():
                
                messages.info(request,'Email taken')
                return redirect('register')

            #else create user in the database
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.is_active=False
                user.save()
                #using the jwt token
                payload={'id': username}
                key="encode"
                algorithm='HS256'
                current_site =get_current_site(request)
                mail_subject="Activate your account"
                #loading a template and rendering it with a context
                message = render_to_string('chat/acc_active.html', {
                'user': username,
                'domain': current_site.domain,
                 # Generating the token by sending payload, key, alogorithm
                'token': Token.encode(payload,key,algorithm),
                })
                to_email = User.objects.get(email=email)
                #Sending a single message to the recipient list
                send_mail(mail_subject, message, EMAIL_HOST_USER ,[to_email.email])
                #print('User created')
                
                #redirects to the homepage
                messages.info(request,'verify the mail')
                return redirect('/')

        #gives a message as password not matching and 
        #returns an HttpResponse object with that rendered text 
        else: 
            messages.info(request,'Password Not Matching')
            return render(request,"chat/register.html")

        

    #Combines a given template with a given context dictionary
    #and returns an HttpResponse object with that rendered text     
    else:
        
        return render(request,'chat/register.html')


def activate(request, token):
    """
    Desc: Function to activate the token which was encoded
    
    params:HTTPrequest,token
    
    """     
    key="encode"
    algorithm='HS256'
    #calling try and  except 
    try:
        print("------->")
        #calling the decode function from Token class
        x=Token.decode(token,key,algorithm)
        #gets the username object from the decoded token
        user = User.objects.get(username=x['id'])
        
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None

    #Checks whether the user is Not none and redirects to login page
    if user is not None :
        user.is_active = True
        user.save()
        messages.info(request,'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')

    #returns the response link activated
    else:
        return HttpResponse('Activation link is invalid!')

def login(request):
     """
     Desc: Function to request the login form
     params:Request(gets the HTTPrequest)
     returns: login form
     """

    # Checks the request method is POST
     if request.method=='POST':
        username=request.POST['User_Name']
        password=request.POST['password']

        #Django authentication provides both authentication 
        #and authorization together
        user=auth.authenticate(username=username,password=password)
        
        #checks whether is user is None none
        if user is not None:
            #It takes an HttpRequest object and a User object
            auth.login(request,user)
            return redirect('/')
        #else, it returns Invalid data and returns to login page.    
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

     #Combines a given template with a given context dictionary
     #and returns an HttpResponse object with that rendered text
     else:
         return render(request,'chat/login.html')

def logout(request):
    """
    desc:The functions is to logout and comes to homepage
     
    params:HTTPrequest
    return: redirects to the homepage 
    """
    auth.logout(request)
    return redirect('/')