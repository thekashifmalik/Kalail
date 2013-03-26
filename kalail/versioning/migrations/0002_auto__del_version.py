# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Version'
        db.delete_table('versioning_version')


    def backwards(self, orm):
        
        # Adding model 'Version'
        db.create_table('versioning_version', (
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('features', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('versioning', ['Version'])


    models = {
        
    }

    complete_apps = ['versioning']
