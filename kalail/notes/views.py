# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from notes.models import Notepad
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

@login_required
def index(request):
	try:
		notepad = request.user.notepad

	except ObjectDoesNotExist:
		notepad = Notepad(body = "", user = request.user)
		notepad.save()

	if request.method == 'POST':
		notepad.body = request.POST['notepad_text']
		notepad.save()
	
	return render_to_response('notes/index.html', {"notepad" : notepad }, context_instance=RequestContext(request))
