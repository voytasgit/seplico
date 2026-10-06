import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
APP_SCHEMA = json.loads((ROOT / 'schema/application.schema.json').read_text(encoding='utf-8'))
INT_SCHEMA = json.loads((ROOT / 'schema/interaction.schema.json').read_text(encoding='utf-8'))
MAP_SCHEMA = json.loads((ROOT / 'schema/evidence-mapping.schema.json').read_text(encoding='utf-8'))
APP = Draft202012Validator(APP_SCHEMA, format_checker=FormatChecker())
INT = Draft202012Validator(INT_SCHEMA, format_checker=FormatChecker())
MAP = Draft202012Validator(MAP_SCHEMA, format_checker=FormatChecker())


def application_claim_ids(doc):
    values = []
    for key in ('skills', 'experience', 'qualifications'):
        values.extend(item['claim_id'] for item in doc.get(key, []) if 'claim_id' in item)
    return values


class SeplicoSchemaTests(unittest.TestCase):
    def load(self, rel):
        return json.loads((ROOT / rel).read_text(encoding='utf-8'))

    def assertValid(self, validator, value):
        errors = sorted(validator.iter_errors(value), key=lambda e: list(e.path))
        self.assertFalse(errors, '\n'.join(e.message for e in errors))

    def test_schemas_are_valid_draft_2020_12(self):
        Draft202012Validator.check_schema(APP_SCHEMA)
        Draft202012Validator.check_schema(INT_SCHEMA)
        Draft202012Validator.check_schema(MAP_SCHEMA)

    def test_application_example_valid(self):
        self.assertValid(APP, self.load('examples/software-developer.seplico'))

    def test_evidence_mapping_example_valid(self):
        self.assertValid(MAP, self.load('examples/evidence-mapping.json'))

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

    def test_claim_ids_are_unique_in_example_application(self):
        doc = self.load('examples/software-developer.seplico')
        ids = application_claim_ids(doc)
        self.assertEqual(len(ids), len(set(ids)))

    def test_duplicate_claim_id_is_semantically_invalid(self):
        doc = self.load('examples/software-developer.seplico')
        doc['skills'][1]['claim_id'] = doc['skills'][0]['claim_id']
        ids = application_claim_ids(doc)
        self.assertNotEqual(len(ids), len(set(ids)))

    def test_evidence_references_resolve(self):
        doc = self.load('examples/software-developer.seplico')
        evidence_ids = {item['evidence_id'] for item in doc.get('evidence', [])}
        refs = {ref for skill in doc.get('skills', []) for ref in skill.get('evidence_refs', [])}
        self.assertTrue(refs.issubset(evidence_ids))

    def test_mapping_application_id_matches_example_application(self):
        doc = self.load('examples/software-developer.seplico')
        mapping = self.load('examples/evidence-mapping.json')
        self.assertEqual(mapping['application_id'], doc['application_id'])

    def test_mapping_claim_references_resolve(self):
        doc = self.load('examples/software-developer.seplico')
        mapping = self.load('examples/evidence-mapping.json')
        claim_ids = set(application_claim_ids(doc))
        refs = {item['claim_ref'] for item in mapping['mappings']}
        self.assertTrue(refs.issubset(claim_ids))

    def test_mapping_evidence_references_resolve(self):
        doc = self.load('examples/software-developer.seplico')
        mapping = self.load('examples/evidence-mapping.json')
        evidence_ids = {item['evidence_id'] for item in doc.get('evidence', [])}
        refs = {ref for item in mapping['mappings'] for ref in item.get('evidence_refs', [])}
        self.assertTrue(refs.issubset(evidence_ids))

    def test_mapping_does_not_accept_assessment_or_score(self):
        mapping = self.load('examples/evidence-mapping.json')
        mapping['mappings'][0]['assessment'] = 'meets'
        self.assertTrue(list(MAP.iter_errors(mapping)))
        mapping = self.load('examples/evidence-mapping.json')
        mapping['mappings'][0]['score'] = 0.95
        self.assertTrue(list(MAP.iter_errors(mapping)))

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
