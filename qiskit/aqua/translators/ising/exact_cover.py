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

""" exact cover """

import logging
import warnings

import numpy as np

from qiskit.quantum_info import Pauli
from qiskit.aqua.operators import WeightedPauliOperator

logger = logging.getLogger(__name__)


def get_qubit_op(list_of_subsets):
    """Construct the Hamiltonian for the exact solver problem.

    Notes:
        Assumption: the union of the subsets contains all the elements to cover.
        The Hamiltonian is:
           sum_{each element e}{(1-sum_{every subset_i that contains e}{Xi})^2},
           where Xi (Xi=1 or 0) means whether should include the subset i.

    Args:
        list_of_subsets (list): list of lists (i.e., subsets)

    Returns:
        tuple(WeightedPauliOperator, float): operator for the Hamiltonian,
                            a constant shift for the obj function.
    """
    # pylint: disable=invalid-name
    n = len(list_of_subsets)

    U = []
    for sub in list_of_subsets:
        U.extend(sub)
    U = np.unique(U)   # U is the universe

    shift = 0
    pauli_list = []

    for e in U:
        # pylint: disable=simplifiable-if-expression
        cond = [True if e in sub else False for sub in list_of_subsets]
        indices_has_e = np.arange(n)[cond]
        num_has_e = len(indices_has_e)
        Y = 1-0.5*num_has_e
        shift += Y*Y

        for i in indices_has_e:
            for j in indices_has_e:
                if i != j:
                    w_p = np.zeros(n)
                    v_p = np.zeros(n)
                    v_p[i] = 1
                    v_p[j] = 1
                    pauli_list.append([0.25, Pauli(v_p, w_p)])
                else:
                    shift += 0.25

        for i in indices_has_e:
            w_p = np.zeros(n)
            v_p = np.zeros(n)
            v_p[i] = 1
            pauli_list.append([-Y, Pauli(v_p, w_p)])

    return WeightedPauliOperator(paulis=pauli_list), shift


def get_solution(x):
    """
    Args:
        x (numpy.ndarray) : binary string as numpy array.

    Returns:
        numpy.ndarray: graph solution as binary numpy array.
    """
    return 1 - x


def check_solution_satisfiability(sol, list_of_subsets):
    """ check solution satisfiability """
    # pylint: disable=invalid-name
    n = len(list_of_subsets)
    U = []
    for sub in list_of_subsets:
        U.extend(sub)
    U = np.unique(U)  # U is the universe

    U2 = []
    selected_subsets = []
    for i in range(n):
        if sol[i] == 1:
            selected_subsets.append(list_of_subsets[i])
            U2.extend(list_of_subsets[i])

    U2 = np.unique(U2)
    if set(U) != set(U2):
        return False

    tmplen = len(selected_subsets)
    for i in range(tmplen):
        for j in range(i):
            L = selected_subsets[i]
            R = selected_subsets[j]

            if set(L) & set(R):  # should be empty
                return False

    return True


def random_number_list(n, weight_range=100, savefile=None):
    """ random number list """
    from .common import random_number_list as redirect_func
    warnings.warn("random_number_list function has been moved to "
                  "qiskit.aqua.translators.ising.common, "
                  "the method here will be removed after Aqua 0.7+",
                  DeprecationWarning)
    return redirect_func(n=n, weight_range=weight_range, savefile=savefile)


def read_numbers_from_file(filename):
    """ read numbers from file """
    from .common import read_numbers_from_file as redirect_func
    warnings.warn("read_numbers_from_file function has been moved to "
                  "qiskit.aqua.translators.ising.common, "
                  "the method here will be removed after Aqua 0.7+",
                  DeprecationWarning)
    return redirect_func(filename)


def sample_most_likely(n=None, state_vector=None):
    """ sample most likely """
    from .common import sample_most_likely as redirect_func
    if n is not None:
        warnings.warn("n argument is not need and it will be removed after Aqua 0.7+",
                      DeprecationWarning)
    warnings.warn("sample_most_likely function has been moved to qiskit.aqua.ising.common, "
                  "the method here will be removed after Aqua 0.7+",
                  DeprecationWarning)
    return redirect_func(state_vector=state_vector)


def get_exact_cover_qubitops(list_of_subsets):
    """ get exact cover qubit ops """
    warnings.warn("get_exact_cover_qubitops function has been changed to get_qubit_op"
                  "the method here will be removed after Aqua 0.7+",
                  DeprecationWarning)
    return get_qubit_op(list_of_subsets)
