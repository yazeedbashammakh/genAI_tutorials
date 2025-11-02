

import os
import logging
from typing import Optional
from pydantic import BaseModel, Field

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


class HotelRequest(BaseModel):
    """Request model for hotel search."""
    location: str = Field(..., description="City or location to search hotels in (e.g., 'London')")
    check_in_date: str = Field(..., description="Check-in date in 'YYYY-MM-DD' format")
    check_out_date: str = Field(..., description="Check-out date in 'YYYY-MM-DD' format")
    adults: int = Field(1, description="Number of adult guests")
    rooms: int = Field(1, description="Number of rooms needed")
    currency: str = Field("INR", description="Currency code for prices (e.g., 'USD')")
    sort_by: Optional[str] = Field(None, description="Sort order (e.g., 'price', 'rating', 'distance')")


def search_hotels(hotel_request: HotelRequest):
    """Search hotels."""
    params = {
        "engine": "google_hotels",
        "q": hotel_request.location,
        "check_in_date": hotel_request.check_in_date,
        "check_out_date": hotel_request.check_out_date,
        "adults": hotel_request.adults,
        "rooms": hotel_request.rooms,
        "currency": hotel_request.currency,
    }
    if hotel_request.sort_by:
        params["sort_by"] = hotel_request.sort_by

    try:
        search_results = run_search(params)
        return search_results
    except Exception as e:
        logging.exception("Error searching hotels: %s", str(e))
        return {"error": str(e)}
