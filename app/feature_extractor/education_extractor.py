import re

DEGREES = ["bachelor", "master", "phd", "bsc", "msc", "mba", "diploma", "certificate"]

def extract_education(education_section):
    """Extract degrees and institutions."""
    degrees = []
    institutions = []
    if education_section:
        for line in education_section.split("\n"):
            if any(degree in line.lower() for degree in DEGREES):
                degrees.append(line.strip())
            elif "university" in line.lower() or "school" in line.lower():
                institutions.append(line.strip())
    return {"degrees": degrees, "institutions": institutions}
