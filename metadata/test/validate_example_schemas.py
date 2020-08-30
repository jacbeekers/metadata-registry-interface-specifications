import unittest
import jsonschema
import json
from pathlib import Path


class ValidateExampleSchemas(unittest.TestCase):

    version = "0.1.0"
    base_schema_directory = "metadata/schemas/interface/" + version + "/"
    base_test_resources_directory = "metadata/test_resources/"

    def test_physical_entity_schema(self):
        json_document = self.base_test_resources_directory + "correct_entity.json"
        self.assertTrue(Path(json_document).is_file(), "Could not find entity JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "physical_entity.json"
        self.assertTrue(Path(json_schema).is_file(), "Could not find entity JSON schema >" + json_schema + "<.")

        self.assertTrue(self.validate(json_document, json_schema))

    def test_physical_attribute_schema(self):
        # Case 1 - JSON contains complete entity definition
        json_document = self.base_test_resources_directory + "correct_attribute.json"
        self.assertTrue(Path(json_document).is_file(), "Could not find attribute JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "physical_attribute.json"
        self.assertTrue(Path(json_schema).is_file(), "Could not find attribute JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))

    def test_physical_attribute_schema_with_uuid(self):
        # Case 2 - JSON contains only the UUID of the entity
        json_document = self.base_test_resources_directory + "correct_attribute_with_uid.json"
        self.assertTrue(Path(json_document).is_file(), "Could not find attribute JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "physical_attribute.json"
        self.assertTrue(Path(json_schema).is_file(), "Could not find attribute JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))

    def test_physical_entity_association(self):
        json_document = self.base_test_resources_directory + "correct_entity_association_with_uids.json"
        self.assertTrue(Path(json_document).is_file(),
                        "Could not find entity association JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "physical_entity_assoc.json"
        self.assertTrue(Path(json_schema).is_file(),
                        "Could not find entity association JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))
        # TODO: Add test case that does NOT use UUIDs

    def test_physical_attribute_association(self):
        json_document = self.base_test_resources_directory + "correct_attribute_association_with_uuids.json"
        self.assertTrue(Path(json_document).is_file(),
                        "Could not find attribute association JSON file >" + json_document + "<.")
        json_schema = self.base_schema_directory + "physical_attribute_assoc.json"
        self.assertTrue(Path(json_schema).is_file(),
                        "Could not find attribute association JSON schema >" + json_schema + "<.")
        self.assertTrue(self.validate(json_document, json_schema))
        # TODO: Add test case that does NOT use UUIDs

    def validate(self, doc, schema):

        with open(doc) as file:
            with open(schema) as structure:
                try:
                    the_doc = json.load(file)
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
