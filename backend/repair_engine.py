def repair_schema(schema):

    required_keys = [
        "ui_schema",
        "api_schema",
        "db_schema",
        "auth"
    ]

    for key in required_keys:
        if key not in schema:
            schema[key] = {}

    return schema