DEGREES = ["bachelor", "master", "phd", "diploma", "certificate"]

def extract_education(jd_text):
    """Extract education requirements."""
    degrees = []
    for degree in DEGREES:
        if degree in jd_text.lower():
            degrees.append(degree)
    return {"degrees": degrees}
