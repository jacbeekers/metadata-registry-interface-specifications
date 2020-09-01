import unittest
import jsonschema
import json
from pathlib import Path


class ValidateExampleSchemas(unittest.TestCase):

    version = "0.2.0"
    base_schema_directory = "../schemas/interface/" + version + "/"
    base_test_resources_directory = "../test_resources/" + version + "/"

    def test_physical_entity_schema(self):
        json_document = self.base_test_resources_directory + "correct_entity_source.json"
        self.assertTrue(Path(json_document).is_file(), "Could not find entity JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "physical_entity.json"
        self.assertTrue(Path(json_schema).is_file(), "Could not find entity JSON schema >" + json_schema + "<.")

        self.assertTrue(self.validate(json_document, json_schema))

    def test_physical_attribute_schema_with_uuid(self):
        # Case 1 - JSON contains only the UUID of the entity
        json_document = self.base_test_resources_directory + "correct_attribute_source.json"
        self.assertTrue(Path(json_document).is_file(), "Could not find attribute JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "physical_attribute.json"
        self.assertTrue(Path(json_schema).is_file(), "Could not find attribute JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))

    def test_physical_entity_association(self):
        json_document = self.base_test_resources_directory + "correct_entity_association_with_uuids.json"
        self.assertTrue(Path(json_document).is_file(),
                        "Could not find entity association JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "physical_entity_association.json"
        self.assertTrue(Path(json_schema).is_file(),
                        "Could not find entity association JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))

    def test_physical_attribute_association(self):
        json_document = self.base_test_resources_directory + "correct_attribute_association_with_uuids.json"
        self.assertTrue(Path(json_document).is_file(),
                        "Could not find attribute association JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "physical_attribute_association.json"
        self.assertTrue(Path(json_schema).is_file(),
                        "Could not find attribute association JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))

    def test_task(self):
        json_document = self.base_test_resources_directory + "correct_task.json"
        self.assertTrue(Path(json_document).is_file(),
                        "Could not find attribute association JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "task.json"
        self.assertTrue(Path(json_schema).is_file(),
                        "Could not find attribute association JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))

    def test_dag(self):
        json_document = self.base_test_resources_directory + "correct_dag.json"
        self.assertTrue(Path(json_document).is_file(),
                        "Could not find attribute association JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "dag.json"
        self.assertTrue(Path(json_schema).is_file(),
                        "Could not find attribute association JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))

    def test_job(self):
        json_document = self.base_test_resources_directory + "correct_job.json"
        self.assertTrue(Path(json_document).is_file(),
                        "Could not find attribute association JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "job.json"
        self.assertTrue(Path(json_schema).is_file(),
                        "Could not find attribute association JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))

    def validate(self, doc, schema):

        with open(doc) as file:
            the_doc = json.load(file)
            with open(schema) as structure:
                try:
                    the_schema = json.load(structure)
                    jsonschema.validate(the_doc, the_schema)
                    return True
                except jsonschema.exceptions.ValidationError as e:
                    print("Validation error: ", e)
                except json.decoder.JSONDecodeError as e:
                    print("Error parsing JSON:", e)
        return False


if __name__ == '__main__':
    unittest.main()
