# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Equipo.codigo'
        db.add_column(u'Quiniela_equipo', 'codigo',
                      self.gf('django.db.models.fields.CharField')(default='BRA', max_length=3),
                      keep_default=False)


        # Changing field 'Equipo.url_bandera'
        db.alter_column(u'Quiniela_equipo', 'url_bandera', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Equipo.codigo'
        db.delete_column(u'Quiniela_equipo', 'codigo')


        # Changing field 'Equipo.url_bandera'
        db.alter_column(u'Quiniela_equipo', 'url_bandera', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        u'Quiniela.equipo': {
            'Meta': {'ordering': "['grupo__nombre', '-puntos', 'nombre']", 'object_name': 'Equipo'},
            'codigo': ('django.db.models.fields.CharField', [], {'default': "'BRA'", 'max_length': '3'}),
            'goles_a_favor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goles_en_contra': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Quiniela.Grupo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'partidos_empatados': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'partidos_ganados': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'partidos_jugados': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'partidos_perdidos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puntos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url_bandera': ('django.db.models.fields.files.FileField', [], {'default': "'bra.png'", 'max_length': '100'})
        },
        u'Quiniela.grupo': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Grupo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'Quiniela.partido': {
            'Meta': {'ordering': "['fecha']", 'object_name': 'Partido'},
            'equipo_a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equipo_a'", 'null': 'True', 'to': u"orm['Quiniela.Equipo']"}),
            'equipo_b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equipo_b'", 'null': 'True', 'to': u"orm['Quiniela.Equipo']"}),
            'equipo_ganador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'equipo_ganador'", 'null': 'True', 'to': u"orm['Quiniela.Equipo']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'goles_equipo_a': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goles_equipo_b': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partido_jugado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tipo_partido': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'Quiniela.perfil': {
            'Meta': {'object_name': 'Perfil'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'Quiniela.pronostico': {
            'Meta': {'ordering': "['partido']", 'unique_together': "(('partido', 'usuario'),)", 'object_name': 'Pronostico'},
            'goles_equipo_a': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goles_equipo_b': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Quiniela.Partido']"}),
            'puntos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'Quiniela.usuario': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Usuario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'correo': ('django.db.models.fields.EmailField', [], {'default': "'usuario@tcs.com.ve'", 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pago_realizado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'puntos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Quiniela']