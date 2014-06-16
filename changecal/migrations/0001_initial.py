# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ChangeRequest'
        db.create_table(u'changecal_changerequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('nomsv2', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('configitem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['manageconfig.ConfigurationItem'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('reason', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('change_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('impact', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('urgency', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('details', self.gf('django.db.models.fields.TextField')()),
            ('testing', self.gf('django.db.models.fields.TextField')()),
            ('impact_details', self.gf('django.db.models.fields.TextField')()),
            ('backout', self.gf('django.db.models.fields.TextField')()),
            ('change_artifacts', self.gf('django.db.models.fields.TextField')()),
            ('initial_approver', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('final_approver', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('implementor', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('submitted_by', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'changecal', ['ChangeRequest'])


    def backwards(self, orm):
        # Deleting model 'ChangeRequest'
        db.delete_table(u'changecal_changerequest')


    models = {
        u'changecal.changerequest': {
            'Meta': {'ordering': "('created',)", 'object_name': 'ChangeRequest'},
            'backout': ('django.db.models.fields.TextField', [], {}),
            'change_artifacts': ('django.db.models.fields.TextField', [], {}),
            'change_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'configitem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manageconfig.ConfigurationItem']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'final_approver': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'impact_details': ('django.db.models.fields.TextField', [], {}),
            'implementor': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'initial_approver': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nomsv2': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'submitted_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'testing': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'urgency': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'manageconfig.configurationitem': {
            'Meta': {'object_name': 'ConfigurationItem'},
            'asset_class': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manageconfig.Manufacturer']"}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'operating_sys': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rack': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'manageconfig.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'service_contract_expiry': ('django.db.models.fields.DateTimeField', [], {}),
            'service_contract_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'service_contract_number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'service_contract_phone': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['changecal']