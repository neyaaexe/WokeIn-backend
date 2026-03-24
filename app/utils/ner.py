from transformers import pipeline
import re

# HuggingFace NER pipeline

ner_pipeline = pipeline("ner", aggregation_strategy="simple") 

def extract_skills(text):
    """
    Extract skills and technologies from resume text
    """
    entities = ner_pipeline(text)
    skills = set()
    for e in entities:
        if e['entity_group'] in ["ORG", "MISC", "PER", "LOC"]:  # tweak depending on model
            skill = re.sub(r"[^a-zA-Z0-9#+]", "", e['word']).strip()
            if skill:
                skills.add(skill)
    return list(skills)