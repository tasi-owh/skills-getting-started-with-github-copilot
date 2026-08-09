from copy import deepcopy

from src import app as app_module

initial_activities = deepcopy(app_module.activities)


def reset_activities():
    app_module.activities.clear()
    app_module.activities.update(deepcopy(initial_activities))


def pytest_runtest_setup(item):
    reset_activities()
