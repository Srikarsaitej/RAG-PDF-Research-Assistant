SUMMARY_KEYWORDS = [
    "summarize",
    "summary",
    "overview",
    "brief",
    "abstract",
    "gist",
    "explain this document",
    "describe this document",
    "tell me about this document",
    "what is this document about",
]


def is_summary_request(question: str) -> bool:
    """
    Returns True if the user is asking for a summary.
    """

    question = question.lower()

    return any(keyword in question for keyword in SUMMARY_KEYWORDS)