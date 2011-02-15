# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Spirituality'
        db.create_table('timing_spirituality', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['Spirituality'])

        # Adding model 'Gender'
        db.create_table('timing_gender', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['Gender'])

        # Adding model 'Race'
        db.create_table('timing_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['Race'])

        # Adding model 'CountyOfResidence'
        db.create_table('timing_countyofresidence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['CountyOfResidence'])

        # Adding model 'Occupation'
        db.create_table('timing_occupation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['Occupation'])

        # Adding model 'Ethnicity'
        db.create_table('timing_ethnicity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['Ethnicity'])

        # Adding model 'PoliticalIdentity'
        db.create_table('timing_politicalidentity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['PoliticalIdentity'])

        # Adding model 'ReligiousAffiliation'
        db.create_table('timing_religiousaffiliation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['ReligiousAffiliation'])

        # Adding model 'EducationLevel'
        db.create_table('timing_educationlevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('scm_revision', self.gf('django.db.models.fields.CharField')(default='.', max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('timing', ['EducationLevel'])

        # Adding field 'Participant.gender'
        db.add_column('timing_participant', 'gender', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timing.Gender'], null=True, blank=True), keep_default=False)

        # Adding field 'Participant.race'
        db.add_column('timing_participant', 'race', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timing.Race'], null=True, blank=True), keep_default=False)

        # Adding field 'Participant.ethnicity'
        db.add_column('timing_participant', 'ethnicity', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timing.Ethnicity'], null=True, blank=True), keep_default=False)

        # Adding field 'Participant.country_of_residence'
        db.add_column('timing_participant', 'country_of_residence', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timing.CountyOfResidence'], null=True, blank=True), keep_default=False)

        # Adding field 'Participant.education_level'
        db.add_column('timing_participant', 'education_level', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timing.EducationLevel'], null=True, blank=True), keep_default=False)

        # Adding field 'Participant.spirituality'
        db.add_column('timing_participant', 'spirituality', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timing.Spirituality'], null=True, blank=True), keep_default=False)

        # Adding field 'Participant.religious_affiliation'
        db.add_column('timing_participant', 'religious_affiliation', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timing.ReligiousAffiliation'], null=True, blank=True), keep_default=False)

        # Adding field 'Participant.policital_identity'
        db.add_column('timing_participant', 'policital_identity', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timing.PoliticalIdentity'], null=True, blank=True), keep_default=False)

        # Adding field 'Participant.occupation'
        db.add_column('timing_participant', 'occupation', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timing.Occupation'], null=True, blank=True), keep_default=False)

        # Adding field 'Participant.postal_code'
        db.add_column('timing_participant', 'postal_code', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True), keep_default=False)

        # Adding field 'Participant.birth_year'
        db.add_column('timing_participant', 'birth_year', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Participant.birth_month'
        db.add_column('timing_participant', 'birth_month', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Spirituality'
        db.delete_table('timing_spirituality')

        # Deleting model 'Gender'
        db.delete_table('timing_gender')

        # Deleting model 'Race'
        db.delete_table('timing_race')

        # Deleting model 'CountyOfResidence'
        db.delete_table('timing_countyofresidence')

        # Deleting model 'Occupation'
        db.delete_table('timing_occupation')

        # Deleting model 'Ethnicity'
        db.delete_table('timing_ethnicity')

        # Deleting model 'PoliticalIdentity'
        db.delete_table('timing_politicalidentity')

        # Deleting model 'ReligiousAffiliation'
        db.delete_table('timing_religiousaffiliation')

        # Deleting model 'EducationLevel'
        db.delete_table('timing_educationlevel')

        # Deleting field 'Participant.gender'
        db.delete_column('timing_participant', 'gender_id')

        # Deleting field 'Participant.race'
        db.delete_column('timing_participant', 'race_id')

        # Deleting field 'Participant.ethnicity'
        db.delete_column('timing_participant', 'ethnicity_id')

        # Deleting field 'Participant.country_of_residence'
        db.delete_column('timing_participant', 'country_of_residence_id')

        # Deleting field 'Participant.education_level'
        db.delete_column('timing_participant', 'education_level_id')

        # Deleting field 'Participant.spirituality'
        db.delete_column('timing_participant', 'spirituality_id')

        # Deleting field 'Participant.religious_affiliation'
        db.delete_column('timing_participant', 'religious_affiliation_id')

        # Deleting field 'Participant.policital_identity'
        db.delete_column('timing_participant', 'policital_identity_id')

        # Deleting field 'Participant.occupation'
        db.delete_column('timing_participant', 'occupation_id')

        # Deleting field 'Participant.postal_code'
        db.delete_column('timing_participant', 'postal_code')

        # Deleting field 'Participant.birth_year'
        db.delete_column('timing_participant', 'birth_year')

        # Deleting field 'Participant.birth_month'
        db.delete_column('timing_participant', 'birth_month')


    models = {
        'timing.countyofresidence': {
            'Meta': {'ordering': "['position']", 'object_name': 'CountyOfResidence'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.educationlevel': {
            'Meta': {'ordering': "['position']", 'object_name': 'EducationLevel'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.ethnicity': {
            'Meta': {'ordering': "['position']", 'object_name': 'Ethnicity'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.gender': {
            'Meta': {'ordering': "['position']", 'object_name': 'Gender'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.occupation': {
            'Meta': {'ordering': "['position']", 'object_name': 'Occupation'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.participant': {
            'Meta': {'object_name': 'Participant'},
            'birth_month': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'country_of_residence': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.CountyOfResidence']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'education_level': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.EducationLevel']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'ethnicity': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.Ethnicity']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.Gender']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['timing.Occupation']", 'null': 'True', 'blank': 'True'}),
            'participant_number': ('django.db.models.fields.CharField', [], {'default': "'413869'", 'unique': 'True', 'max_length': '8'}),
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
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.race': {
            'Meta': {'ordering': "['position']", 'object_name': 'Race'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'timing.religiousaffiliation': {
            'Meta': {'ordering': "['position']", 'object_name': 'ReligiousAffiliation'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
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
            'label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'scm_revision': ('django.db.models.fields.CharField', [], {'default': "'.'", 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['timing']
