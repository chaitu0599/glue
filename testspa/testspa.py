import sys
import boto3

client = boto3.client('lakeformation')

response = client.add_lf_tags_to_resource(
    Resource={
        'TableWithColumns': {
            'DatabaseName': 'Default',
            'Name': 'sparkk',
            'ColumnNames': [
                'name'
            ]
            }
    },
    LFTags=[
        {
            'TagKey': 'owner',
            'TagValues': [
                'munipsai'
            ]
        },
    ]
)
