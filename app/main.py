from input_pdf import process_resume
from section_identifiers import identify_sections
from feature_extractor import extract_skills, extract_education, extract_job_titles
from similarity_scorer import match_skills, match_education, match_job_titles, calculate_total_score
from job_description_parser import extract_skills as jd_extract_skills, extract_education as jd_extract_education, extract_jobs as jd_extract_jobs


def extract_features(sections):
    """Extract structured features from sections."""
    skills = extract_skills(sections.get("skills", ""), [sections.get("languages", "")])
    education = extract_education(sections.get("education", ""))
    job_titles = extract_job_titles(sections.get("experience", ""))
    return {
        "skills": skills,
        "education": education,
        "job_titles": job_titles
    }


def parse_job_description(jd_text):
    """Convert a plain job description into a structured format."""
    skills = jd_extract_skills(jd_text)
    education = jd_extract_education(jd_text)
    jobs = jd_extract_jobs(jd_text)
    return {
        "skills": skills,
        "education": education,
        "jobs": jobs
    }


def process_file(filepath, job_description):
    """Process resume, identify sections, extract features, and score relevance."""
    # Step 1: Extract raw text
    raw_text = process_resume(filepath)
    if not raw_text:
        return None

    # Step 2: Identify sections
    sections = identify_sections(raw_text)
    if not sections:
        return None

    # Step 3: Extract features
    features = extract_features(sections)

    # Step 4: Match features with job description
    skills_score = match_skills(features["skills"], job_description["skills"])
    education_score = match_education(features["education"], job_description["education"])
    job_score = match_job_titles(features["job_titles"], job_description["jobs"])

    # Step 5: Calculate total score
    total_score = calculate_total_score(skills_score, education_score, job_score)
    return sections, features, {
        "skills_score": skills_score,
        "education_score": education_score,
        "job_score": job_score,
        "total_score": total_score
    }


if __name__ == "__main__":
    # Input Resume
    filepath = "C:/Users/jesli/Downloads/Jeslin_Resume.pdf"  # Replace with actual file path

    # Input Job Description
    raw_job_description = """
    We are looking for a Python Developer with experience in TensorFlow and Django. 
    The candidate should have a Bachelor's or Master's degree in Computer Science.
    Experience as a Backend Developer is preferred.
    """

    # Parse job description into a structured format
    job_description = parse_job_description(raw_job_description)

    # Process resume and calculate scores
    result = process_file(filepath, job_description)

    if result:
        sections, features, scores = result

        # Print identified sections
        print("=== IDENTIFIED SECTIONS ===")
        for section, content in sections.items():
            print(f"\n=== {section.upper()} ===")
            print(content)

        # Print extracted features
        print("\n=== EXTRACTED FEATURES ===")
        print(features)

        # Print job description
        print("\n=== JOB DESCRIPTION ===")
        print(job_description)

        # Print scores
        print("\n=== MATCHING SCORES ===")
        print(scores)
    else:
        print("Failed to process the resume.")
