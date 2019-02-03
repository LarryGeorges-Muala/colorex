import traceback
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest, JsonResponse
from django.urls import reverse
from django.utils import timezone

from colorex.models import User
from htmlmin.decorators import minified_response


def error_catcher(error):
	print(error)
	print(traceback.format_exc())


def init_gamer(request):
	gamer = ''
	try:
		if request.session.has_key('gamer'):
			gamer_check = User.objects.filter(id=request.session['gamer'])
			if gamer_check:
				gamer = gamer_check.order_by('id').first()
				print('Existing Player')

		if not gamer:
			gamer = User.objects.create(level_1_unlock=True)
			request.session['gamer'] = gamer.id
			print('New Player')

	except Exception as error:
		error_catcher(error)

	return gamer


def init_mobile_gamer(request):
	''' Invalid Pre-emptive Response '''
	data = {'status': False}

	''' Handler '''
	try:
		gamer = None
		user_id = request.GET.get('user_id', '')

		if user_id:
			gamer_check = User.objects.filter(id=int(user_id))
			if gamer_check:
				gamer = gamer_check.order_by('id').first()
				print('Existing Player')
				data = {'status': True, 'user_id': gamer.id, 'has_a_user_name': gamer.has_a_user_name}

		if not gamer:
			gamer = User.objects.create(level_1_unlock=True)
			print('New Player')
			data = {'status': True, 'user_id': gamer.id, 'has_a_user_name': gamer.has_a_user_name}

	except Exception as error:
		error_catcher(error)

	return JsonResponse(data)


@minified_response
def index(request):		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/index.html', context)
	

def levels_dispatcher(request):
	try:
		''' Init Gamer '''
		gamer = init_gamer(request)

		if not gamer.level_2_unlock:
			return HttpResponseRedirect(reverse('colorex:level_1'))
		if not gamer.level_3_unlock:
			return HttpResponseRedirect(reverse('colorex:level_2'))
		if not gamer.level_4_unlock:
			return HttpResponseRedirect(reverse('colorex:level_3'))
		if not gamer.level_5_unlock:
			return HttpResponseRedirect(reverse('colorex:level_4'))
		if not gamer.level_6_unlock:
			return HttpResponseRedirect(reverse('colorex:level_5'))
		if not gamer.level_7_unlock:
			return HttpResponseRedirect(reverse('colorex:level_6'))
		if not gamer.level_8_unlock:
			return HttpResponseRedirect(reverse('colorex:level_7'))
		if not gamer.level_9_unlock:
			return HttpResponseRedirect(reverse('colorex:level_8'))
		if not gamer.level_10_unlock:
			return HttpResponseRedirect(reverse('colorex:level_9'))
		return HttpResponseRedirect(reverse('colorex:levels'))

	except Exception as error:
		error_catcher(error)

	return HttpResponseRedirect(reverse('colorex:index'))


def time_saver(request):
	''' Invalid Pre-emptive Response '''
	data = {'status': False}

	''' Handler '''
	try:
		''' Initial Data '''
		user_id = request.GET.get('user_id', '')
		user_time = request.GET.get('user_time', '')
		level_id = request.GET.get('level', '')

		''' Handler '''
		if user_id and user_time and level_id:
			''' Find User '''
			gamer_check = User.objects.filter(id=int(user_id))
			if gamer_check:
				gamer = gamer_check.order_by('id').first()

				''' Update Levels '''
				gamer.update_level_time(int(level_id), user_time)

				''' Update Total Time '''
				gamer.update_total_time()

				data = {'status': True}

	except Exception as error:
		error_catcher(error)

	return JsonResponse(data)


def name_saver(request):
	''' Invalid Pre-emptive Response '''
	data = {'status': False}

	''' Handler '''
	try:
		''' Initial Data '''
		user_id = request.GET.get('user_id', '')
		user_name = request.GET.get('user_name', '')

		''' Handler '''
		if user_id and user_name:
			''' Find User '''
			gamer_check = User.objects.filter(id=int(user_id))
			if gamer_check:
				gamer = gamer_check.order_by('id').first()

				''' Update Name '''
				gamer.user_name = user_name
				gamer.has_a_user_name = True
				gamer.save()

				data = {'status': True}

	except Exception as error:
		error_catcher(error)

	return JsonResponse(data)
	

def level_tutorial(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': 'X'
	}
	return render(request, 'colorex/tutorial.html', context)


def level_1(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '1'
	}
	return render(request, 'colorex/level_1.html', context)
	
	
def level_2(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '2'
	}
	return render(request, 'colorex/level_2.html', context)
	
	
def level_3(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '3'
	}
	return render(request, 'colorex/level_3.html', context)
	
	
def level_4(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '4'
	}
	return render(request, 'colorex/level_4.html', context)
	
	
def level_5(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '5'
	}
	return render(request, 'colorex/level_5.html', context)


def level_6(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '6'
	}
	return render(request, 'colorex/level_6_pyramid.html', context)


def level_7(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '7'
	}
	return render(request, 'colorex/level_7_losange.html', context)


def level_8(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '8'
	}
	return render(request, 'colorex/level_8_earth.html', context)


def level_9(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '9'
	}
	return render(request, 'colorex/level_9_africa.html', context)


def level_10(request):
	context = {
		'user': init_gamer(request),
		'level_index_name': '10'
	}
	return render(request, 'colorex/level_10_guitar.html', context)
	

def score_board(request):
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/score_board.html', context)
	
	
def leader_board(request):
	
	gamer = ''
	
	##Numerizer
	for data in User.objects.all():
		data.total_time_numeric = int(data.total_time)
		data.save()
	print('numerized')
	
	
	all_users = ''
	if User.objects.all():
		# all_users = User.objects.all().order_by('-total_time_numeric')
		all_users = User.objects.all().exclude(total_time_numeric=0, level_6_unlock=False)
		all_users = all_users.order_by('-total_time_numeric')
	print(all_users)
		
	context = {'user': init_gamer(request), 'all_users': all_users}
	return render(request, 'colorex/leaderboard.html', context)
	
	
def levels(request):		
	context = {'user': init_gamer(request)}
	return render(request, 'colorex/levels.html', context)
	

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
