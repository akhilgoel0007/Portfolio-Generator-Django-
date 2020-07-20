from django.http import HttpResponse
from django.shortcuts import render

def DisplayConfigure(ParameterName, Parameter):
	Display = {
		'Display': True,
		ParameterName: Parameter
	}

	if not len(Parameter):
		Display['Display'] = False
	print(f"{ParameterName}: {Display}")
	
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
	return render(request, 'Home.html')

def FormPage(request):
	Parameters = {
		'EducationFieldCount': 1
	}
	# Parameters = 1 

	return render(request, 'ResumeForm.html', Parameters)

def GeneratedResume(request):
	Name = request.POST.get('Name') # Candidate Name
	Designation = DisplayConfigure('Designation', request.POST.get('Designation', 'default')) # Candidate Designation
	Description = DisplayConfigure('Description', request.POST.get('Description', 'default')) # Candidate Description
	Gmail = DisplayConfigure('Gmail', request.POST.get('Gmail', 'default')) # Candidate Gmail
	PhoneNumber = DisplayConfigure('PhoneNumber', request.POST.get('PhoneNumber', 'default')) # Candidate Phone Number
	Location = DisplayConfigure('Location', request.POST.get('Location', 'default')) # Candidate Location
	LinkedIn = DisplayConfigure('LinkedIn', request.POST.get('LinkedIn', 'default')) # Candidate Linked In
	Github = DisplayConfigure('Github', request.POST.get('Github', 'default')) # Candidate Github

	# Candidate Skill Set
	Skills = DisplayConfigure('Skills', RefineList(request.POST.getlist('Skill', 'default'))) 

	# Candidate Interest Set
	Interest = DisplayConfigure('Interest', RefineList(request.POST.getlist('Interest', 'default'))) 

	# Get All The Education Fields..
	Education = DisplayConfigure('Education', EducationData(RefineList(request.POST.getlist('Field', 'default')), RefineList(request.POST.getlist('College', 'default')), RefineList(request.POST.getlist('StudyStartTime', 'default')), RefineList(request.POST.getlist('StudyEndTime', 'default')), RefineList(request.POST.getlist('GPA', 'default'))))

	# Get All The Personal Projects..
	PersonalProjects = DisplayConfigure('PersonalProjects', ProjectData(RefineList(request.POST.getlist('ProjectHeading', 'default')), RefineList(request.POST.getlist('ProjectStartTime', 'default')), RefineList(request.POST.getlist('ProjectEndTime', 'default')), RefineList(request.POST.getlist('ProjectDescription', 'default'))))
	
	# Get All The Achievements..
	Achievements = DisplayConfigure('Achievements', AchievementData(RefineList(request.POST.getlist('AchievementHeading', 'default')), RefineList(request.POST.getlist('AchievementDate', 'default')), RefineList(request.POST.getlist('AchievementDescription', 'default'))))
	
	# Get All The Certifications..
	Certifications = DisplayConfigure('Certifications', CertificateData(RefineList(request.POST.getlist('CertificateHeading', 'default')), RefineList(request.POST.getlist('CertificateStartTime', 'default')), RefineList(request.POST.getlist('CertificateEndTime', 'default')), RefineList(request.POST.getlist('CertificateDescription', 'default'))))

	Parameters = {
		'Name': Name,
		'Designation': Designation,
		'Description': Description,
		'Gmail': Gmail,
		'PhoneNumber': PhoneNumber,
		'Location': Location,
		'LinkedIn': LinkedIn,
		'Github': Github,
		'Education': Education,
		'PersonalProjects': PersonalProjects,
		'Skills': Skills,
		'Achievements': Achievements,
		'Certifications': Certifications,
		'Interest': Interest
	}

	return render(request, 'GeneratedResume.html', Parameters)