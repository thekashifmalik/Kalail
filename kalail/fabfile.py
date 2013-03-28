from fabric.api import *

# Import settings
import kalail.settings as settings

cmd_envs = settings.FAB_DEPLOY_ENVS


def push(environment=None):
	"""Push the app to heroku."""

	if not environment:
		print "No environment declared!"
		return
	# Push to heroku
	if environment in cmd_envs['development']:
		cmd_env = 'heroku'
	elif environment in cmd_envs['production']:
		cmd_env = 'heroku-production'
	else:
		print "Incorrect environment declared!"
		return

	local('git push %s' % cmd_env)


def add_config_vars(environment=None):
	"""Add given config variables as environment variables."""

	if not environment:
		print "No environment declared!"
		return

	if environment in cmd_envs['development']:
		cmd_env = 'kalail-dev'
		config_vars = settings.CONFIG_VARS['DEVELOPMENT']
	elif environment in cmd_envs['production']:
		cmd_env = 'kalail'
		config_vars = settings.CONFIG_VARS['PRODUCTION']
	else:
		print "Incorrect environment declared!"
		return

	config_commands = ['%s="%s"' % (name, var) for name, var in config_vars.items()]
	config_command = ' '.join(config_commands)
	local('heroku config:add %s --app %s' % (config_command, cmd_env))

def syncdb(environment=None):
	"""Run syncdb on the server."""

	if not environment:
		print "No environment declared!"
		return

	if environment in cmd_envs['development']:
		cmd_env = 'kalail-dev'
	elif environment in cmd_envs['production']:
		cmd_env = 'kalail'
	else:
		print "Incorrect environment declared!"
		return

	local('heroku run python kalail/manage.py syncdb --app %s' % cmd_env)

def migrate(environment=None):
	"""Migrate the database on the server."""
	if not environment:
		print "No environment declared!"
		return

	if environment in cmd_envs['development']:
		cmd_env = 'kalail-dev'
	elif environment in cmd_envs['production']:
		cmd_env = 'kalail'
	else:
		print "Incorrect environment declared!"
		return

	local('heroku run python kalail/manage.py migrate --app %s' % cmd_env)

def collectstatic(environment=None):
	"""Push all static assets to S3."""
	if not environment:
		print "No environment declared!"
		return

	if environment in cmd_envs['development']:
		cmd_env = 'kalail-dev'
	elif environment in cmd_envs['production']:
		cmd_env = 'kalail'
	else:
		print "Incorrect environment declared!"
		return

	local('heroku run python kalail/manage.py collectstatic --app %s' % cmd_env)


def deploy(environment=None):
	"""Fully deploy the app to heroku, running all the steps."""

	if not environment:
		print "No environment declared!"
		return

	if environment in cmd_envs['development']:
		env_name = 'development'
	elif environment in cmd_envs['production']:
		env_name = 'production'
	else:
		print "Incorrect environment declared!"
		return

	push(env_name)
	add_config_vars(env_name)
	syncdb(env_name)
	migrate(env_name)
	collectstatic(env_name)

def watch_coffee():
	"""Watch and compile coffeescript files to javascript""" 

	coffee_folder = 'static/coffee'
	js_folder = 'static/js'
	print('watching %s for changes' % coffee_folder)
	local('coffee -o %s -wc %s' % (js_folder, coffee_folder))

def watch_less():
	"""Watch and compile less files to CSS"""

	less_folder = 'static/css'
	print('watching %s for changes' % less_folder)
	local('watch-less -d %s -e .css' % less_folder)