def normalize_skills(extracted_skills, skill_mapping):
    """Map extracted skills to canonical names."""
    normalized = []
    for skill in extracted_skills:
        normalized.append(skill_mapping.get(skill.lower(), skill))
    return normalized
