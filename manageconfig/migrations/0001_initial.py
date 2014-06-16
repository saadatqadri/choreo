# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manufacturer'
        db.create_table(u'manageconfig_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('service_contract_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('service_contract_number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('service_contract_phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('service_contract_expiry', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'manageconfig', ['Manufacturer'])

        # Adding model 'ConfigurationItem'
        db.create_table(u'manageconfig_configurationitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('parent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('asset_class', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['manageconfig.Manufacturer'])),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('operating_sys', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rack', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
        ))
        db.send_create_signal(u'manageconfig', ['ConfigurationItem'])


    def backwards(self, orm):
        # Deleting model 'Manufacturer'
        db.delete_table(u'manageconfig_manufacturer')

        # Deleting model 'ConfigurationItem'
        db.delete_table(u'manageconfig_configurationitem')


    models = {
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

    complete_apps = ['manageconfig']