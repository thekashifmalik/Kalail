# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from feedbax.models import TestSystem, Feedback
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

@login_required
def index(request):
	systems = request.user.testsystem_set.all()
	return render_to_response('feedbax/index.html', {'systems': systems}, context_instance=RequestContext(request))

@login_required
def setup_feedback_system(request):
	if request.method == 'POST':
		new_name = request.POST['new_feedbax_name']
		new_site = "http://" + request.POST['new_comment_site']
		new_report_email = request.POST['new_feedbax_report_email']
		new_user = request.user
		new_feedbax_site = slugify(new_name)
		
		new_system = TestSystem(name=new_name, site=new_site, feedbax_site=new_feedbax_site, report_email=new_report_email)
		new_system.save()
		new_system.users.add(new_user)

		# Send email
		
		return HttpResponseRedirect(reverse('feedbax.views.index'))
	return render_to_response('feedbax/setup_feedback_system.html', {}, context_instance=RequestContext(request))

@login_required
def show_system_feedback(request, feedbax_site):
	system = get_object_or_404(TestSystem, feedbax_site=feedbax_site)
	all_feedback = system.feedback_set.all().order_by('created_on')
	return render_to_response('feedbax/show_system_feedback.html', {'system': system, 'all_feedback': all_feedback}, context_instance=RequestContext(request))

@login_required
def send_feedback(request, feedbax_site):
	system = get_object_or_404(TestSystem, feedbax_site=feedbax_site)
	if request.method == 'POST':
		new_content = request.POST['new_feedback_content']
		new_user = request.user
		new_system = system

		new_feedback = Feedback(content=new_content, system=new_system, user=new_user)
		new_feedback.save()
		
		# Send email

		return HttpResponseRedirect(reverse('feedbax.views.index'))
	return render_to_response('feedbax/send_feedback.html', {'system': system}, context_instance=RequestContext(request))