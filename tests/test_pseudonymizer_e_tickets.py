import sys
from pathlib import Path

src_path = Path(__file__).parent.parent / "src/tspii"
sys.path.append(str(src_path))
import unittest
from tspii.reversible_anonymizers.reversible_anonymizer import ReversibleAnonymizer
from tspii.recognizers.recognizers import create_travel_specific_recognizers
from tspii.operators.faker_operators import create_fake_data_operators


class TestTravelSpecificPIIPseudonymization(unittest.TestCase):

    def setUp(self):
        # Initialize the CustomPseudonymizer before each test
        self.reversible_anonymizer = ReversibleAnonymizer()
        # Add custom recognizers and fake data generators
        for recognizer in create_travel_specific_recognizers():
            self.reversible_anonymizer.add_recognizer(recognizer)
        self.reversible_anonymizer.add_operators(create_fake_data_operators())

    def test_pseudonymize_e_ticket(self):
        document_content = "My e-ticket number is 123-4567890123."
        self.reversible_anonymizer.analyze(document_content)
        anonymized_content = self.reversible_anonymizer.anonymize()
        self.assertNotIn("123-4567890123", anonymized_content.text)

    def test_pseudonymize_e_ticket_(self):
        document_content = "My e-ticket number is 123-3049203039."
        self.reversible_anonymizer.analyze(document_content)
        anonymized_content = self.reversible_anonymizer.anonymize()
        self.assertNotIn("123-3049203039", anonymized_content.text)


if __name__ == "__main__":
    unittest.main()
