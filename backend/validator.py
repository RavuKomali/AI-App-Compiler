def validate_schema(schema):

    required_keys = [
        "ui_schema",
        "api_schema",
        "db_schema",
        "auth"
    ]

    missing = []

    for key in required_keys:
        if key not in schema:
            missing.append(key)

    if len(missing) == 0:
        return {
            "valid": True,
            "missing": []
        }

    return {
        "valid": False,
        "missing": missing
    }