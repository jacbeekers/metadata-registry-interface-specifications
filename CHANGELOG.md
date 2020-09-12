# Metadata Registry Interfaces Changelog

In this document we'll track the releases of the Metadata Registry Interface Specifications, with notable changes and potential backwards compatibility issues. See [TODO.md](TODO.md) for an actual list of known issues.


## Master

The master branch may contain functionality that is not yet in a point release. Currently the following features are in master:

* Lineage metadata structures for physical entities and their attributes, including the association between them

## Version 0.3.0

### Breaking structure changes
* task.json is now an array with tasks, so for one DAG one single file with all tasks within that DAG can be provided. The task json must include the uuid of the DAG.
* added location as required attribute in physical_entity.json
* the dag.json has been simplified. You can now only reference task uuids. The task uuids have to be listed in a task.json.

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

## Version 0.1.0

* Introduction unit tests
