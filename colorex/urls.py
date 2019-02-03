from django.conf.urls import url 
from . import views

app_name = 'colorex'

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^1/$', views.level_1, name='level_1'),
	url(r'^2/$', views.level_2, name='level_2'),
	url(r'^3/$', views.level_3, name='level_3'),
	url(r'^4/$', views.level_4, name='level_4'),
	url(r'^5/$', views.level_5, name='level_5'),
	url(r'^6/$', views.level_6, name='level_6'),
	url(r'^7/$', views.level_7, name='level_7'),
	url(r'^8/$', views.level_8, name='level_8'),
	url(r'^9/$', views.level_9, name='level_9'),
	url(r'^10/$', views.level_10, name='level_10'),
	url(r'^score/$', views.score_board, name='score_board'),
	url(r'^leaderboard/$', views.leader_board, name='leader_board'),
	url(r'^levels/$', views.levels, name='levels'),
	url(r'^logout/$', views.logout, name='logout'),

	url(r'^tutorial/$', views.level_tutorial, name='level_tutorial'),

	url(r'^handler/levels/$', views.levels_dispatcher, name='levels_dispatcher'),
	url(r'^handler/time/$', views.time_saver, name='time_saver'),
	url(r'^handler/name/$', views.name_saver, name='name_saver'),
	url(r'^handler/mobile/$', views.init_mobile_gamer, name='init_mobile_gamer'),
	
]