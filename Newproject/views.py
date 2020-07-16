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
	return render(request, 'Home.html', Parameters)

def FormPage(request):
	return render(request, 'ResumeForm.html')

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
		'Interests': Interest
	}
	
	# Name = 'Akhil Goel'
	# Designation = {'Display': True, 'Designation': 'Electrical Engineering Undergraduate'}
	# Description = {'Display': True, 'Description': 'I am a 2nd year Electrical Engineering student with a good command over programming languages. A programming Enthusiast with a sheer will to learn and grow in the field of programming'}
	# Gmail = {'Display': True, 'Gmail': 'akhilgoeljan@gmail.com'}
	# PhoneNumber = {'Display': True, 'PhoneNumber': '0941757493'} 
	# Location = {'Display': True, 'Location': 'Chandigarh, India'} 
	# LinkedIn = {'Display': True, 'LinkedIn': 'linkedin.com/in/akhil-goel-a5a666176'} 
	# Github = {'Display': True, 'Github': 'github.com/akhilgoel0007'}
	# Education = [
	# 	{
	# 		'Field': 'Bachelor of Technology (B.Tech)',
	# 		'College': 'Punjab Engineering College, Chandigarh',
	# 		'StartTime': '08/2018',
	# 		'EndTime': 'Present',
	# 		'GPA': '8.46/10.0'
	# 	},
	# 	{
	# 		'Field': 'Class XII',
	# 		'College': 'D.C. Montessori Smart School, Chandigarh',
	# 		'StartTime': '03/2016',
	# 		'EndTime': '03/2018',
	# 		'GPA': '92%'
	# 	},
	# ]

	# PersonalProjects = [
	# 	{
	# 		'Heading': 'Chess Game Simulator',
	# 		'StartTime': '06/2019',
	# 		'EndTime': '09/2019',
	# 		'Description': 'The Application is made using python only (GUI is made using tkinter library). Application can be used to visulaize any chess game which is stored in form of sentences. (Source code on my github account)'
	# 	},
	# 	{
	# 		'Heading': 'HeadBeats - Desktop Music Application',
	# 		'StartTime': '01/2020',
	# 		'EndTime': '04/2020',
	# 		'Description': 'It is a desktop music application with a frontend made in vue.js, electron.js, HTML, HTML Canvas, CSS and javascript. The Data is Stored in a JSON file which is edited and read using fs module of Node.js. (Source code on my github account)'
	# 	}
	# ]

	# Skills = ['C++', 'Ruby', 'Python', 'Data Structures','Algorithms', 'HTML5', 'CSS', 'Javascript', 'Node.js', 'Vue.js', 'Electron.js', 'Web scrapping', 'Git']

	# Achievements = [
	# 	{
	# 		'Name': 'JEE Mains 2018', 
	# 		'Date': '06/2018', 
	# 		'Description': 'Secured a rank of 32,949 in JEE Mains 2018' 
	# 	},
	# 	{
	# 		'Name': 'Talent Hunt by Career Launcher', 
	# 		'Date': '10/2018', 
	# 		'Description': 'Secured 2 position in a 3 stage competition organised by career launcher company' 
	# 	}
	# ]

	# Certifications = [
	# 	{
	# 		'Heading': 'Algorithmic Toolbox course',
	# 		'StartTime': '12/2019',
	# 		'EndTime': '01/2020',
	# 		'Description': 'Course on Mathematical aspect of algorithms and their implementation'
	# 	},
	# 	{
	# 		'Heading': 'Data Structures course',
	# 		'StartTime': '02/2020',
	# 		'EndTime': '03/2020',
	# 		'Description': 'Course on basic data structures and their implementation'
	# 	},
	# 	{
	# 		'Heading': 'Algorithms on Graphs',
	# 		'StartTime': '03/2020',
	# 		'EndTime': '04/2020',
	# 		'Description': 'Course on graph algorithms and their implementation'
	# 	},
	# 	{
	# 		'Heading': 'Algorithms on Strings',
	# 		'StartTime': '03/2020',
	# 		'EndTime': '04/2020',
	# 		'Description': 'Course on String algorithms and their implementation'
	# 	}
	# ]

	# Interest = ['Chess', 'Travelling', 'Competitive', 'Programming', 'Automating Tasks']
	# PersonalProjects = {'Display': True, 'PersonalProjects': PersonalProjects}
	# Skills = {'Display': True, 'Skills': Skills}
	# Achievements = {'Display': True, 'Achievements': Achievements}
	# Education = {'Display': True, 'Education': Education}
	# Interest = {'Display': True, 'Interest': Interest}
	# Certifications = {'Display': True, 'Certifications': Certifications}

	# NewParameters = {
	# 	'Name': Name,
	# 	'Designation': Designation,
	# 	'Description': Description,
	# 	'Gmail': Gmail,
	# 	'PhoneNumber': PhoneNumber,
	# 	'Location': Location,
	# 	'LinkedIn': LinkedIn,
	# 	'Github': Github,
	# 	'Education': Education,
	# 	'PersonalProjects': PersonalProjects,
	# 	'Skills': Skills,
	# 	'Achievements': Achievements,
	# 	'Certifications': Certifications,
	# 	'Interest': Interest
	# }

	return render(request, 'GeneratedResume.html', Parameters)