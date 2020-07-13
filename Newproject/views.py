from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
	Parameters = {'Name': 'Akhil', 'Occupation': 'Coder'}
	return render(request, 'Home.html', Parameters)

def AboutPage(request):
	return render(request, 'About.html')

def ContactPage(request):
	return render(request, 'Contact.html')

def FormPage(request):
	return render(request, 'ResumeForm.html')

def GeneratedResume(request):
	Name = 'Akhil Goel'
	Designation = 'Electrical Engineering Undergraduate'
	Description = '''I am a 2nd year Electrical Engineering student with a good
					command over programming languages. A programming Enthusiast
					with a sheer will to learn and grow in the field of programming'''
	# Details = ['akhilgoeljan@gmail.com', '0941757493', 'Chandigarh, India', 'linkedin.com/in/akhil-goel-a5a666176', 'github.com/akhilgoel0007']
	Details = []
	Parameters = {
		'Name': Name,
		'Designation': Designation,
		'Description': Description,
		'Details': Details
	}

	return render(request, 'GeneratedResume.html', Parameters)