# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Preparation'
        db.delete_table(u'public_preparation')

        # Adding model 'Instruction'
        db.create_table(u'public_instruction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('instruction', self.gf('django.db.models.fields.TextField')()),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'public', ['Instruction'])

        # Deleting field 'Recipe.instructions'
        db.delete_column(u'public_recipe', 'instructions')

        # Removing M2M table for field preparation on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_preparation'))

        # Adding M2M table for field instructions on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_instructions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('instruction', models.ForeignKey(orm[u'public.instruction'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'instruction_id'])


    def backwards(self, orm):
        # Adding model 'Preparation'
        db.create_table(u'public_preparation', (
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('instruction', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'public', ['Preparation'])

        # Deleting model 'Instruction'
        db.delete_table(u'public_instruction')


        # User chose to not deal with backwards NULL issues for 'Recipe.instructions'
        raise RuntimeError("Cannot reverse this migration. 'Recipe.instructions' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Recipe.instructions'
        db.add_column(u'public_recipe', 'instructions',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)

        # Adding M2M table for field preparation on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_preparation')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('preparation', models.ForeignKey(orm[u'public.preparation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'preparation_id'])

        # Removing M2M table for field instructions on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_instructions'))


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