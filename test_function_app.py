"""
Unit tests for Azure Function App.

Tests the process_request and health_check functions following Azure Functions
testing best practices.
"""

import unittest
import json
from unittest.mock import Mock
import azure.functions as func
from function_app import process_request, health_check


class TestProcessRequest(unittest.TestCase):
    """Test cases for the process_request function."""
    
    def test_process_request_with_query_param(self):
        """Test process_request with name in query string."""
        # Arrange
        req = func.HttpRequest(
            method='GET',
            body=b'',
            url='/api/process',
            params={'name': 'John'}
        )
        
        # Act
        response = process_request(req)
        
        # Assert
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_body())
        self.assertEqual(response_data['status'], 'success')
        self.assertIn('John', response_data['message'])
        self.assertEqual(response_data['data']['name'], 'John')
    
    def test_process_request_with_json_body(self):
        """Test process_request with name in JSON body."""
        # Arrange
        body = json.dumps({'name': 'Alice'})
        req = func.HttpRequest(
            method='POST',
            body=body.encode('utf-8'),
            url='/api/process',
            params={}
        )
        
        # Act
        response = process_request(req)
        
        # Assert
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_body())
        self.assertEqual(response_data['status'], 'success')
        self.assertIn('Alice', response_data['message'])
    
    def test_process_request_missing_name(self):
        """Test process_request without name parameter."""
        # Arrange
        req = func.HttpRequest(
            method='GET',
            body=b'',
            url='/api/process',
            params={}
        )
        
        # Act
        response = process_request(req)
        
        # Assert
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_body())
        self.assertEqual(response_data['status'], 'error')
        self.assertEqual(response_data['error_code'], 'MISSING_PARAMETER')
    
    def test_process_request_empty_name(self):
        """Test process_request with empty name."""
        # Arrange
        req = func.HttpRequest(
            method='GET',
            body=b'',
            url='/api/process',
            params={'name': '   '}
        )
        
        # Act
        response = process_request(req)
        
        # Assert
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_body())
        self.assertEqual(response_data['status'], 'error')
        self.assertEqual(response_data['error_code'], 'EMPTY_NAME')
    
    def test_process_request_invalid_json(self):
        """Test process_request with invalid JSON in body."""
        # Arrange
        req = func.HttpRequest(
            method='POST',
            body=b'{invalid json}',
            url='/api/process',
            params={}
        )
        
        # Act
        response = process_request(req)
        
        # Assert
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_body())
        self.assertEqual(response_data['status'], 'error')


class TestHealthCheck(unittest.TestCase):
    """Test cases for the health_check function."""
    
    def test_health_check_returns_healthy(self):
        """Test health_check returns healthy status."""
        # Arrange
        req = func.HttpRequest(
            method='GET',
            body=b'',
            url='/api/health',
            params={}
        )
        
        # Act
        response = health_check(req)
        
        # Assert
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.get_body())
        self.assertEqual(response_data['status'], 'healthy')
        self.assertIn('version', response_data)


if __name__ == '__main__':
    unittest.main()
