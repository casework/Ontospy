# Cyber-investigation Analysis Standard Expression (CASE)

_Read the [CASE Wiki tab](https://github.com/ucoProject/CASE/wiki) to learn **everything** you need to know about the Cyber-investigation Analysis Standard Expression (CASE) ontology._
_For learning about the Unified Cyber Ontology, CASE's parent, see [UCO](https://github.com/ucoProject/UCO)._

# OntoSpy

**_Note: Ontospy was forked so that a static version of the tool could be obtained. The Python API's Autogeneration feature relies on this static version for parsing purposes (v0.1.0). In the future if this fork is to be updated from the original lambdamusic repository it may require updating the scripts._**

Python toolkit for inspecting linked data knowledge models AKA ontologies or vocabularies.


### Description

OntoSpy is a lightweight Python library and command line tool for inspecting and visualizing vocabularies encoded using W3C Semantic Web standards, that is, RDF or any of its dialects (RDFS, OWL, SKOS).

The basic workflow is simple: load a graph by instantiating the ``Ontospy`` class with a file containing RDFS, OWL or SKOS definitions. You get back an object that lets you interrogate the ontology. That's all!

The same functionalities are accessible also via a command line application (`ontospy-shell`). This is an interactive environment (like a repl) that allows to load ontologies from a local repository, interrogate them and cache them so that they can be quickly reloaded for inspection later on.


### More info
https://github.com/lambdamusic/OntoSpy/wiki
