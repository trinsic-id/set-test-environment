from unittest import TestCase

from main import eval_input

server_endpoint_inputs = """
'dev-internal.trinsic.cloud'
"dev-internal.trinsic.cloud"
[ 'dev-internal.trinsic.cloud',]
[ "dev-internal.trinsic.cloud" ]
[ "dev-internal.trinsic.cloud", "staging-internal.trinsic.cloud" ]
[ "", "dev-internal.trinsic.cloud" ]
"""

port_inputs = """
443
'443'
"443"
[ 443, 0]
[ "", 443]
"""


class TestEvaluateInput(TestCase):
    def test_eval_server_endpoint(self):
        for input_str in server_endpoint_inputs.split('\n'):
            if not input_str:
                continue
            with self.subTest(input_str):
                endpoint_str = eval_input(input_str)
                self.assertIsNotNone(endpoint_str)
                self.assertIsInstance(endpoint_str, str)
                self.assertEqual(endpoint_str, 'dev-internal.trinsic.cloud')

    def test_eval_server_port(self):
        for input_str in port_inputs.split('\n'):
            if not input_str:
                continue
            with self.subTest(input_str):
                endpoint_str = eval_input(input_str)
                self.assertIsNotNone(endpoint_str)
                self.assertIsInstance(endpoint_str, str)
                self.assertEqual(endpoint_str, '443')
