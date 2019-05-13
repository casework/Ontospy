# Cyber-investigation Analysis Standard Expression (CASE)

_Read the [CASE Wiki tab](https://github.com/casework/CASE/wiki) to learn **everything** you need to know about the Cyber-investigation Analysis Standard Expression (CASE) ontology._
_For learning about the Unified Cyber Ontology, CASE's parent, see [UCO](https://github.com/ucoProject/UCO)._

# OntoSpy

**_Note: OntoSpy was forked so that a static version of the tool could be obtained. The Python API's autogeneration relies on this static version for parsing purposes (v0.1.0). In the future if this fork is to be updated from the original lambdamusic repository it may require updating the scripts. Thus, when using OntoSpy for mapping or ontological purposes we suggest using the original repository._**

Python toolkit for inspecting linked data knowledge models AKA ontologies or vocabularies.


### Description

OntoSpy is a lightweight Python library and command line tool for inspecting and visualizing vocabularies encoded using W3C Semantic Web standards, that is, RDF or any of its dialects (RDFS, OWL, SKOS).

The basic workflow is simple: load a graph by instantiating the ``Ontospy`` class with a file containing RDFS, OWL or SKOS definitions. You get back an object that lets you interrogate the ontology. That's all!

The same functionalities are accessible also via a command line application (`ontospy-shell`). This is an interactive environment (like a repl) that allows to load ontologies from a local repository, interrogate them and cache them so that they can be quickly reloaded for inspection later on.


### More info
https://github.com/lambdamusic/OntoSpy/wiki

# I have a question!

Before you post a Github issue or send an email ensure you've done this checklist:

1. [Determined scope](https://caseontology.org/ontology/start.html#scope) of your task. It is not necessary for most parties to understand all aspects of the ontology, mapping methods, and supporting tools.

2. Familiarize yourself with the [labels](https://github.com/casework/Ontospy/labels) and search the [Issues tab](https://github.com/casework/Ontospy/issues). Typically, only light-blue and red labels should be used by non-admin Github users while the others should be used by CASE Github admins.
*All but the red `Project` labels are found in every [`casework`](https://github.com/casework) repository.*

3. This repository is a "preserved" fork that is used for backend autogeneration, etc. All feature/bug requests for the core functionality of the tool should be reported to the original repository. However, if it is something that is specific to CASE we _may_ add support a patch here.
