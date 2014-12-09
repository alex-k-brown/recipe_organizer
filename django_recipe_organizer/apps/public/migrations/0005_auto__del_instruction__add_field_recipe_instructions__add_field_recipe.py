# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Instruction'
        db.delete_table(u'public_instruction')

        # Adding field 'Recipe.instructions'
        db.add_column(u'public_recipe', 'instructions',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Recipe.video'
        db.add_column(u'public_recipe', 'video',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field instructions on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_instructions'))


        # Changing field 'Recipe.categories'
        db.alter_column(u'public_recipe', 'categories', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):
        # Adding model 'Instruction'
        db.create_table(u'public_instruction', (
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('instruction', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'public', ['Instruction'])

        # Deleting field 'Recipe.instructions'
        db.delete_column(u'public_recipe', 'instructions')

        # Deleting field 'Recipe.video'
        db.delete_column(u'public_recipe', 'video')

        # Adding M2M table for field instructions on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_instructions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('instruction', models.ForeignKey(orm[u'public.instruction'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'instruction_id'])


        # Changing field 'Recipe.categories'
        db.alter_column(u'public_recipe', 'categories', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'brand': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'categories': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'No description has been entered yet'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'instructions': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'time': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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