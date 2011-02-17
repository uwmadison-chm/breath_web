# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Handedness'
        db.create_table('timing_handedness', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['Handedness'])

        # Adding unique constraint on 'Spirituality', fields ['label']
        db.create_unique('timing_spirituality', ['label'])

        # Adding unique constraint on 'Gender', fields ['label']
        db.create_unique('timing_gender', ['label'])

        # Adding unique constraint on 'Race', fields ['label']
        db.create_unique('timing_race', ['label'])

        # Adding unique constraint on 'Occupation', fields ['label']
        db.create_unique('timing_occupation', ['label'])

        # Adding unique constraint on 'Ethnicity', fields ['label']
        db.create_unique('timing_ethnicity', ['label'])

        # Adding unique constraint on 'ReligiousAffiliation', fields ['label']
        db.create_unique('timing_religiousaffiliation', ['label'])

        # Adding unique constraint on 'PoliticalIdentity', fields ['label']
        db.create_unique('timing_politicalidentity', ['label'])

        # Adding unique constraint on 'CountryOfResidence', fields ['label']
        db.create_unique('timing_countryofresidence', ['label'])

        # Adding unique constraint on 'EducationLevel', fields ['label']
        db.create_unique('timing_educationlevel', ['label'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'EducationLevel', fields ['label']
        db.delete_unique('timing_educationlevel', ['label'])

        # Removing unique constraint on 'CountryOfResidence', fields ['label']
        db.delete_unique('timing_countryofresidence', ['label'])

        # Removing unique constraint on 'PoliticalIdentity', fields ['label']
        db.delete_unique('timing_politicalidentity', ['label'])

        # Removing unique constraint on 'ReligiousAffiliation', fields ['label']
        db.delete_unique('timing_religiousaffiliation', ['label'])

        # Removing unique constraint on 'Ethnicity', fields ['label']
        db.delete_unique('timing_ethnicity', ['label'])

        # Removing unique constraint on 'Occupation', fields ['label']
        db.delete_unique('timing_occupation', ['label'])

        # Removing unique constraint on 'Race', fields ['label']
        db.delete_unique('timing_race', ['label'])

        # Removing unique constraint on 'Gender', fields ['label']
        db.delete_unique('timing_gender', ['label'])

        # Removing unique constraint on 'Spirituality', fields ['label']
        db.delete_unique('timing_spirituality', ['label'])

        # Deleting model 'Handedness'
        db.delete_table('timing_handedness')


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
            'country_of_residence': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.CountryOfResidence']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'education_level': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.EducationLevel']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'email_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ethnicity': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.Ethnicity']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.Gender']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.Occupation']", 'null': 'True', 'blank': 'True'}),
            'participant_number': ('django.db.models.fields.CharField', [], {'default': "'121064'", 'unique': 'True', 'max_length': '8'}),
            'policital_identity': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.PoliticalIdentity']", 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.Race']", 'null': 'True', 'blank': 'True'}),
            'religious_affiliation': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.ReligiousAffiliation']", 'null': 'True', 'blank': 'True'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'spirituality': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.Spirituality']", 'null': 'True', 'blank': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'ms_since_run_start': ('django.db.models.fields.IntegerField', [], {}),
            'press_num': ('django.db.models.fields.IntegerField', [], {}),
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
            'planned_length_sec': ('django.db.models.fields.IntegerField', [], {'default': '900'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.spirituality': {
            'Meta': {'ordering': "['position']", 'object_name': 'Spirituality'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['timing']
