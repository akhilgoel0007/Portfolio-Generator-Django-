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
	GotName = request.GET.get('Name', 'default') # Candidate Name
	GotDesignation = DisplayConfigure('Designation', request.GET.get('Designation', 'default')) # Candidate Designation
	print(f"Designation:{GotDesignation}")
	GotDescription = DisplayConfigure('Description', request.GET.get('Description', 'default')) # Candidate Description
	GotGmail = DisplayConfigure('Gmail', request.GET.get('Gmail', 'default')) # Candidate Gmail
	GotPhoneNumber = DisplayConfigure('PhoneNumber', request.GET.get('PhoneNumber', 'default')) # Candidate Phone Number
	GotLocation = DisplayConfigure('Location', request.GET.get('Location', 'default')) # Candidate Location
	GotLinkedIn = DisplayConfigure('LinkedIn', request.GET.get('LinkedIn', 'default')) # Candidate Linked In
	GotGithub = DisplayConfigure('Github', request.GET.get('Github', 'default')) # Candidate Github

	# Candidate Skill Set
	GotSkills = DisplayConfigure('Skills', RefineList(request.GET.getlist('Skill', 'default'))) 
	# print(f"Skills: {GotSkills}")
	# Candidate Interest Set
	GotInterest = DisplayConfigure('Interests', RefineList(request.GET.getlist('Interest', 'default'))) 

	# Get All The Education Fields..
	GotEducation = DisplayConfigure('Education', EducationData(RefineList(request.GET.getlist('Field', 'default')), RefineList(request.GET.getlist('College', 'default')), RefineList(request.GET.getlist('StudyStartTime', 'default')), RefineList(request.GET.getlist('StudyEndTime', 'default')), RefineList(request.GET.getlist('GPA', 'default'))))
	# print(f"Education: {GotEducation}")
	# Get All The Personal Projects..
	GotPersonalProjects = DisplayConfigure('PersonalProjects', ProjectData(RefineList(request.GET.getlist('ProjectHeading', 'default')), RefineList(request.GET.getlist('ProjectStartTime', 'default')), RefineList(request.GET.getlist('ProjectEndTime', 'default')), RefineList(request.GET.getlist('ProjectDescription', 'default'))))
	
	# Get All The Achievements..
	GotAchievements = DisplayConfigure('Achievements', AchievementData(RefineList(request.GET.getlist('AchievementHeading', 'default')), RefineList(request.GET.getlist('AchievementDate', 'default')), RefineList(request.GET.getlist('AchievementDescription', 'default'))))
	
	# Get All The Certifications..
	GotCertifictions = DisplayConfigure('Certifications', CertificateData(RefineList(request.GET.getlist('CertificateHeading', 'default')), RefineList(request.GET.getlist('CertificateStartTime', 'default')), RefineList(request.GET.getlist('CertificateEndTime', 'default')), RefineList(request.GET.getlist('CertificateDescription', 'default'))))

	GetParameters = {
		'Name': GotName,
		'Designation': GotDesignation,
		'Description': GotDescription,
		'Gmail': GotGmail,
		'PhoneNumber': GotPhoneNumber,
		'Location': GotLocation,
		'LinkedIn': GotLinkedIn,
		'Github': GotGithub,
		'Skills': GotSkills,
		'Interests': GotInterest,
		'Education': GotEducation,
		'PersonalProjects': GotPersonalProjects,
		'Achievements': GotAchievements,
		'Certifications': GotCertifictions
	}

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