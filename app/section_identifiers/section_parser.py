import re
from .regex_patterns import SECTION_PATTERNS

def identify_sections(text):
    """Identify and structure text into sections."""
    sections = {}
    lines = text.split("\n")
    
    current_section = None
    for line in lines:
        # Check if the line matches any section header
        for section, pattern in SECTION_PATTERNS.items():
            if re.search(pattern, line, re.IGNORECASE):
                current_section = section
                sections[current_section] = []
                break
        
        # Append lines to the current section
        if current_section:
            sections[current_section].append(line.strip())

    # Clean up sections
    for section, content in sections.items():
        sections[section] = "\n".join(content).strip()
    
    return sections
