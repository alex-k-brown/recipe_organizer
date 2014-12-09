# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recipe.photo'
        db.add_column(u'public_recipe', 'photo',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Recipe.photo'
        db.delete_column(u'public_recipe', 'photo')


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'brand': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.instruction': {
            'Meta': {'object_name': 'Instruction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'categories': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'instructions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Instruction']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'time': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'public.takeout': {
            'Meta': {'object_name': 'Takeout'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'restaurants': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['public']