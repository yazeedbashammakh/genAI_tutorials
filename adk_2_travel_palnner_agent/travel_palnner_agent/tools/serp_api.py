"""Generic SerpAPI calling function."""

import os
import logging
from serpapi import GoogleSearch

SERPAPI_API_KEY = os.getenv("SERPAPI_KEY")

def run_search(params):
    """Generic function to run SerpAPI searches."""
    params["api_key"] = SERPAPI_API_KEY
    try:
        return GoogleSearch(params).get_dict()
    except Exception as e:
        logging.exception("SerpAPI search error: %s", str(e))
        raise e
