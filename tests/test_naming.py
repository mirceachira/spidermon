import pytest

from fixtures.naming import *


TEST_NAMES = [
    'UnnamedMonitor:A Test',
    'UnnamedMonitor:test_without_name',
    'Class Monitor:A Test',
    'Class Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
    'UnnamedMonitor:A Test',
    'UnnamedMonitor:test_without_name',
    'Class Monitor:A Test',
    'Class Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
    'UnnamedMonitor:A Test',
    'UnnamedMonitor:test_without_name',
    'Class Monitor:A Test',
    'Class Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
    'UnnamedMonitor:A Test',
    'UnnamedMonitor:test_without_name',
    'Class Monitor:A Test',
    'Class Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
]

TEST_MONITOR_NAMES = [
    'UnnamedMonitor',
    'UnnamedMonitor',
    'Class Monitor',
    'Class Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'UnnamedMonitor',
    'UnnamedMonitor',
    'Class Monitor',
    'Class Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'UnnamedMonitor',
    'UnnamedMonitor',
    'Class Monitor',
    'Class Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'UnnamedMonitor',
    'UnnamedMonitor',
    'Class Monitor',
    'Class Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'Instance Monitor',
    'Instance Monitor',
]

TEST_TEST_METHOD_NAMES = [
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
    'A Test',
    'test_without_name',
]

TEST_FULLNAME_NAMES_UNNNAMED_SUITE = [
    'UnnamedMonitor:A Test',
    'UnnamedMonitor:test_without_name',
    'Class Monitor:A Test',
    'Class Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
    'Instance Monitor:A Test',
    'Instance Monitor:test_without_name',
    'The Child Suite/UnnamedMonitor:A Test',
    'The Child Suite/UnnamedMonitor:test_without_name',
    'The Child Suite/Class Monitor:A Test',
    'The Child Suite/Class Monitor:test_without_name',
    'The Child Suite/Instance Monitor:A Test',
    'The Child Suite/Instance Monitor:test_without_name',
    'The Child Suite/Instance Monitor:A Test',
    'The Child Suite/Instance Monitor:test_without_name',
    'Instance Suite Name/UnnamedMonitor:A Test',
    'Instance Suite Name/UnnamedMonitor:test_without_name',
    'Instance Suite Name/Class Monitor:A Test',
    'Instance Suite Name/Class Monitor:test_without_name',
    'Instance Suite Name/Instance Monitor:A Test',
    'Instance Suite Name/Instance Monitor:test_without_name',
    'Instance Suite Name/Instance Monitor:A Test',
    'Instance Suite Name/Instance Monitor:test_without_name',
    'Instance Suite Name/UnnamedMonitor:A Test',
    'Instance Suite Name/UnnamedMonitor:test_without_name',
    'Instance Suite Name/Class Monitor:A Test',
    'Instance Suite Name/Class Monitor:test_without_name',
    'Instance Suite Name/Instance Monitor:A Test',
    'Instance Suite Name/Instance Monitor:test_without_name',
    'Instance Suite Name/Instance Monitor:A Test',
    'Instance Suite Name/Instance Monitor:test_without_name',
]

TEST_FULLNAME_NAMES_NAMED_SUITE = [
    'The Top Suite/UnnamedMonitor:A Test',
    'The Top Suite/UnnamedMonitor:test_without_name',
    'The Top Suite/Class Monitor:A Test',
    'The Top Suite/Class Monitor:test_without_name',
    'The Top Suite/Instance Monitor:A Test',
    'The Top Suite/Instance Monitor:test_without_name',
    'The Top Suite/Instance Monitor:A Test',
    'The Top Suite/Instance Monitor:test_without_name',
    'The Top Suite/The Child Suite/UnnamedMonitor:A Test',
    'The Top Suite/The Child Suite/UnnamedMonitor:test_without_name',
    'The Top Suite/The Child Suite/Class Monitor:A Test',
    'The Top Suite/The Child Suite/Class Monitor:test_without_name',
    'The Top Suite/The Child Suite/Instance Monitor:A Test',
    'The Top Suite/The Child Suite/Instance Monitor:test_without_name',
    'The Top Suite/The Child Suite/Instance Monitor:A Test',
    'The Top Suite/The Child Suite/Instance Monitor:test_without_name',
    'The Top Suite/Instance Suite Name/UnnamedMonitor:A Test',
    'The Top Suite/Instance Suite Name/UnnamedMonitor:test_without_name',
    'The Top Suite/Instance Suite Name/Class Monitor:A Test',
    'The Top Suite/Instance Suite Name/Class Monitor:test_without_name',
    'The Top Suite/Instance Suite Name/Instance Monitor:A Test',
    'The Top Suite/Instance Suite Name/Instance Monitor:test_without_name',
    'The Top Suite/Instance Suite Name/Instance Monitor:A Test',
    'The Top Suite/Instance Suite Name/Instance Monitor:test_without_name',
    'The Top Suite/Instance Suite Name/UnnamedMonitor:A Test',
    'The Top Suite/Instance Suite Name/UnnamedMonitor:test_without_name',
    'The Top Suite/Instance Suite Name/Class Monitor:A Test',
    'The Top Suite/Instance Suite Name/Class Monitor:test_without_name',
    'The Top Suite/Instance Suite Name/Instance Monitor:A Test',
    'The Top Suite/Instance Suite Name/Instance Monitor:test_without_name',
    'The Top Suite/Instance Suite Name/Instance Monitor:A Test',
    'The Top Suite/Instance Suite Name/Instance Monitor:test_without_name',
]


@pytest.fixture
def named_top_suite():
    return NamedTopSuite()

@pytest.fixture
def unnamed_top_suite():
    return UnnamedTopSuite()


def test_naming_test_names(named_top_suite, unnamed_top_suite):
    _check_names(
        generated_names=_generate_test_names(named_top_suite),
        expected_names=TEST_NAMES,
    )
    _check_names(
        generated_names=_generate_test_names(unnamed_top_suite),
        expected_names=TEST_NAMES,
    )


def test_naming_test_monitor_names(named_top_suite, unnamed_top_suite):
    _check_names(
        generated_names=_generate_test_monitor_names(named_top_suite),
        expected_names=TEST_MONITOR_NAMES,
    )
    _check_names(
        generated_names=_generate_test_monitor_names(unnamed_top_suite),
        expected_names=TEST_MONITOR_NAMES,
    )


def test_naming_test_test_method_names(named_top_suite, unnamed_top_suite):
    _check_names(
        generated_names=_generate_test_test_method_names(named_top_suite),
        expected_names=TEST_TEST_METHOD_NAMES,
    )
    _check_names(
        generated_names=_generate_test_test_method_names(unnamed_top_suite),
        expected_names=TEST_TEST_METHOD_NAMES,
    )


def test_naming_test_full_names(named_top_suite, unnamed_top_suite):
    _check_names(
        generated_names=_generate_test_full_names(named_top_suite),
        expected_names=TEST_FULLNAME_NAMES_NAMED_SUITE,
    )
    _check_names(
        generated_names=_generate_test_full_names(unnamed_top_suite),
        expected_names=TEST_FULLNAME_NAMES_UNNNAMED_SUITE,
    )


def _generate_test_names(suite):
    return [test.name for test in suite.all_tests]


def _generate_test_monitor_names(suite):
    return [test.monitor_name for test in suite.all_tests]


def _generate_test_test_method_names(suite):
    return [test.test_method_name for test in suite.all_tests]


def _generate_test_full_names(suite):
    return [test.full_name for test in suite.all_tests]


def _check_names(generated_names, expected_names):
    assert len(generated_names) == len(expected_names)
    for generated_name, expected_name in zip(generated_names, expected_names):
        assert generated_name == expected_name