# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding unique constraint on 'Pronostico', fields ['partido', 'usuario']
        db.create_unique(u'Quiniela_pronostico', ['partido_id', 'usuario_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Pronostico', fields ['partido', 'usuario']
        db.delete_unique(u'Quiniela_pronostico', ['partido_id', 'usuario_id'])


    models = {
        u'Quiniela.equipo': {
            'Meta': {'object_name': 'Equipo'},
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
            'url_bandera': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'Quiniela.grupo': {
            'Meta': {'object_name': 'Grupo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'Quiniela.partido': {
            'Meta': {'object_name': 'Partido'},
            'equipo_a': ('django.db.models.fields.related.ForeignKey', [],
                         {'related_name': "'equipo_a'", 'to': u"orm['Quiniela.Equipo']"}),
            'equipo_b': ('django.db.models.fields.related.ForeignKey', [],
                         {'related_name': "'equipo_b'", 'to': u"orm['Quiniela.Equipo']"}),
            'equipo_ganador': ('django.db.models.fields.related.ForeignKey', [],
                               {'related_name': "'equipo_ganador'", 'null': 'True', 'to': u"orm['Quiniela.Equipo']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'goles_equipo_a': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'goles_equipo_b': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'Quiniela.pronostico': {
            'Meta': {'unique_together': "(('partido', 'usuario'),)", 'object_name': 'Pronostico'},
            'goles_equipo_a': ('django.db.models.fields.IntegerField', [], {}),
            'goles_equipo_b': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Quiniela.Partido']"}),
            'puntos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Quiniela.Usuario']"})
        },
        u'Quiniela.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'correo': (
            'django.db.models.fields.EmailField', [], {'default': "'usuario@tcs.com.ve'", 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pago_realizado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'puntos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['Quiniela']