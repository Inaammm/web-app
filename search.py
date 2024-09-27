def search_keyword(text, query):
    """
    Search for the keyword in the extracted text.
    """
    if query.lower() in text.lower():
        return f"Keyword '{query}' found!"
    else:
        return f"Keyword '{query}' not found."
