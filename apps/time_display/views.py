from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.timezone import localtime, now
localtime(now()).date()
# from datetime import datetime


def index(request):
	# time = datetime.now()
	context = {
		# 'date': time.strftime('%b %d, %Y'),
		'time': strftime('%Y-%m-%d %H:%M %p', gmtime())
	}
	return render(request, 'time_display/index.html', context)
	