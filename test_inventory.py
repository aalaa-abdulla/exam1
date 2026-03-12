"""
Exam 1 - Test Inventory Module
================================
Write your tests below. Each section (Part A through E) is marked.
Follow the instructions in each part carefully.

Run your tests with:
    pytest test_inventory.py -v

Run with coverage:
    pytest test_inventory.py --cov=inventory --cov-report=term-missing -v
"""

import pytest
from unittest.mock import patch
from inventory import (
    add_product,
    get_product,
    update_stock,
    calculate_total,
    apply_bulk_discount,
    list_products,
)


# ============================================================
# FIXTURE: Temporary inventory file (provided for you)
# This ensures each test gets a clean, isolated inventory.
# ============================================================

@pytest.fixture(autouse=True)
def clean_inventory(tmp_path, monkeypatch):
    """Use a temporary inventory file for each test."""
    db_file = str(tmp_path / "inventory.json")
    monkeypatch.setattr("inventory.INVENTORY_FILE", db_file)
    yield


# ============================================================
# PART A - Basic Assertions (18 marks)
# Write at least 8 tests using plain assert statements.
# Cover: add_product, get_product, update_stock,
#        calculate_total, and list_products.
# Follow the AAA pattern (Arrange, Act, Assert).
# ============================================================

# TODO: Write your Part A tests here

def test_add_product():
    product_id = "1"
    name = "laptop"
    price = 400
    stock = 1

    results = add_product(product_id, name, price, stock)

    assert results["product_id"] == "1"
    assert results["name"] == "laptop"
    assert results["price"] == 400
    assert results["stock"] == 1

def test_add_product_two():
        product_id = "2"
        name = "PC"
        price = 1000
        stock = 10

        results = add_product(product_id, name, price, stock)

        assert results["product_id"] == "2"
        assert results["name"] == "PC"
        assert results["price"] == 1000
        assert results["stock"] == 10

def test_add_product_three():
        product_id = "3"
        name = "phone"
        price = 500
        stock = 12

        results = add_product(product_id, name, price, stock)

        assert results["product_id"] == "3"
        assert results["name"] == "phone"
        assert results["price"] == 500
        assert results["stock"] == 12

def test_get_product():
    add_product("1", "laptop", 400, 1)
    results = get_product("1") 

    assert results["product_id"] == "1"
    assert results["name"] == "laptop"
    assert results["price"] == 400
    assert results["stock"] == 1

def test_get_prodcut_none():
    assert get_product("9") is None

def test_update_stock():
     add_product("1", "laptop", 400, 20)
     new = update_stock("1",5)
     assert new == 25 
     new = update_stock("1", -10)
     assert new == 15

def test_calculate_total():
    add_product("1", "laptop", 9.99, 20)
    sum = calculate_total("1", 3)
    assert sum == 29.97

def test_list_products():
    add_product("1", "laptop", 400, 15)
    add_product("2", "PC", 1000, 10)
    prod = list_products()
    assert len(prod) == 2

# ============================================================
# PART B - Exception Testing (12 marks)
# Write at least 6 tests using pytest.raises.
# Cover: empty name, negative price, duplicate product,
#        stock going below zero, product not found, etc.
# ============================================================

# TODO: Write your Part B tests here
def test_add_product_empty_ID():
     with pytest.raises(ValueError,  match="Product ID and name are required"):
          add_product("", "laptop", 400, 15)

def test_add_product_empty_name():
     with pytest.raises(ValueError,  match="Product ID and name are required"):
          add_product("1", "", 400, 15)

def test_add_product_neg_price():
     with pytest.raises(ValueError,  match="Price must be positive"):
          add_product("1", "laptop", -400, 15)

def test_add_product_doublicate():
     add_product("1", "laptop", 400, 15)
     with pytest.raises(ValueError,  match="Product '1' already exists"):
          add_product("1", "pc", 1000, 12)

def test_update_stock_neg_stock():
     add_product("1", "laptop", 400, 5)
     with pytest.raises(ValueError,  match="Stock cannot go below zero"):
          update_stock("1", -10)

def test_calculate_total_wrong_quantity():
      add_product("1", "laptop", 400, 15)
      with pytest.raises(ValueError,  match="Quantity must be positive"):
           calculate_total("1", -16)
# ============================================================
# PART C - Fixtures and Parametrize (10 marks)
#
# C1: Create a @pytest.fixture called "sample_products" that
#     adds 3 products to the inventory and returns their IDs.
#     Write 2 tests that use this fixture.
@pytest.fixture
def sample_products():
     add_product("1", "laptop", 999.99, 10)
     add_product("2", "PC", 29.99, 50)
     add_product("3", "phone", 79.99, 25)

     return ["1", "2", "3"]

def test_sample_product_list(sample_products):
    
     prod = sample_products
     assert len(prod) == 3

def test_calculate_total_sample_products(sample_products):
     sum = calculate_total(sample_products[1], 2)
     assert sum == 59.98    
#
# C2: Use @pytest.mark.parametrize to test apply_bulk_discount
#     with at least 5 different (total, quantity, expected) combos.
# ============================================================
# TODO: Write your Part C tests here
@pytest.mark.parametrize(
    "sum, quantity, expected_result",
    [
        (100, 5, 100),        
        (200, 10, 190),       
        (300, 25, 270),       
        (500, 50, 425),       
        (99.99, 12, 94.99),   
    ]
)
def test_apply_bulk_discount(sum, quantity, expected_result):
    result = apply_bulk_discount(sum, quantity)
    assert result == expected_result
# ============================================================
# PART D - Mocking (5 marks)
# Use @patch to mock _send_restock_alert.
# Write 2 tests:
#   1. Verify the alert IS called when stock drops below 5
#   2. Verify the alert is NOT called when stock stays >= 5
# ============================================================

# TODO: Write your Part D tests here


# ============================================================
# PART E - Coverage (5 marks)
# Run: pytest test_inventory.py --cov=inventory --cov-report=term-missing -v
# You must achieve 90%+ coverage on inventory.py.
# If lines are missed, add more tests above to cover them.
# ============================================================


# ============================================================
# BONUS (5 extra marks)
# 1. Add a function get_low_stock_products(threshold) to
#    inventory.py that returns all products with stock < threshold.
# 2. Write 3 parametrized tests for it below.
# ============================================================

# TODO: Write your bonus tests here (optional)
