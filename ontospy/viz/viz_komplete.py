# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
#
#
# TEST TEST TEST TEST TES
#
#



from .. import *
from ..core.utils import *
from ..core.manager import *

from .utils import *
from .viz_factory import VizFactory

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass

# django loading requires different steps based on version
# https://docs.djangoproject.com/en/dev/releases/1.7/#standalone-scripts
import django

# http://stackoverflow.com/questions/1714027/version-number-comparison
from distutils.version import StrictVersion

if StrictVersion(django.get_version()) > StrictVersion('1.7'):
    from django.conf import settings
    from django.template import Context, Template

else:
    from django.conf import settings
    from django.template import Context, Template


import os, sys



class KompleteViz(VizFactory):
    """

    """

    def __init__(self, ontospy_graph, title=""):
        """
        Init
        """
        super(KompleteViz, self).__init__(ontospy_graph, title)
        self.static_files = ["static"]


    def _buildTemplates(self):
        """
        OVERRIDING THIS METHOD from Factory
        """

        # DASHBOARD - MAIN PAGE
        contents = self._renderTemplate("komplete/dashboard.html", extraContext=None)
        FILE_NAME = "dashboard.html"
        main_url = self._save2File(contents, FILE_NAME, self.output_path)

        # VIZ LIST
        if False:
            contents = self._renderTemplate("komplete/viz_list.html", extraContext=None)
            FILE_NAME = "visualizations.html"
            self._save2File(contents, FILE_NAME, self.output_path)


        browser_output_path = self.output_path

        # ENTITIES A-Z
        extra_context = {"ontograph": self.ontospy_graph}
        contents = self._renderTemplate("komplete/browser/browser_entities_az.html", extraContext=extra_context)
        FILE_NAME = "entities-az.html"
        self._save2File(contents, FILE_NAME, browser_output_path)



        if self.ontospy_graph.classes:
            # CLASSES = ENTITIES TREE
            extra_context = {"ontograph": self.ontospy_graph, "treetype" : "classes",
                'treeTable' : formatHTML_EntityTreeTable(self.ontospy_graph.ontologyClassTree())}
            contents = self._renderTemplate("komplete/browser/browser_entities_tree.html", extraContext=extra_context)
            FILE_NAME = "entities-tree-classes.html"
            self._save2File(contents, FILE_NAME, browser_output_path)
            # BROWSER PAGES - CLASSES ======
            for entity in self.ontospy_graph.classes:
                extra_context = {"main_entity": entity,
                                "main_entity_type": "class",
                                "ontograph": self.ontospy_graph
                                }
                extra_context.update(self.highlight_code(entity))
                contents = self._renderTemplate("komplete/browser/browser_classinfo.html", extraContext=extra_context)
                FILE_NAME = entity.slug + ".html"
                self._save2File(contents, FILE_NAME, browser_output_path)


        if self.ontospy_graph.properties:

            # PROPERTIES = ENTITIES TREE
            extra_context = {"ontograph": self.ontospy_graph, "treetype" : "properties",
                'treeTable' : formatHTML_EntityTreeTable(self.ontospy_graph.ontologyPropTree())}
            contents = self._renderTemplate("komplete/browser/browser_entities_tree.html", extraContext=extra_context)
            FILE_NAME = "entities-tree-properties.html"
            self._save2File(contents, FILE_NAME, browser_output_path)

            # BROWSER PAGES - PROPERTIES ======

            for entity in self.ontospy_graph.properties:
                extra_context = {"main_entity": entity,
                                "main_entity_type": "property",
                                "ontograph": self.ontospy_graph
                                }
                extra_context.update(self.highlight_code(entity))
                contents = self._renderTemplate("komplete/browser/browser_propinfo.html", extraContext=extra_context)
                FILE_NAME = entity.slug + ".html"
                self._save2File(contents, FILE_NAME, browser_output_path)


        if self.ontospy_graph.skosConcepts:

            # CONCEPTS = ENTITIES TREE

            extra_context = {"ontograph": self.ontospy_graph, "treetype" : "concepts",
                'treeTable' : formatHTML_EntityTreeTable(self.ontospy_graph.ontologyConceptTree())}
            contents = self._renderTemplate("komplete/browser/browser_entities_tree.html", extraContext=extra_context)
            FILE_NAME = "entities-tree-concepts.html"
            self._save2File(contents, FILE_NAME, browser_output_path)

            # BROWSER PAGES - CONCEPTS ======

            for entity in self.ontospy_graph.skosConcepts:
                extra_context = {"main_entity": entity,
                                "main_entity_type": "concept",
                                "ontograph": self.ontospy_graph
                                }
                extra_context.update(self.highlight_code(entity))
                contents = self._renderTemplate("komplete/browser/browser_conceptinfo.html", extraContext=extra_context)
                FILE_NAME = entity.slug + ".html"
                self._save2File(contents, FILE_NAME, browser_output_path)


        return main_url



if __name__ == '__main__':

    TEST_ONLINE = False
    try:

        if TEST_ONLINE:
            from ..core.ontospy import Ontospy
            g = Ontospy("http://cohere.open.ac.uk/ontology/cohere.owl#")
        else:
            uri, g = get_random_ontology(50) # pattern="core"

        v = KompleteViz(g)
        v.build()
        v.preview()

        sys.exit(0)

    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
