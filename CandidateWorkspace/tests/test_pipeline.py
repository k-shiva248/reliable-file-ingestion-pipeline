import pandas as pd
import pytest


def validate_orders(df):

    if df.empty:
        raise ValueError("Input DataFrame is empty")

    required_columns = [
        "order_id",
        "customer_id",
        "product_id",
        "quantity",
        "unit_price",
        "order_status"
    ]

    missing = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError("Missing required columns")

    if df[required_columns].isnull().any().any():
        raise ValueError("Null values found")

    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order IDs")

    if (df["quantity"] <= 0).any():
        raise ValueError("Invalid quantity")

    if (df["unit_price"] <= 0).any():
        raise ValueError("Invalid price")

    allowed = ["Completed", "Pending", "Cancelled"]

    if not df["order_status"].isin(allowed).all():
        raise ValueError("Invalid order status")

    return True


@pytest.fixture
def valid_orders():
    return pd.DataFrame({
        "order_id": [1001, 1002],
        "customer_id": [1, 2],
        "product_id": [10, 20],
        "quantity": [2, 3],
        "unit_price": [100.0, 200.0],
        "order_status": ["Completed", "Pending"]
    })


def test_happy_path(valid_orders):
    assert validate_orders(valid_orders)


def test_empty_input(valid_orders):
    empty_df = valid_orders.iloc[0:0]

    with pytest.raises(ValueError, match="empty"):
        validate_orders(empty_df)


def test_duplicate_records(valid_orders):
    df = pd.concat(
        [valid_orders, valid_orders.iloc[[0]]],
        ignore_index=True
    )

    with pytest.raises(ValueError):
        validate_orders(df)


def test_missing_required_field(valid_orders):
    df = valid_orders.copy()
    df.loc[0, "customer_id"] = None

    with pytest.raises(ValueError):
        validate_orders(df)


def test_invalid_quantity(valid_orders):
    df = valid_orders.copy()
    df.loc[0, "quantity"] = -1

    with pytest.raises(ValueError):
        validate_orders(df)


def test_invalid_price(valid_orders):
    df = valid_orders.copy()
    df.loc[0, "unit_price"] = -100

    with pytest.raises(ValueError):
        validate_orders(df)


def test_invalid_status(valid_orders):
    df = valid_orders.copy()
    df.loc[0, "order_status"] = "Unknown"

    with pytest.raises(ValueError):
        validate_orders(df)


def test_malformed_schema(valid_orders):
    df = valid_orders.drop(columns=["customer_id"])

    with pytest.raises(ValueError):
        validate_orders(df)
