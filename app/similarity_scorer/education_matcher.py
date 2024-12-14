def match_education(resume_education, jd_education):
    """Calculate education match score."""
    degrees = resume_education.get("degrees", [])
    institutions = resume_education.get("institutions", [])

    matched_degrees = [deg for deg in degrees if any(req in deg.lower() for req in jd_education.get("degrees", []))]
    match_score = len(matched_degrees) / len(jd_education.get("degrees", [])) if jd_education.get("degrees") else 1
    return round(match_score, 2)
