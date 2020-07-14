from django.http import HttpResponse
from django.shortcuts import render

def DisplayConfigure(ParameterName, Parameter):
	Display = {
		'Display': True,
		ParameterName: Parameter
	}

	if not len(Parameter):
		Display['Display'] = False
	
	return Display 

def RefineList(OriginalList):
	"""
		SkillList also has blank strings like ''
		RefineList will remove all the blank strings
	"""

	AllItems = []
	for Item in OriginalList:
		if Item is not '':
			AllItems.append(Item)
	return AllItems

def EducationData(Field, College, StartTime, EndTime, GPA):
	AllFields = []
	for i in range(0, len(Field)):
		FieldData = {
			'Field': Field[i],
			'College': College[i],
			'StartTime': StartTime[i],
			'EndTime': EndTime[i],
			'GPA': GPA[i]
		}
		AllFields.append(FieldData)
	return AllFields

def ProjectData(Heading, StartTime, EndTime, Description):
	AllProjects = []
	for i in range(0, len(Heading)):
		ProjectData = {
			'Heading': Heading[i],
			'StartTime': StartTime[i],
			'EndTime': EndTime[i],
			'Description': Description[i]
		}
		AllProjects.append(ProjectData)

	return AllProjects

def AchievementData(Name, Date, Description):
	AllAchievements = []
	
	for i in range(0, len(Name)):
		AchievementData = {
			'Name': Name[i], 
			'Date': Date[i], 
			'Description': Description[i]
		}

		AllAchievements.append(AchievementData)
	return AllAchievements

def CertificateData(Heading, StartTime, EndTime, Description):
	AllCertificates = []
	for i in range(0, len(Heading)):
		CertificateData = {
			'Heading': Heading[i],
			'StartTime': StartTime[i],
			'EndTime': EndTime[i],
			'Description': Description[i]
		}
		AllCertificates.append(CertificateData)
	return AllCertificates

def HomePage(request):
	Parameters = {'Name': 'Akhil', 'Occupation': 'Coder'}
	return render(request, 'Home.html', Parameters)

def FormPage(request):
	return render(request, 'ResumeForm.html')

def GeneratedResume(request):
	Name = request.GET.get('Name', 'default') # Candidate Name
	Designation = DisplayConfigure('Designation', request.GET.get('Designation', 'default')) # Candidate Designation
	Description = DisplayConfigure('Description', request.GET.get('Description', 'default')) # Candidate Description
	Gmail = DisplayConfigure('Gmail', request.GET.get('Gmail', 'default')) # Candidate Gmail
	PhoneNumber = DisplayConfigure('PhoneNumber', request.GET.get('PhoneNumber', 'default')) # Candidate Phone Number
	Location = DisplayConfigure('Location', request.GET.get('Location', 'default')) # Candidate Location
	LinkedIn = DisplayConfigure('LinkedIn', request.GET.get('LinkedIn', 'default')) # Candidate Linked In
	Github = DisplayConfigure('Github', request.GET.get('Github', 'default')) # Candidate Github

	# Candidate Skill Set
	Skills = DisplayConfigure('Skills', RefineList(request.GET.getlist('Skill', 'default'))) 

	# Candidate Interest Set
	Interest = DisplayConfigure('Interests', RefineList(request.GET.getlist('Interest', 'default'))) 

	# Get All The Education Fields..
	Education = DisplayConfigure('Education', EducationData(RefineList(request.GET.getlist('Field', 'default')), RefineList(request.GET.getlist('College', 'default')), RefineList(request.GET.getlist('StudyStartTime', 'default')), RefineList(request.GET.getlist('StudyEndTime', 'default')), RefineList(request.GET.getlist('GPA', 'default'))))
	
	# Get All The Personal Projects..
	PersonalProjects = DisplayConfigure('PersonalProjects', ProjectData(RefineList(request.GET.getlist('ProjectHeading', 'default')), RefineList(request.GET.getlist('ProjectStartTime', 'default')), RefineList(request.GET.getlist('ProjectEndTime', 'default')), RefineList(request.GET.getlist('ProjectDescription', 'default'))))
	
	# Get All The Achievements..
	Achievements = DisplayConfigure('Achievements', AchievementData(RefineList(request.GET.getlist('AchievementHeading', 'default')), RefineList(request.GET.getlist('AchievementDate', 'default')), RefineList(request.GET.getlist('AchievementDescription', 'default'))))
	
	# Get All The Certifications..
	Certifictions = DisplayConfigure('Certifications', CertificateData(RefineList(request.GET.getlist('CertificateHeading', 'default')), RefineList(request.GET.getlist('CertificateStartTime', 'default')), RefineList(request.GET.getlist('CertificateEndTime', 'default')), RefineList(request.GET.getlist('CertificateDescription', 'default'))))

	Parameters = {
		'Name': Name,
		'Designation': Designation,
		'Description': Description,
		'Gmail': Gmail,
		'PhoneNumber': PhoneNumber,
		'Location': Location,
		'LinkedIn': LinkedIn,
		'Github': Github,
		'Skills': Skills,
		'Interests': Interest,
		'Education': Education,
		'PersonalProjects': PersonalProjects,
		'Achievements': Achievements,
		'Certifications': Certifictions
	}

	# Name = 'Akhil Goel'
	# Designation = 'Electrical Engineering Undergraduate'
	# Description = '''I am a 2nd year Electrical Engineering student with a good command over programming languages. A programming Enthusiast with a sheer will to learn and grow in the field of programming'''
	# Gmail = {'Display': True, 'Value': 'akhilgoeljan@gmail.com'}
	# PhoneNumber = {'Display': True, 'Value': '0941757493'} 
	# Location = {'Display': True, 'Value': 'Chandigarh, India'} 
	# LinkedIn = {'Display': True, 'Value': 'linkedin.com/in/akhil-goel-a5a666176'} 
	# Github = {'Display': True, 'Value': 'github.com/akhilgoel0007'}
	
	# NewParameters = {
	# 	'Name': Name,
	# 	'Designation': Designation,
	# 	'Description': Description,
	# 	'Gmail': Gmail,
	# 	'PhoneNumber': PhoneNumber,
	# 	'Location': Location,
	# 	'LinkedIn': LinkedIn,
	# 	'Github': Github,
	# }

	# return render(request, 'GeneratedResume.html', NewParameters)
	return render(request, 'GeneratedResume.html', Parameters)
