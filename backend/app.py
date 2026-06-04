from intent_extractor import extract_intent
from architecture_designer import design_architecture
from schema_generator import generate_schema
from validator import validate_schema
from repair_engine import repair_schema

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/generate", methods=["POST"])
def generate():

    data = request.get_json()
    prompt = data.get("prompt", "")

    # Step 1 - Intent Extraction
    intent = extract_intent(prompt)

    # Step 2 - Architecture Design
    architecture = design_architecture(intent)

    # Step 3 - Schema Generation
    schema = generate_schema(architecture)

    # Step 4 - Validation
    validation_result = validate_schema(schema)

    # Step 5 - Repair if needed
    if validation_result is False:
        schema = repair_schema(schema)

    result = {
        "status": "success",
        "intent": intent,
        "architecture": architecture,
        "schema": schema
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)