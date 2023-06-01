def get_source_dict():
    return {
        "key1": "John",  # deep 0
        'key2': {
            'key3': 'Ann',  # deep 1
            'key4': {
                'key5': ['Kate', 'Mary'],  # deep 2
                'key6': {
                    'key7': [
                        'Bob',  # deep 3
                        'Duke',
                        {
                            'key8': {  # deep 4
                                'key9': [  # deep 5
                                    'Lisa',
                                    {
                                        'key10': ['Mark', 'Alex']  # deep 6
                                    }
                                ],
                                "key11": "Louisa",  # deep 5
                            }
                        },
                        "Alex",  # deep 3
                    ]
                },
            },
            'key12': 'Robert'  # deep 1
        },
        "key13": "Ronaldo"  # deep 0
    }


def recursive_search(our_dict, lookup_value, deep=0, parent=[]):
    for key, value in our_dict.items():
        if not isinstance(value, dict):
            if lookup_value == value:
                parent.append(key)
                print(lookup_value, parent, deep)
        else:
            deep += 1
            recursive_search(value, lookup_value, deep)
    return


recursive_search(get_source_dict(), 'Ann')
