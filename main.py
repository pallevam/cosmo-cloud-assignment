list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    # Merge the information from list_1 and list_2 into a single list
    merged_list = list({item["id"]: item for item in list_1 + list_2}.values())

    # Sort the merged list by the "id" key
    merged_list.sort(key=lambda item: item["id"])

    return merged_list


list_3 = merge_lists(list_1, list_2)
