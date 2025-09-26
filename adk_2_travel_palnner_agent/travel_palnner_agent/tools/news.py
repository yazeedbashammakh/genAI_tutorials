"""Tools around flights using SerpApi."""

import logging

from .serp_api import run_search


def search_news(search_query: str):
    """Search news.
    Arguments:
        search_query: The news search query.
    """
    params = {
        "engine": "google_news",
        "q": search_query,
    }

    try:
        search_results = run_search(params)
        return search_results
    except Exception as e:
        logging.exception("Error searching news: %s", str(e))
        return {"error": str(e)}
