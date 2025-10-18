# GitHub Copilot in Actions - Usage Examples

This document provides practical examples of how to use both GitHub Copilot CLI Q&A and Copilot Coding Agent workflows.

## 🎯 Copilot Q&A Examples

### How to Run

```bash
gh workflow run copilot-qa.yml \
  -f question="How do I implement rate limiting in Python using decorators?"
```

### What Happens

1. **Workflow Triggers**: The GitHub Action starts with your question
2. **Copilot CLI Executes**: Sends question to GitHub Copilot
3. **Response Generated**: Copilot provides a detailed answer
4. **Files Created**:
   - `response.md` - Latest answer (in root directory)
   - `responses/response_YYYYMMDD_HHMMSS.md` - Archived timestamped copy
5. **Committed to Repo**: Both files are automatically committed to `copilot-responses` branch
6. **Artifact Available**: Response also available as downloadable artifact

### Example Questions

#### Implementation Questions
```bash
gh workflow run copilot-qa.yml \
  -f question="How do I implement OAuth 2.0 authentication in Python?"

gh workflow run copilot-qa.yml \
  -f question="How do I create a REST API in Python using Flask?"
```

#### Best Practices
```bash
gh workflow run copilot-qa.yml \
  -f question="What are the best practices for error handling in REST APIs?"

gh workflow run copilot-qa.yml \
  -f question="What are the essential security measures for a Python web application?"
```

#### Code Examples
```bash
gh workflow run copilot-qa.yml \
  -f question="Show me how to implement a simple caching system in Python"

gh workflow run copilot-qa.yml \
  -f question="How do I implement JWT authentication in Python?"
```

#### Architecture Advice
```bash
gh workflow run copilot-qa.yml \
  -f question="What's the best way to structure a microservices architecture with Python?"

gh workflow run copilot-qa.yml \
  -f question="How should I design a scalable database schema for an e-commerce application?"
```

## 🤖 Copilot Coding Agent Examples

### Prerequisites

Before using the Coding Agent, ensure you have:
- GitHub Copilot Business or Enterprise subscription
- Properly configured `COPILOT_OAUTH_TOKEN` secret (see setup options below)
- GitHub CLI 2.80.0+ in the runner environment

### Token Setup Options

#### OAuth Application (Recommended)
- ✅ Best security and scalability
- ✅ Application-specific permissions
- ✅ Better auditability and team workflows
- ✅ Independent of individual user accounts

#### Personal OAuth Token (Alternative)
- ⚠️ Use only when OAuth apps cannot be created
- ❌ Security risks: tied to personal account
- ❌ Limited scalability for team usage
- ❌ Actions appear under personal name
- ❌ Token expires with account changes

### How to Run

```bash
gh workflow run copilot-agent-task.yml \
  -f task_description="Create a function to sort arrays" \
  -f base_branch="main"
```

### What Happens

1. **Agent Analysis**: Copilot Agent analyzes your task and repository structure
2. **Implementation Planning**: Agent creates a plan for the requested changes
3. **Code Generation**: Agent writes code following best practices
4. **Branch Creation**: Agent creates a new branch with the implementation
5. **Pull Request**: Agent opens a PR with detailed description and changes
6. **Notification**: You receive notifications when ready for review

### Feature Development Examples

```bash
# Create utility functions
gh workflow run copilot-agent-task.yml \
  -f task_description="Create a Python module for data validation with email, phone number, and credit card validation functions"

# Implement API endpoints
gh workflow run copilot-agent-task.yml \
  -f task_description="Implement REST API endpoints for user management: registration, login, profile update, and password reset using Flask"

# Add authentication system
gh workflow run copilot-agent-task.yml \
  -f task_description="Add JWT-based authentication system with role-based access control and refresh token functionality"
```

### Bug Fixes and Improvements

```bash
# Fix performance issues
gh workflow run copilot-agent-task.yml \
  -f task_description="Optimize the existing database queries in the user service module to reduce response time"

# Security improvements
gh workflow run copilot-agent-task.yml \
  -f task_description="Add input validation and sanitization to all API endpoints to prevent SQL injection and XSS attacks"

# Code refactoring
gh workflow run copilot-agent-task.yml \
  -f task_description="Refactor the legacy payment processing code to follow modern Python patterns and add type hints"
```

### Testing and Quality

```bash
# Add comprehensive tests
gh workflow run copilot-agent-task.yml \
  -f task_description="Create comprehensive unit tests for the existing calculator module using pytest"

# Integration testing
gh workflow run copilot-agent-task.yml \
  -f task_description="Add integration tests for the API endpoints using pytest and test database setup"

# Code quality tools
gh workflow run copilot-agent-task.yml \
  -f task_description="Set up code quality tools including black formatter, flake8 linter, and pre-commit hooks"
```

## 🔄 Combined Workflow Pattern

### Research → Implementation

1. **Research Phase (Q&A)**: First, understand the approach
```bash
gh workflow run copilot-qa.yml \
  -f question="What are the best practices for implementing a caching layer in a Python web application? Include Redis integration and cache invalidation strategies."
```

2. **Implementation Phase (Agent)**: Then let the agent implement
```bash
gh workflow run copilot-agent-task.yml \
  -f task_description="Implement a Redis-based caching layer for the existing Flask API following best practices for cache invalidation and TTL management"
```

## 📊 Expected Output

### Q&A Response Format (`copilot-responses` branch)

```markdown
# Copilot Response

**Question:** How do I implement rate limiting in Python using decorators?

**Asked:** 2025-10-17 07:30:00 UTC

---

Here's how to implement rate limiting in Python using decorators:

[Detailed answer with code examples...]
```

### Coding Agent PR Format

The agent creates a pull request with detailed description:

```markdown
## 🤖 AI-Generated Feature

**Task:** Create a function to sort arrays
**Agent:** GitHub Copilot Coding Agent  
**Branch:** copilot-agent/sort-arrays-1729234567

### Changes Made
- Added `utils/sorting.py` with multiple sorting algorithms
- Implemented quicksort, mergesort, and heapsort functions
- Added comprehensive error handling and input validation
- Included docstrings and type hints
- Added unit tests in `tests/test_sorting.py`

### Testing
✅ All tests pass  
✅ Code follows project style guidelines  
✅ Documentation updated

**Ready for review!**
```

## 📝 Tips for Effective Usage

### For Q&A Workflow
- Be specific about your technology stack and context
- Ask for examples when appropriate
- Include your experience level (beginner/intermediate/advanced)
- Ask follow-up questions to dive deeper into topics

### For Coding Agent
- Provide clear, specific task descriptions
- Mention the programming language and frameworks you're using
- Specify expected file structure or naming conventions
- Include any constraints or requirements (performance, security, etc.)
- Reference existing code patterns when relevant

### General Best Practices
- Use Q&A for learning and understanding concepts
- Use Coding Agent for actual implementation work
- Review all generated code carefully before merging
- Combine both approaches for complex projects
- Maintain clear documentation of your AI-assisted development process

## 🔍 Viewing Results

### Q&A Results
```bash
# Check the copilot-responses branch
git checkout copilot-responses
git pull origin copilot-responses

# View latest response
cat response.md

# View archived responses
ls responses/
```

### Coding Agent Results
- Monitor workflow runs in GitHub Actions
- Check for PR notifications from the agent
- Review agent logs artifact if no PR is created
- Participate in the code review process

### Integration with Development
- Use Q&A responses as project documentation
- Create issues from agent PRs for tracking
- Link agent PRs to project milestones
- Use agent-generated code as starting points for further development

## 🎯 Use Cases

### Q&A Workflow
- 📚 Build a knowledge base of technical Q&A
- 🎓 Learn best practices and patterns
- 💡 Get implementation guidance
- 🔍 Research architectural decisions

### Coding Agent Workflow  
- 🚀 Rapid feature development
- 🐛 Automated bug fixes
- 🧪 Test suite generation
- 📖 Documentation creation
- ♻️ Code refactoring

### Combined Workflow
- 📋 Research → Implementation pipeline
- 🎯 Problem analysis → Solution delivery
- 🔄 Continuous learning and building
