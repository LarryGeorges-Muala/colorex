from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.utils import timezone
from colorex.models import User
from htmlmin.decorators import minified_response

def init_gamer(request):
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			gamer = User.objects.get(id=request.session['gamer'])
		except KeyError:
			return HttpResponseRedirect(reverse('colorex:index'))
	return gamer

@minified_response
def index(request):		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/index.html', context)
	
	
def level_1(request):
	
	gamer = ''

	if request.method == "POST" and request.POST.get("NEXT"):
		try:
			gamer = create_player(request)
			update_level_1(request)			
			return HttpResponseRedirect(reverse('colorex:level_2'))
		except Exception as error:
			print(error)
			
	if request.method == "POST" and request.POST.get("LEVELS"):
		try:
			gamer = create_player(request)
			update_level_1(request)
			return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)

	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_1.html', context)
	
	
def level_2(request):
	
	gamer = ''

	if request.method == "POST" and request.POST.get("NEXT"):
		try:
			gamer = create_player(request)
			update_level_2(request)
			return HttpResponseRedirect(reverse('colorex:level_3'))
		except Exception as error:
			print(error)
			
	if request.method == "POST" and request.POST.get("LEVELS"):
		try:
			gamer = create_player(request)
			update_level_2(request)
			return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)

	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_2.html', context)
	
	
def level_3(request):
	
	gamer = ''

	if request.method == "POST" and request.POST.get("NEXT"):
		try:
			gamer = create_player(request)
			update_level_3(request)
			return HttpResponseRedirect(reverse('colorex:level_4'))
		except Exception as error:
			print(error)
			
	if request.method == "POST" and request.POST.get("LEVELS"):
		try:
			gamer = create_player(request)
			update_level_3(request)
			return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)
	
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_3.html', context)
	
	
def level_4(request):
	
	gamer = ''
			
	if request.method == "POST" and request.POST.get("NEXT"):
		try:
			gamer = create_player(request)
			update_level_4(request)
			return HttpResponseRedirect(reverse('colorex:level_5'))
		except Exception as error:
			print(error)
			
	if request.method == "POST" and request.POST.get("LEVELS"):
		try:
			gamer = create_player(request)
			update_level_4(request)
			return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)
		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_4.html', context)
	
	
def level_5(request):
	
	gamer = ''

	if request.method == "POST" and request.POST.get("SCORE"):
		try:
			gamer = create_player(request)
			update_level_5(request)
			return HttpResponseRedirect(reverse('colorex:score_board'))
		except Exception as error:
			print(error)

	if request.method == "POST" and request.POST.get("NEW_NAME"):
		try:
			gamer = create_player(request)
			update_player(request)
			update_level_5(request)
			return HttpResponseRedirect(reverse('colorex:score_board'))
		except Exception as error:
			print(error)	

	if request.method == "POST" and request.POST.get("LEVELS"):
		try:
			gamer = create_player(request)
			update_level_5(request)
			return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)

	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_5.html', context)


def level_6(request):
		
	gamer = ''
			
	if request.method == "POST":
		try:
			gamer = create_player(request)
			update_level_6(request)
			if request.POST.get("NEXT"):
				return HttpResponseRedirect(reverse('colorex:level_7'))
			if request.POST.get("LEVELS"):
				return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)
		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_6_pyramid.html', context)


def level_7(request):
		
	gamer = ''
			
	if request.method == "POST":
		try:
			gamer = create_player(request)
			update_level_7(request)
			if request.POST.get("NEXT"):
				return HttpResponseRedirect(reverse('colorex:level_8'))
			if request.POST.get("LEVELS"):
				return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)
		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_7_losange.html', context)


def level_8(request):
		
	gamer = ''
			
	if request.method == "POST":
		try:
			gamer = create_player(request)
			update_level_8(request)
			if request.POST.get("NEXT"):
				return HttpResponseRedirect(reverse('colorex:level_9'))
			if request.POST.get("LEVELS"):
				return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)
		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_8_earth.html', context)


def level_9(request):
		
	gamer = ''
			
	if request.method == "POST":
		try:
			gamer = create_player(request)
			update_level_9(request)
			if request.POST.get("NEXT"):
				return HttpResponseRedirect(reverse('colorex:level_10'))
			if request.POST.get("LEVELS"):
				return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)
		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_9_africa.html', context)


def level_10(request):
		
	gamer = ''

	if request.method == "POST":
		try:
			gamer = create_player(request)
			update_level_10(request)
			if request.POST.get("SCORE"):
				return HttpResponseRedirect(reverse('colorex:score_board'))
			if request.POST.get("NEW_NAME"):
				return HttpResponseRedirect(reverse('colorex:score_board'))
			if request.POST.get("LEVELS"):
				return HttpResponseRedirect(reverse('colorex:levels'))
		except Exception as error:
			print(error)
		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/level_10_guitar.html', context)
	

def score_board(request):
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/score_board.html', context)
	
	
def leader_board(request):
	
	gamer = ''
	
	"""
	##Auto user load 
	dummy = User(
			user_name = 'Lelouch',
			level_1_time = '12',
			level_2_time = '24',
			level_3_time = '48',
			level_4_time = '56',
			level_5_time = '10',
			total_time = '0'
		)
	dummy.save()
	
	dummy.total_time = int(dummy.level_1_time) + int(dummy.level_2_time) + int(dummy.level_3_time) + int(dummy.level_4_time) + int(dummy.level_5_time)
	dummy.save()
	print('loaded')
	
	"""
	
	##Numerizer
	for data in User.objects.all():
		data.total_time_numeric = int(data.total_time)
		data.save()
	print('numerized')
	
	
	all_users = ''
	if User.objects.all():
		all_users = User.objects.all().order_by('-total_time_numeric')
	print(all_users)
		
	context = {'user': init_gamer(request), 'all_users': all_users}
	return render(request, 'colorex/leaderboard.html', context)
	
	
def levels(request):		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/levels.html', context)
	
	
def create_player(request):
	
	gamer = ''
	
	try:
		gamer = User.objects.get(id=request.session['gamer'])		
		print('existing gamer')
	except Exception as error:
		print(error)
		
		##Saving to database
		gamer = User(
			user_name = 'Anonymous',
			level_1_time = '0',
			level_1_unlock = True,
			level_2_time = '0',
			level_3_time = '0',
			level_4_time = '0',
			level_5_time = '0',
		)
		gamer.save()
		print('new gamer IDed')
		
		request.session['gamer'] = gamer.id
	return gamer
	
def update_level_1(request):
	
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])
			
			##Best Performance Checker
			if gamer.level_1_time:
				if int(gamer.level_1_time) != 0 and int(captured_time) > int(gamer.level_1_time):
					captured_time = gamer.level_1_time

			gamer.level_1_time = captured_time
			gamer.level_1_unlock = True
			gamer.total_time = int(gamer.level_1_time) + int(gamer.level_2_time) + int(gamer.level_3_time) + int(gamer.level_4_time) + int(gamer.level_5_time)
			gamer.save()
			print('Level 1 saved')
			
		except Exception as error:
			print(error)
		
	return True
	
def update_level_2(request):
	
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])	
			
			##Best Performance Checker
			if gamer.level_2_time:
				if int(gamer.level_2_time) != 0 and int(captured_time) > int(gamer.level_2_time):
					captured_time = gamer.level_2_time
					
			gamer.level_1_unlock = True
			gamer.level_2_time = captured_time
			gamer.level_2_unlock = True
			gamer.total_time = int(gamer.level_1_time) + int(gamer.level_2_time) + int(gamer.level_3_time) + int(gamer.level_4_time) + int(gamer.level_5_time)
			gamer.save()
			print('Level 2 saved')
			
		except Exception as error:
			print(error)
		
	return True
	
	
def update_level_3(request):
	
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])	
			
			##Best Performance Checker
			if gamer.level_3_time:
				if int(gamer.level_3_time) != 0 and int(captured_time) > int(gamer.level_3_time):
					captured_time = gamer.level_3_time
					
			gamer.level_1_unlock = True
			gamer.level_2_unlock = True
			gamer.level_3_time = captured_time
			gamer.level_3_unlock = True
			gamer.total_time = int(gamer.level_1_time) + int(gamer.level_2_time) + int(gamer.level_3_time) + int(gamer.level_4_time) + int(gamer.level_5_time)
			gamer.save()
			print('Level 3 saved')
			
		except Exception as error:
			print(error)
			
			
def update_level_4(request):
	
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])	
			
			##Best Performance Checker
			if gamer.level_4_time:
				if int(gamer.level_4_time) != 0 and int(captured_time) > int(gamer.level_4_time):
					captured_time = gamer.level_4_time
					
			gamer.level_1_unlock = True
			gamer.level_2_unlock = True
			gamer.level_3_unlock = True
			gamer.level_4_time = captured_time
			gamer.level_4_unlock = True
			gamer.total_time = int(gamer.level_1_time) + int(gamer.level_2_time) + int(gamer.level_3_time) + int(gamer.level_4_time) + int(gamer.level_5_time)
			gamer.save()
			print('Level 4 saved')
			
		except Exception as error:
			print(error)
		
	return True
	
	
def update_level_5(request):
	
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])	
			
			##Best Performance Checker
			if gamer.level_5_time:
				if int(gamer.level_5_time) != 0 and int(captured_time) > int(gamer.level_5_time):
					captured_time = gamer.level_5_time
					
			gamer.level_1_unlock = True
			gamer.level_2_unlock = True
			gamer.level_3_unlock = True
			gamer.level_4_unlock = True
			gamer.level_5_time = captured_time
			gamer.level_5_unlock = True
			gamer.total_time = int(gamer.level_1_time) + int(gamer.level_2_time) + int(gamer.level_3_time) + int(gamer.level_4_time) + int(gamer.level_5_time) 
			gamer.save()
			print('Level 5 saved')
			
		except Exception as error:
			print(error)
		
	return True


def update_level_6(request):
		
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])	
			
			##Best Performance Checker
			if gamer.level_6_time:
				if int(gamer.level_6_time) != 0 and int(captured_time) > int(gamer.level_6_time):
					captured_time = gamer.level_6_time
					
			gamer.level_1_unlock = True
			gamer.level_2_unlock = True
			gamer.level_3_unlock = True
			gamer.level_4_unlock = True
			gamer.level_5_unlock = True
			gamer.level_6_time = captured_time
			gamer.level_6_unlock = True
			gamer.save()
			print('Level 6 saved')
			
		except Exception as error:
			print(error)
		
	return True


def update_level_7(request):
		
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])	
			
			##Best Performance Checker
			if gamer.level_7_time:
				if int(gamer.level_7_time) != 0 and int(captured_time) > int(gamer.level_7_time):
					captured_time = gamer.level_7_time
					
			gamer.level_1_unlock = True
			gamer.level_2_unlock = True
			gamer.level_3_unlock = True
			gamer.level_4_unlock = True
			gamer.level_5_unlock = True
			gamer.level_6_unlock = True
			gamer.level_7_time = captured_time
			gamer.level_7_unlock = True
			gamer.save()
			print('Level 7 saved')
			
		except Exception as error:
			print(error)
		
	return True


def update_level_8(request):
		
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])	
			
			##Best Performance Checker
			if gamer.level_8_time:
				if int(gamer.level_8_time) != 0 and int(captured_time) > int(gamer.level_8_time):
					captured_time = gamer.level_8_time
					
			gamer.level_1_unlock = True
			gamer.level_2_unlock = True
			gamer.level_3_unlock = True
			gamer.level_4_unlock = True
			gamer.level_5_unlock = True
			gamer.level_6_unlock = True
			gamer.level_7_unlock = True
			gamer.level_8_time = captured_time
			gamer.level_8_unlock = True
			gamer.save()
			print('Level 8 saved')
			
		except Exception as error:
			print(error)
		
	return True


def update_level_9(request):
		
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])	
			
			##Best Performance Checker
			if gamer.level_9_time:
				if int(gamer.level_9_time) != 0 and int(captured_time) > int(gamer.level_9_time):
					captured_time = gamer.level_9_time
					
			gamer.level_1_unlock = True
			gamer.level_2_unlock = True
			gamer.level_3_unlock = True
			gamer.level_4_unlock = True
			gamer.level_5_unlock = True
			gamer.level_6_unlock = True
			gamer.level_7_unlock = True
			gamer.level_8_unlock = True
			gamer.level_9_time = captured_time
			gamer.level_9_unlock = True
			gamer.save()
			print('Level 9 saved')
			
		except Exception as error:
			print(error)
		
	return True


def update_level_10(request):
		
	gamer = ''
	if request.session.has_key('gamer'):
		try:
			captured_time = request.POST.get('time', None)
			gamer = User.objects.get(id=request.session['gamer'])	
			
			##Best Performance Checker
			if gamer.level_10_time:
				if int(gamer.level_10_time) != 0 and int(captured_time) > int(gamer.level_10_time):
					captured_time = gamer.level_10_time
					
			gamer.level_1_unlock = True
			gamer.level_2_unlock = True
			gamer.level_3_unlock = True
			gamer.level_4_unlock = True
			gamer.level_5_unlock = True
			gamer.level_6_unlock = True
			gamer.level_7_unlock = True
			gamer.level_8_unlock = True
			gamer.level_9_unlock = True
			gamer.level_10_time = captured_time
			gamer.level_10_unlock = True
			gamer.save()
			print('Level 10 saved')
			
		except Exception as error:
			print(error)
		
	return True
	
	
def update_player(request):
	
	gamer = ''
	captured_name = request.POST.get('firstName', 'Anonymous')
	print(captured_name)
	try:
		gamer = User.objects.get(id=request.session['gamer'])	
		gamer.user_name = captured_name
		gamer.save()
		
		print('updated name')
	except Exception as error:
		print(error)
		
	return True
	

def logout(request):

	if request.session.has_key('gamer'):
		try:
			del request.session['gamer']
		except KeyError:
			pass
					
	return HttpResponseRedirect(reverse('colorex:index'))
	
	
''' Cookies disabled error handler '''
def csrf_failure(request, reason=""):
	context = {}
	return render(request, 'colorex/cookie_error.html', context)