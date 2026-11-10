import pytest
from employee import Employee

@pytest.fixture
def employee():
    """Employee yang bisa dipakai di semua test."""
    return Employee('Budi', 'Santoso', 65000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 70000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 75000