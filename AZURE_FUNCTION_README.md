# Azure Function - HTTP Request Processor

## Overview

This Azure Function application processes HTTP requests and returns JSON responses. It implements Microsoft best practices for error handling, logging, and response formatting.

## Features

- **HTTP-Triggered Function**: Processes GET and POST requests
- **JSON Response Format**: Returns structured JSON responses
- **Error Handling**: Comprehensive error handling with try/except blocks
- **Input Validation**: Validates request parameters and body
- **Structured Logging**: Uses Azure Functions logging best practices
- **Health Check Endpoint**: Includes a health monitoring endpoint

## Endpoints

### 1. Process Request - `/api/process`

Processes HTTP requests and returns a personalized JSON response.

**Methods**: GET, POST

**Parameters**:
- `name` (string): Required parameter, can be passed via query string or JSON body

**Example Requests**:

```bash
# GET request with query parameter
curl "http://localhost:7071/api/process?name=John"

# POST request with JSON body
curl -X POST "http://localhost:7071/api/process" \
  -H "Content-Type: application/json" \
  -d '{"name": "John"}'
```

**Example Success Response** (200 OK):
```json
{
  "status": "success",
  "message": "Hello, John! Your request was processed successfully.",
  "data": {
    "name": "John",
    "method": "GET"
  }
}
```

**Example Error Response** (400 Bad Request):
```json
{
  "status": "error",
  "message": "Please provide a 'name' parameter in the query string or request body",
  "error_code": "MISSING_PARAMETER",
  "example": {
    "query": "?name=YourName",
    "body": {"name": "YourName"}
  }
}
```

### 2. Health Check - `/api/health`

Returns the health status of the function.

**Methods**: GET

**Example Request**:
```bash
curl "http://localhost:7071/api/health"
```

**Example Response** (200 OK):
```json
{
  "status": "healthy",
  "message": "Azure Function is running",
  "version": "1.0.0"
}
```

## Error Codes

The function returns the following error codes:

| Code | Description | HTTP Status |
|------|-------------|-------------|
| `MISSING_PARAMETER` | Required parameter not provided | 400 |
| `INVALID_INPUT_TYPE` | Parameter has wrong type | 400 |
| `EMPTY_NAME` | Name parameter is empty | 400 |
| `INTERNAL_ERROR` | Unexpected server error | 500 |

## Best Practices Implemented

### 1. Error Handling
- **Structured exception handling**: Uses try/except blocks at function level
- **Specific error catching**: Catches ValueError for JSON parsing
- **Graceful degradation**: Returns meaningful error messages
- **Error logging**: Logs errors with appropriate severity levels

### 2. Logging
- **Appropriate log levels**: Uses INFO, WARNING, and ERROR appropriately
- **Structured logging**: Includes context in log messages
- **Exception tracking**: Logs full exception details with `exc_info=True`
- **Application Insights integration**: Configured in host.json

### 3. Input Validation
- **Type checking**: Validates parameter types
- **Empty value checking**: Rejects empty strings
- **JSON parsing error handling**: Gracefully handles malformed JSON

### 4. Response Format
- **Consistent structure**: All responses follow same JSON structure
- **Proper MIME types**: Sets `application/json` content type
- **Appropriate HTTP status codes**: Uses standard status codes (200, 400, 500, 503)
- **Helpful error messages**: Provides clear guidance on what went wrong

## Local Development

### Prerequisites
- Python 3.9 or later
- Azure Functions Core Tools
- Azure Storage Emulator (Azurite) for local development

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Azure Functions Core Tools:
```bash
# On macOS
brew tap azure/functions
brew install azure-functions-core-tools@4

# On Windows
npm install -g azure-functions-core-tools@4 --unsafe-perm true

# On Linux
wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install azure-functions-core-tools-4
```

3. Run the function locally:
```bash
func start
```

The function will be available at `http://localhost:7071`.

### Testing

Test the function using curl or any HTTP client:

```bash
# Test success case
curl "http://localhost:7071/api/process?name=Alice"

# Test missing parameter
curl "http://localhost:7071/api/process"

# Test POST with JSON
curl -X POST "http://localhost:7071/api/process" \
  -H "Content-Type: application/json" \
  -d '{"name": "Bob"}'

# Test health check
curl "http://localhost:7071/api/health"
```

## Deployment to Azure

### Using Azure CLI

1. Create a resource group:
```bash
az group create --name myResourceGroup --location eastus
```

2. Create a storage account:
```bash
az storage account create \
  --name mystorageaccount \
  --resource-group myResourceGroup \
  --location eastus \
  --sku Standard_LRS
```

3. Create a function app:
```bash
az functionapp create \
  --resource-group myResourceGroup \
  --consumption-plan-location eastus \
  --runtime python \
  --runtime-version 3.9 \
  --functions-version 4 \
  --name myFunctionApp \
  --storage-account mystorageaccount \
  --os-type linux
```

4. Deploy the function:
```bash
func azure functionapp publish myFunctionApp
```

### Using VS Code

1. Install the Azure Functions extension
2. Sign in to Azure
3. Right-click on the function app in the Azure panel
4. Select "Deploy to Function App..."

## Monitoring

The function is configured to send telemetry to Application Insights:

- **Logs**: View in Azure Portal > Function App > Monitor > Logs
- **Metrics**: View in Azure Portal > Application Insights > Metrics
- **Live Metrics**: Real-time monitoring in Application Insights

## Configuration

### host.json
- Configures logging levels
- Sets up Application Insights sampling
- Specifies extension bundle version

### requirements.txt
- Lists Python dependencies
- Specifies azure-functions package version

### local.settings.json
- Contains local development settings
- Not deployed to Azure (use Application Settings in Azure Portal)

## Security Considerations

- **Authentication**: Currently set to `ANONYMOUS` for demo purposes
  - For production, consider using `FUNCTION` or `ADMIN` auth level
  - Implement Azure AD authentication for enterprise scenarios
- **Input validation**: All inputs are validated before processing
- **Error messages**: Don't expose sensitive information in error messages
- **HTTPS**: Always use HTTPS in production

## References

- [Azure Functions Python Developer Guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Azure Functions Error Handling](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-error-pages)
- [Monitor Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-monitoring)
- [Azure Functions Best Practices](https://learn.microsoft.com/en-us/azure/azure-functions/functions-best-practices)
