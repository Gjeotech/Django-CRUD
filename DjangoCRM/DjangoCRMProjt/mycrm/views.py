from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.forms import UserCreationForm #added to make suer we can add more users
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from .forms import addrecord


# Create your views here.

def home(request):
    #fetching all the ojects in the record table
    records = Record.objects.all()

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully login!')
            return redirect('home')
        else:
            messages.error(request, 'Sorry ! we could not find your account or credentials are not valid')
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})

    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    messages.warning(request, 'You have been logout successfully')
    return redirect('home')


#SIGNUP FUN
def Register_user(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('home')  # Redirect to a success page or login page
        else:
            print(form.errors)
            messages.error(request, 'Registration failed. Please try again.')
            # Render the form with error messages
            #return render(request, 'Register.html', {'form': form})
            return redirect('Register')
    else:
        form = SignUpForm()
        return render(request, 'Register.html', {'form': form})

    return render(request, 'Register.html')

#to view a particular customer records

def customer_record(request,pk):
    if request.method == 'POST':
        form = addrecord(request.POST)
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':customer_record})

    else:
        messages.success(request, 'Data not found, or you have not login')
        return redirect('home')



#DELETE FUNCTION

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Data has been deleted successfully!')
        return redirect('home')
    else:
        messages.success(request, 'You have not login yet!')
        return redirect('home')

#ADD RECORD FUNT

def add_record(request):
    if request.user.is_authenticated:
        form = addrecord(request.POST, request.FILES)
        if request.method=='POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added successfully!')
                return redirect('home')
    else:
        messages.success(request, 'You have to login first, you have not login yet!')
        return redirect('home')
    return render(request,'addrecord.html',{'form':form})



#UPDATE FUNCT
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = addrecord(request.POST or None, request.FILES or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated successfully!')
            return redirect('home')
        return render(request, 'update.html', {'form': form})
    else:
        messages.success(request, 'You have not login yet!')
        return redirect('home')