# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Run.started_at'
        db.add_column('timing_run', 'started_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Run.started_at'
        db.delete_column('timing_run', 'started_at')


    models = {
        'timing.participant': {
            'Meta': {'object_name': 'Participant'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant_number': ('django.db.models.fields.CharField', [], {'default': "'343483'", 'unique': 'True', 'max_length': '8'}),
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
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['timing']
