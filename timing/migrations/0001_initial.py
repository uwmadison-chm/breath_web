# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Participant'
        db.create_table('timing_participant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('participant_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=8)),
        ))
        db.send_create_signal('timing', ['Participant'])

        # Adding model 'Run'
        db.create_table('timing_run', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timing.Participant'])),
            ('finished_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('timing', ['Run'])

        # Adding model 'Response'
        db.create_table('timing_response', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('run', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timing.Run'])),
            ('char', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('ms_since_run_start', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('timing', ['Response'])


    def backwards(self, orm):
        
        # Deleting model 'Participant'
        db.delete_table('timing_participant')

        # Deleting model 'Run'
        db.delete_table('timing_run')

        # Deleting model 'Response'
        db.delete_table('timing_response')


    models = {
        'timing.participant': {
            'Meta': {'object_name': 'Participant'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '8'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.response': {
            'Meta': {'object_name': 'Response'},
            'char': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ms_since_run_start': ('django.db.models.fields.IntegerField', [], {}),
            'run': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Run']"}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.run': {
            'Meta': {'object_name': 'Run'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Participant']"}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['timing']
