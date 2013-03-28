# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from notes.models import Notepad

@login_required
def index(request):
	try:
		notepad = request.user.notepad
	except Notepad.DoesNotExist:
		notepad = Notepad(body="", user=request.user)
		notepad.save()

	if request.method == 'GET':
		return render_to_response('notes/index.html',
			{
				"notepad" : notepad
			},
			context_instance=RequestContext(request)
		)

	if request.is_ajax() and request.method == 'POST':
		notepad.body = request.POST['notepad_text']
		notepad.save()
		return HttpResponse("OK")

