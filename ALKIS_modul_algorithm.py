# -*- coding: utf-8 -*-

"""
/***************************************************************************
 ALKIS_Objektarten
                                 A QGIS plugin
 Das Plugin hilft bei Aufbereitung von ALKIS Daten 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-06-15
        copyright            : (C) 2023 by Sajjad Tabatabaei
        email                : sajjadtabatabaei05@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Sajjad Tabatabaei'
__date__ = '2023-06-15'
__copyright__ = '(C) 2023 by Sajjad Tabatabaei'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'
from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
import processing
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink)


class ALKIS_ObjektartenAlgorithm(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('NutzungFlurstueck', 'NutzungFlurstueck', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Verkehr', 'Verkehr', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Extract by expression
        alg_params = {
            'EXPRESSION': ' (\"nutzart\" = \'Platz\' and  \"bez\" is  NULL) or  (\"nutzart\" = \'Platz\' and  \"bez\" =   \'Festplatz\' ) or (\"nutzart\" = \'Platz\' and  \"bez\" =   \'Fußgängerzone\' ) or (\"nutzart\" = \'Platz\' and  \"bez\" =   \'Marktplatz\' ) or (\"nutzart\" = \'Platz\' and  \"bez\" =  \'Parkplatz\') or (\"nutzart\" = \'Platz\' and  \"bez\" =   \'Rastplatz\' ) or ( \"nutzart\" = \'Straßenverkehr\' and  \"bez\" is  NULL ) or ( \"nutzart\" = \'Straßenverkehr\' and  \"bez\" =   \'Fußgängerzone\' ) or ( \"nutzart\" = \'Weg\' and  \"bez\" = \'Fahrweg\' ) or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Fußweg\') or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Gang\'  )or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Hauptwirtschaftsweg\' ) or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Rad- und Fußweg\'  ) or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Radweg\'  ) or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Wirtschaftsweg\' ) or ( \"nutzart\" = \'Weg\' and  \"bez\" is NULL)',
            'INPUT': parameters['NutzungFlurstueck'],
            'OUTPUT': parameters['Verkehr']
        }
        outputs['ExtractByExpression'] = processing.run('native:extractbyexpression', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Verkehr'] = outputs['ExtractByExpression']['OUTPUT']
        return results

    def name(self):
        return 'erstelle_objektartengruppen'
    def displayName(self):
        return 'erstelle_objektartengruppen'
    def group(self):
        return 'ALKIS1'
    def groupId(self):
        return 'ALKIS1'
    def createInstance(self):
        return ALKIS_ObjektartenAlgorithm()

class ALKIS_GebaeudeAlgorithm(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('NutzungFlurstueck', 'NutzungFlurstueck', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Verkehr', 'Verkehr', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Extract by expression
        alg_params = {
            'EXPRESSION': ' (\"nutzart\" = \'Platz\' and  \"bez\" is  NULL) or  (\"nutzart\" = \'Platz\' and  \"bez\" =   \'Festplatz\' ) or (\"nutzart\" = \'Platz\' and  \"bez\" =   \'Fußgängerzone\' ) or (\"nutzart\" = \'Platz\' and  \"bez\" =   \'Marktplatz\' ) or (\"nutzart\" = \'Platz\' and  \"bez\" =  \'Parkplatz\') or (\"nutzart\" = \'Platz\' and  \"bez\" =   \'Rastplatz\' ) or ( \"nutzart\" = \'Straßenverkehr\' and  \"bez\" is  NULL ) or ( \"nutzart\" = \'Straßenverkehr\' and  \"bez\" =   \'Fußgängerzone\' ) or ( \"nutzart\" = \'Weg\' and  \"bez\" = \'Fahrweg\' ) or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Fußweg\') or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Gang\'  )or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Hauptwirtschaftsweg\' ) or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Rad- und Fußweg\'  ) or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Radweg\'  ) or ( \"nutzart\" = \'Weg\' and  \"bez\" =  \'Wirtschaftsweg\' ) or ( \"nutzart\" = \'Weg\' and  \"bez\" is NULL)',
            'INPUT': parameters['NutzungFlurstueck'],
            'OUTPUT': parameters['Verkehr']
        }
        outputs['ExtractByExpression'] = processing.run('native:extractbyexpression', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Verkehr'] = outputs['ExtractByExpression']['OUTPUT']
        return results

    def name(self):
        return 'erstelle_Gebaeude'
    def displayName(self):
        return 'erstelle_Gebaeude'
    def group(self):
        return 'ALKIS2'
    def groupId(self):
        return 'ALKIS2'
    def createInstance(self):
        return ALKIS_GebaeudeAlgorithm()
