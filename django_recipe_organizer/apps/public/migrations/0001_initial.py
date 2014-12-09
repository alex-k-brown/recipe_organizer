# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table(u'public_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('categories', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('instructions', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('rating', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('time', self.gf('django.db.models.fields.TimeField')(default=0)),
        ))
        db.send_create_signal(u'public', ['Recipe'])

        # Adding M2M table for field ingredients on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('ingredient', models.ForeignKey(orm[u'public.ingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'ingredient_id'])

        # Adding M2M table for field preparation on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_preparation')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('preparation', models.ForeignKey(orm[u'public.preparation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'preparation_id'])

        # Adding model 'Ingredient'
        db.create_table(u'public_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('brand', self.gf('django.db.models.fields.CharField')(default=0, max_length=100)),
        ))
        db.send_create_signal(u'public', ['Ingredient'])

        # Adding model 'Preparation'
        db.create_table(u'public_preparation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('instruction', self.gf('django.db.models.fields.TextField')()),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'public', ['Preparation'])

        # Adding model 'Takeout'
        db.create_table(u'public_takeout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('restaurants', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rating', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
        ))
        db.send_create_signal(u'public', ['Takeout'])


    def backwards(self, orm):
        # Deleting model 'Recipe'
        db.delete_table(u'public_recipe')

        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_ingredients'))

        # Removing M2M table for field preparation on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_preparation'))

        # Deleting model 'Ingredient'
        db.delete_table(u'public_ingredient')

        # Deleting model 'Preparation'
        db.delete_table(u'public_preparation')

        # Deleting model 'Takeout'
        db.delete_table(u'public_takeout')


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'brand': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.preparation': {
            'Meta': {'object_name': 'Preparation'},
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
            'instructions': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'preparation': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Preparation']", 'symmetrical': 'False'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'time': ('django.db.models.fields.TimeField', [], {'default': '0'})
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