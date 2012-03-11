# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Post'
        db.create_table('blog_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Post'])

        # Adding model 'Comment'
        db.create_table('blog_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('blog', ['Comment'])


    def backwards(self, orm):
        
        # Deleting model 'Post'
        db.delete_table('blog_post')

        # Deleting model 'Comment'
        db.delete_table('blog_comment')


    models = {
        'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Post']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['blog']
