def classify_comment(comment: str) -> str:
    comment = comment.lower()

    if any(k in comment for k in [
        "api", "endpoint", "auth", "authorization", "bearer",
        "header", "curl", "post", "request"
    ]):
        return "TECHNICAL"

    if any(k in comment for k in [
        "why", "philosophy", "conscious", "meaning", "ethics"
    ]):
        return "PHILOSOPHICAL"

    return "GENERAL"
