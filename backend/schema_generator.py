def generate_schema(architecture):

    return {
        "ui_schema": {
            "pages": [
                "login",
                "dashboard",
                "contacts"
            ]
        },

        "api_schema": {
            "endpoints": [
                {
                    "path": "/login",
                    "method": "POST"
                },
                {
                    "path": "/contacts",
                    "method": "GET"
                }
            ]
        },

        "db_schema": {
            "tables": [
                "users",
                "contacts"
            ]
        },

        "auth": {
            "roles": [
                "admin",
                "user"
            ]
        }
    }