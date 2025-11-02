"""Tools around flights using SerpApi."""

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

class FlightRequest(BaseModel):
    """Request model for flight search."""
    origin: str = Field(..., description="IATA code of the departure airport (e.g., 'JFK')")
    destination: str = Field(..., description="IATA code of the arrival airport (e.g., 'LHR')")
    outbound_date: str = Field(..., description="Departure date in 'YYYY-MM-DD' format")
    return_date: Optional[str] = Field(None, description="Return date in 'YYYY-MM-DD' format")
    adults: int = Field(1, description="Number of adult passengers")
    currency: str = Field("INR", description="Currency code for prices (e.g., 'USD')")


def search_flights(flight_request: FlightRequest):
    """Search flights"""
    params = {
        "engine": "google_flights",
        "departure_id": flight_request.origin.strip().upper(),
        "arrival_id": flight_request.origin.strip().upper(),
        "outbound_date": flight_request.outbound_date,
        "adults": flight_request.adults,
        "currency": flight_request.currency.strip().upper(),
    }
    if flight_request.return_date:
        params["return_date"] = flight_request.return_date

    try:
        search_results = run_search(params)
        return search_results
    except Exception as e:
        logging.exception("Error searching hotels: %s", str(e))
        return {"error": str(e)}
