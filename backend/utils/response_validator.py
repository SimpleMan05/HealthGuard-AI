def validate_response(output):
    issues = []

    if "analysis" not in output:
        issues.append("Missing analysis section.")

    if "symptom" not in output or not output["symptom"]:
        issues.append("User symptom missing.")

    if "emergency_guideline" not in output:
        issues.append("Emergency guideline missing.")

    output["quality_report"] = {
        "is_valid": len(issues) == 0,
        "issues": issues
    }

    return output
