# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Feedback'
        db.delete_table('feedbax_feedback')

        # Deleting model 'TestSystem'
        db.delete_table('feedbax_testsystem')

        # Removing M2M table for field users on 'TestSystem'
        db.delete_table('feedbax_testsystem_users')


    def backwards(self, orm):
        
        # Adding model 'Feedback'
        db.create_table('feedbax_feedback', (
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedbax.TestSystem'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('feedbax', ['Feedback'])

        # Adding model 'TestSystem'
        db.create_table('feedbax_testsystem', (
            ('feedbax_site', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('report_email', self.gf('django.db.models.fields.EmailField')(max_length=128)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=128)),
        ))
        db.send_create_signal('feedbax', ['TestSystem'])

        # Adding M2M table for field users on 'TestSystem'
        db.create_table('feedbax_testsystem_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('testsystem', models.ForeignKey(orm['feedbax.testsystem'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('feedbax_testsystem_users', ['testsystem_id', 'user_id'])


    models = {
        
    }

    complete_apps = ['feedbax']
