import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    """
    Add a transformer block and perform the following:
    - Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero.
    - Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    - Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    """
    # Specify your transformation logic here

    # print('Total data rows', data.sum())
    print('preprocessing, passenger_count:', data['passenger_count'].isin([0]).sum())
    print('preprocessing, trip_distance:', data['trip_distance'].isin([0]).sum())
    print('columns, before: ', data.columns)
    print('columns, after: ', data.columns
            .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
            .str.lower()
    )
    
    data = data[ data['passenger_count'] > 0]
    data = data[ data['trip_distance'] > 0]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    print(pd.to_datetime(data['lpep_pickup_datetime'], unit='s'))
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime'], unit='s') #.to_datetime()
    
    return data
    # return data[ data['passenger_count'] > 0]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passangers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance'
