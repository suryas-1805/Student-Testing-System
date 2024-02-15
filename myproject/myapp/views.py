from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Student_Details
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Details Registered...!!!')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        global student
        student = Student_Details.objects.filter(name=name, password=password).first()
        if student:
            messages.success(request, 'Login Successfully...!!!')
            return render(request, "profile.html", {'detail': student})
        else:
            messages.error(request, 'Invalid username or password...!!!')
    return render(request, "login.html")

def test(request,student_id):
    test_complete=Student_Details.objects.get(id=student_id)
    test_complete.testing=True
    test_complete.save()
    return render(request,"test.html",{'detail':test_complete})

correct_answers = {
    'q1': 'd', 'q2':'a','q3':'c','q4':'c','q5':'d','q6':'c','q7':'c','q8':'b','q9':'b','q10':'b',
    'q11':'c','q12':'a','q13':'d','q14':'a','q15':'c','q16':'c','q17':'d','q18':'b','q19':'c','q20':'d' # Question 1's correct answer
    # Add more question IDs and correct answers as needed
}

def result(request,student_id):
    student_detail = Student_Details.objects.get(id=student_id)
    if request.method == 'POST':
        score = 0
        for question_id, correct_answer in correct_answers.items():
            user_answer = request.POST.get(question_id)
            if user_answer == correct_answer:
                score += 1
        student_detail.score=score
        student_detail.save()
        messages.success(request, 'Test Successfully Completed...!!!')
    return render(request,"result.html",{'detail':student_detail})

def marks(request):
    student_data=Student_Details.objects.filter(testing=True)
    return render(request,"marks.html",{'data':student_data})
