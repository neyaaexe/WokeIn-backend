def fast_filter(sentences):
    return [
        s for s in sentences
        if len(s.split()) > 5 and any(c.isalpha() for c in s)
    ]


def skill_filter(sentences, skills):
    filtered = []
    for s in sentences:
        s_lower = s.lower()
        if any(skill in s_lower for skill in skills):
            filtered.append(s)
    return filtered
