"""
Azure Function App for HTTP request processing with JSON responses.

This module implements an HTTP-triggered Azure Function following Microsoft best practices
for error handling, logging, and JSON response formatting.
"""

import azure.functions as func
import logging
import json
from typing import Dict, Any

# Initialize the Function App
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="process", methods=["GET", "POST"])
def process_request(req: func.HttpRequest) -> func.HttpResponse:
    """
    Process HTTP requests and return JSON responses.
    
    This function demonstrates Microsoft best practices for Azure Functions:
    - Structured error handling with try/except blocks
    - Comprehensive logging at appropriate levels
    - Input validation
    - Proper JSON response formatting
    - HTTP status code handling
    
    Args:
        req (func.HttpRequest): The incoming HTTP request
        
    Returns:
        func.HttpResponse: JSON response with appropriate status code
    """
    logging.info('Python HTTP trigger function processing a request.')
    
    try:
        # Extract request parameters
        name = req.params.get('name')
        
        # Attempt to get JSON body if name not in query params
        if not name:
            try:
                req_body = req.get_json()
                name = req_body.get('name')
            except ValueError as ve:
                logging.warning(f'Invalid JSON in request body: {ve}')
                # If JSON parsing fails but name wasn't in query, it's okay
                pass
        
        # Validate input
        if name:
            if not isinstance(name, str):
                logging.error(f'Invalid input type for name: {type(name).__name__}')
                response_data = {
                    "status": "error",
                    "message": "Name must be a string",
                    "error_code": "INVALID_INPUT_TYPE"
                }
                return func.HttpResponse(
                    body=json.dumps(response_data),
                    mimetype="application/json",
                    status_code=400
                )
            
            if len(name.strip()) == 0:
                logging.warning('Empty name provided')
                response_data = {
                    "status": "error",
                    "message": "Name cannot be empty",
                    "error_code": "EMPTY_NAME"
                }
                return func.HttpResponse(
                    body=json.dumps(response_data),
                    mimetype="application/json",
                    status_code=400
                )
            
            # Success response
            logging.info(f'Successfully processed request for name: {name}')
            response_data = {
                "status": "success",
                "message": f"Hello, {name}! Your request was processed successfully.",
                "data": {
                    "name": name,
                    "method": req.method
                }
            }
            return func.HttpResponse(
                body=json.dumps(response_data),
                mimetype="application/json",
                status_code=200
            )
        else:
            # Missing parameter response
            logging.warning('Request received without name parameter')
            response_data = {
                "status": "error",
                "message": "Please provide a 'name' parameter in the query string or request body",
                "error_code": "MISSING_PARAMETER",
                "example": {
                    "query": "?name=YourName",
                    "body": {"name": "YourName"}
                }
            }
            return func.HttpResponse(
                body=json.dumps(response_data),
                mimetype="application/json",
                status_code=400
            )
            
    except Exception as e:
        # Catch-all for unexpected errors
        logging.error(f'Unexpected error occurred: {str(e)}', exc_info=True)
        response_data = {
            "status": "error",
            "message": "An unexpected error occurred while processing your request",
            "error_code": "INTERNAL_ERROR"
        }
        return func.HttpResponse(
            body=json.dumps(response_data),
            mimetype="application/json",
            status_code=500
        )


@app.route(route="health", methods=["GET"])
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    """
    Health check endpoint for monitoring.
    
    Args:
        req (func.HttpRequest): The incoming HTTP request
        
    Returns:
        func.HttpResponse: JSON response indicating health status
    """
    logging.info('Health check endpoint called')
    
    try:
        response_data = {
            "status": "healthy",
            "message": "Azure Function is running",
            "version": "1.0.0"
        }
        return func.HttpResponse(
            body=json.dumps(response_data),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        logging.error(f'Health check failed: {str(e)}', exc_info=True)
        response_data = {
            "status": "unhealthy",
            "message": "Health check failed"
        }
        return func.HttpResponse(
            body=json.dumps(response_data),
            mimetype="application/json",
            status_code=503
        )
