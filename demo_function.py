#!/usr/bin/env python3
"""
Demo script to demonstrate Azure Function behavior.

This script simulates HTTP requests to the Azure Function and displays
the JSON responses without requiring the Azure Functions runtime.
"""

import json
import azure.functions as func
from function_app import process_request, health_check


def print_response(title: str, response: func.HttpResponse):
    """Pretty print a function response."""
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.mimetype}")
    print("\nResponse Body:")
    try:
        body = json.loads(response.get_body())
        print(json.dumps(body, indent=2))
    except:
        print(response.get_body().decode('utf-8'))


def main():
    """Run demonstration of Azure Function."""
    print("\n" + "="*60)
    print("Azure Function HTTP Request Processor - Demo")
    print("="*60)
    
    # Test 1: Successful request with query parameter
    req1 = func.HttpRequest(
        method='GET',
        body=b'',
        url='/api/process',
        params={'name': 'John Doe'}
    )
    response1 = process_request(req1)
    print_response("Test 1: Successful GET request with query parameter", response1)
    
    # Test 2: Successful POST request with JSON body
    body2 = json.dumps({'name': 'Alice Smith'})
    req2 = func.HttpRequest(
        method='POST',
        body=body2.encode('utf-8'),
        url='/api/process',
        params={}
    )
    response2 = process_request(req2)
    print_response("Test 2: Successful POST request with JSON body", response2)
    
    # Test 3: Error - Missing parameter
    req3 = func.HttpRequest(
        method='GET',
        body=b'',
        url='/api/process',
        params={}
    )
    response3 = process_request(req3)
    print_response("Test 3: Error - Missing 'name' parameter", response3)
    
    # Test 4: Error - Empty name
    req4 = func.HttpRequest(
        method='GET',
        body=b'',
        url='/api/process',
        params={'name': '   '}
    )
    response4 = process_request(req4)
    print_response("Test 4: Error - Empty name parameter", response4)
    
    # Test 5: Invalid JSON in body
    req5 = func.HttpRequest(
        method='POST',
        body=b'{invalid json}',
        url='/api/process',
        params={}
    )
    response5 = process_request(req5)
    print_response("Test 5: Error - Invalid JSON in request body", response5)
    
    # Test 6: Health check endpoint
    req6 = func.HttpRequest(
        method='GET',
        body=b'',
        url='/api/health',
        params={}
    )
    response6 = health_check(req6)
    print_response("Test 6: Health check endpoint", response6)
    
    print("\n" + "="*60)
    print("Demo completed successfully!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
