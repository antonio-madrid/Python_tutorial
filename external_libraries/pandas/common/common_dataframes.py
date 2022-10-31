import pandas as pd

df = pd.DataFrame(
    {
        'Column1': [
            'value1',
            'value2',
            'value3'
        ],
        'Column2': ''
    }
)

df_people = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

df_animals = pd.DataFrame(
    {
        'num_legs': [2, 4],
        'num_wings': [2, 0]
    },
    index=['falcon', 'dog'])

df_person = pd.DataFrame(
    {
        'name': ['Antonio'],
        'age': [33],
        'id': [
            {
                'number': [12345678],
                'expire_date': ['22-02-2024']
            }
        ]
    }
)
