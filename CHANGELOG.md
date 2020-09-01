# Metadata Registry Interfaces Changelog

In this document we'll track the releases of the Metadata Registry Interface Specifications, with notable changes and potential backwards compatibility issues. See [TODO.md](TODO.md) for an actual list of known issues.


## Master

The master branch may contain functionality that is not yet in a point release. Currently the following features are in master:

* Lineage metadata structures for physical entities and their attributes, including the association between them


## Version 0.1.0

* Introduction unit tests

## Version 0.2.0

### Structure changes
* Attribute json is now  list of attributes for one entity
* Introduced "meta" and "meta_version" in all schemas
* Added "version" and "uid" to DAG, job and Task (mandatory)
* Added "description" to DAG, job and task (optional)
* Job structure changed

### Examples and Unit tests
* provided examples for DAG, job and task
* Added unittests for DAC, job and task
