import os
import sys
import json
import httpx
import requests
import base64
import urllib.parse
from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from kroger_api.kroger_api import KrogerAPI
from env import load_and_validate_env, get_zip_code

# Initialize FastMCP server
mcp = FastMCP('kroger')
load_and_validate_env(["KROGER_CLIENT_ID", "KROGER_CLIENT_SECRET"])
kroger = KrogerAPI()


print("Authenticating with Kroger API...")
token_info = kroger.authorization.get_token_with_client_credentials("product.compact")
print('token_info', token_info)
print(f"Authentication successful! Token expires in {token_info['expires_in']} seconds.")


# --- MCP Tools ---
@mcp.tool()
async def get_locaitons_by_zip_code(zipcode = "98001") -> str:
    #zip_code = get_zip_code(zipcode)
    try:
        locations = kroger.location.search_locations(
            zip_code = zipcode,
            radius_in_miles = 10,
            limit = 5
        )
        if locations and "data" in locations and locations["data"]:
                # Format the locations into a table
                table_data = ''
                for loc in locations["data"]:
                    address = loc["address"] if "address" in loc else {}
                    address_str = f"{address.get('addressLine1', '')}, {address.get('city', '')}, {address.get('state', '')} {address.get('zipCode', '')}"

                    table_data += address_str
        return {
            'success': True,
            'message': f"Found 5 Kroger store(s) in {zipcode}.",
            'stores': table_data
        }

    except Exception as e:
        return {
            'success': False,
            'error': f"An unexpected error occurred: {str(e)}"
        }

# --- Server Execution & Shutdown ---
async def shutdown_event():
    """Gracefully close the httpx client."""
    await http_client.aclose()
    # print("HTTP client closed.") # Optional print statement if desired


if __name__ == "__main__":
    mcp.run(transport="stdio")
