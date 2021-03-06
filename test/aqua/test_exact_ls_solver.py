# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" Test Exact LS solver """

import unittest
from test.aqua.common import QiskitAquaTestCase
import numpy as np
from qiskit.aqua import run_algorithm
from qiskit.aqua.input import LinearSystemInput
from qiskit.aqua.algorithms import ExactLSsolver


class TestExactLSsolver(QiskitAquaTestCase):
    """ Test Exact LS solver """
    def setUp(self):
        super().setUp()
        self.algo_input = LinearSystemInput()
        self.algo_input.matrix = [[1, 2], [2, 1]]
        self.algo_input.vector = [1, 2]

    def test_els_via_run_algorithm_full_dict(self):
        """ ELS Via Run Algorithm Full Dict test """
        params = {
            'algorithm': {
                'name': 'ExactLSsolver'
            },
            'problem': {
                'name': 'linear_system'
            },
            'input': {
                'name': 'LinearSystemInput',
                'matrix': self.algo_input.matrix,
                'vector': self.algo_input.vector
            }
        }
        result = run_algorithm(params)
        np.testing.assert_array_almost_equal(result['solution'], [1, 0])
        np.testing.assert_array_almost_equal(result['eigvals'], [3, -1])

    def test_els_via_run_algorithm(self):
        """ ELS Via Run Algorithm test """
        params = {
            'algorithm': {
                'name': 'ExactLSsolver'
            },
            'problem': {
                'name': 'linear_system'
            }
        }
        result = run_algorithm(params, self.algo_input)
        np.testing.assert_array_almost_equal(result['solution'], [1, 0])
        np.testing.assert_array_almost_equal(result['eigvals'], [3, -1])

    def test_els_direct(self):
        """ ELS Direct test """
        algo = ExactLSsolver(self.algo_input.matrix, self.algo_input.vector)
        result = algo.run()
        np.testing.assert_array_almost_equal(result['solution'], [1, 0])
        np.testing.assert_array_almost_equal(result['eigvals'], [3, -1])


if __name__ == '__main__':
    unittest.main()
