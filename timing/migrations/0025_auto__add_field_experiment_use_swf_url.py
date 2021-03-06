# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Experiment.use_swf_url'
        db.add_column('timing_experiment', 'use_swf_url', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Experiment.use_swf_url'
        db.delete_column('timing_experiment', 'use_swf_url')


    models = {
        'timing.countryofresidence': {
            'Meta': {'ordering': "['position']", 'object_name': 'CountryOfResidence'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.educationlevel': {
            'Meta': {'ordering': "['position']", 'object_name': 'EducationLevel'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.ethnicity': {
            'Meta': {'ordering': "['position']", 'object_name': 'Ethnicity'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.experiment': {
            'Meta': {'object_name': 'Experiment'},
            'breath_time_key': ('django.db.models.fields.CharField', [], {'default': "'J'", 'max_length': '1'}),
            'chime_on_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cycle_length': ('django.db.models.fields.IntegerField', [], {'default': '9'}),
            'data_last_added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'end_cycle_key': ('django.db.models.fields.CharField', [], {'default': "'K'", 'max_length': '1'}),
            'guide_sound_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_exported_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'practice_cycles': ('django.db.models.fields.FloatField', [], {'default': '1.5'}),
            'run_instructions': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'run_length_seconds': ('django.db.models.fields.IntegerField', [], {'default': '900'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'survey_url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url_slug': ('django.db.models.fields.SlugField', [], {'default': "'mhzkv'", 'unique': 'True', 'max_length': '10', 'db_index': 'True'}),
            'use_swf_url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'timing.gender': {
            'Meta': {'ordering': "['position']", 'object_name': 'Gender'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.handedness': {
            'Meta': {'ordering': "['position']", 'object_name': 'Handedness'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.occupation': {
            'Meta': {'ordering': "['position']", 'object_name': 'Occupation'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.participant': {
            'Meta': {'object_name': 'Participant'},
            'birth_month': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'consent_given': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'country_of_residence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.CountryOfResidence']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'education_level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.EducationLevel']", 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'email_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ethnicity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Ethnicity']", 'null': 'True'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Gender']", 'null': 'True'}),
            'handedness': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Handedness']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Occupation']", 'null': 'True'}),
            'participant_number': ('django.db.models.fields.CharField', [], {'default': "'366258'", 'unique': 'True', 'max_length': '8'}),
            'political_identity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.PoliticalIdentity']", 'null': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Race']", 'null': 'True'}),
            'religious_affiliation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.ReligiousAffiliation']", 'null': 'True'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'spirituality': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Spirituality']", 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.politicalidentity': {
            'Meta': {'ordering': "['position']", 'object_name': 'PoliticalIdentity'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.race': {
            'Meta': {'ordering': "['position']", 'object_name': 'Race'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.religiousaffiliation': {
            'Meta': {'ordering': "['position']", 'object_name': 'ReligiousAffiliation'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.response': {
            'Meta': {'unique_together': "(('run', 'press_num'),)", 'object_name': 'Response'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'duration_ms': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'ms_since_run_start': ('django.db.models.fields.IntegerField', [], {}),
            'played_error_chime': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'press_num': ('django.db.models.fields.IntegerField', [], {}),
            'run': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Run']"}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'timezone_offset_min': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.run': {
            'Meta': {'object_name': 'Run'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'experiment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Experiment']"}),
            'finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Participant']"}),
            'run_num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'timing.spirituality': {
            'Meta': {'ordering': "['position']", 'object_name': 'Spirituality'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.viewing': {
            'Meta': {'object_name': 'Viewing'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timing.Participant']", 'null': 'True', 'blank': 'True'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'view_key': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['timing']
