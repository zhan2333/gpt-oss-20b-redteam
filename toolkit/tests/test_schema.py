import json, pathlib
def test_example_finding_json_has_minimal_fields():
    path = pathlib.Path(__file__).resolve().parents[2] / "findings" / "F1.example.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    for k in ["finding_id","title","category","severity","breadth","novelty","prompt_minimal"]:
        assert k in data, f"missing field: {k}"
