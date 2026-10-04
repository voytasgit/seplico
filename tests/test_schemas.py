import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
APP_SCHEMA = json.loads((ROOT / 'schema/application.schema.json').read_text(encoding='utf-8'))
INT_SCHEMA = json.loads((ROOT / 'schema/interaction.schema.json').read_text(encoding='utf-8'))
APP = Draft202012Validator(APP_SCHEMA, format_checker=FormatChecker())
INT = Draft202012Validator(INT_SCHEMA, format_checker=FormatChecker())

class SeplicoSchemaTests(unittest.TestCase):
    def load(self, rel):
        return json.loads((ROOT / rel).read_text(encoding='utf-8'))

    def assertValid(self, validator, value):
        errors = sorted(validator.iter_errors(value), key=lambda e: list(e.path))
        self.assertFalse(errors, '\n'.join(e.message for e in errors))

    def test_application_example_valid(self):
        self.assertValid(APP, self.load('examples/software-developer.seplico'))

    def test_identity_request_valid(self):
        self.assertValid(INT, self.load('examples/identity-request.json'))

    def test_identity_response_valid(self):
        self.assertValid(INT, self.load('examples/identity-response.json'))

    def test_direct_email_field_rejected_in_application(self):
        doc = self.load('examples/software-developer.seplico')
        doc['email'] = 'person@example.invalid'
        self.assertTrue(list(APP.iter_errors(doc)))

    def test_verified_flag_rejected(self):
        doc = self.load('examples/software-developer.seplico')
        doc['evidence'][0]['verified'] = True
        self.assertTrue(list(APP.iter_errors(doc)))

    def test_global_person_id_rejected(self):
        doc = self.load('examples/software-developer.seplico')
        doc['person_id'] = 'person-123'
        self.assertTrue(list(APP.iter_errors(doc)))

    def test_evidence_references_resolve(self):
        doc = self.load('examples/software-developer.seplico')
        evidence_ids = {item['evidence_id'] for item in doc.get('evidence', [])}
        refs = {ref for skill in doc.get('skills', []) for ref in skill.get('evidence_refs', [])}
        self.assertTrue(refs.issubset(evidence_ids))

    def test_identity_response_requires_consent_true(self):
        doc = self.load('examples/identity-response.json')
        doc['consent'] = False
        self.assertTrue(list(INT.iter_errors(doc)))

    def test_request_attribute_is_limited(self):
        doc = self.load('examples/identity-request.json')
        doc['requested_attributes'].append('date_of_birth')
        self.assertTrue(list(INT.iter_errors(doc)))

    def test_example_interaction_flow_is_consistent(self):
        req = self.load('examples/identity-request.json')
        res = self.load('examples/identity-response.json')
        self.assertEqual(res['application_id'], req['application_id'])
        self.assertEqual(res['request_id'], req['request_id'])
        self.assertTrue(set(res['released_attributes']).issubset(set(req['requested_attributes'])))

    def test_unrequested_released_attribute_is_semantically_invalid(self):
        req = self.load('examples/identity-request.json')
        res = self.load('examples/identity-response.json')
        res['released_attributes']['phone'] = '+49 000 000000'
        self.assertFalse(set(res['released_attributes']).issubset(set(req['requested_attributes'])))

if __name__ == '__main__':
    unittest.main()
