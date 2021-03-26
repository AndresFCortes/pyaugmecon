from tests.helper import Helper
import numpy as np
from tests.optimization_models import three_objective_model
from pyaugmecon import *

moop_opts = {
    'grid_points': 10,
    'early_exit': True,
    'bypass_coefficient': True,
    'maximize': False,
    }

solver_opts = {
    'solver_name': 'gurobi',
    'solver_io': 'python',
    }
 
py_augmecon = MOOP(
    three_objective_model(),
    moop_opts, solver_opts,
    'test_three_objectives',
    )


def test_payoff_table():
    payoff_table = np.array([
        [3075000, 62460, 33000],
        [3855000, 45180, 37000],
        [3225000, 55260, 23000]])
    assert Helper.array_equal(py_augmecon.payoff_table, payoff_table, 2)


def test_e_points():
    e_points = np.array([
        [45180, 47100, 49020, 50940, 52860, 54780, 56700, 58620, 60540, 62460],
        [23000, 24555.555556, 26111.111111, 27666.666667, 29222.222222,
            30777.777778, 32333.333333, 33888.888889, 35444.444444, 37000]])
    assert Helper.array_equal(py_augmecon.e, e_points, 2)


def test_pareto_sols():
    pareto_sols = np.array([
        [3075000, 62460, 33000],
        [3085000, 61980, 32333.33],
        [3108333.33, 60860, 30777.78],
        [3115000, 60540, 30333.33],
        [3131666.67, 59740, 29222.22],
        [3155000, 58620, 27666.67],
        [3178333.33, 57500, 26111.11],
        [3195000, 56700, 25000],
        [3201666.67, 56380, 24555.56],
        [3225000, 55260, 23000],
        [3255000, 54780, 23666.67],
        [3375000, 52860, 26333.33],
        [3495000, 50940, 29000],
        [3615000, 49020, 31666.67],
        [3735000, 47100, 34333.33],
        [3855000, 45180, 37000]])
    assert Helper.array_equal(py_augmecon.pareto_sols, pareto_sols, 2)