# Example: Ask Copilot a Question

This example demonstrates how to use the Copilot Q&A workflow to get answers from GitHub Copilot CLI and commit them to your repository.

## How to Run

```bash
gh workflow run copilot-qa.yml \
  -f question="How do I implement rate limiting in Python using decorators?"
```

## What Happens

1. **Workflow Triggers**: The GitHub Action starts with your question
2. **Copilot CLI Executes**: Sends question to GitHub Copilot
3. **Response Generated**: Copilot provides a detailed answer
4. **Files Created**:
   - `response.md` - Latest answer (in root directory)
   - `responses/response_YYYYMMDD_HHMMSS.md` - Archived timestamped copy
5. **Committed to Repo**: Both files are automatically committed
6. **Artifact Available**: Response also available as downloadable artifact

## Example Questions

### Implementation Questions
```bash
gh workflow run copilot-qa.yml \
  -f question="How do I implement OAuth 2.0 authentication in Python?"
```

### Best Practices
```bash
gh workflow run copilot-qa.yml \
  -f question="What are the best practices for error handling in REST APIs?"
```

### Code Examples
```bash
gh workflow run copilot-qa.yml \
  -f question="Show me how to implement a simple caching system in Python"
```

### Architecture Advice
```bash
gh workflow run copilot-qa.yml \
  -f question="What's the best way to structure a microservices architecture with Python?"
```

## Expected Output

After running the workflow, you'll find:

### `response.md` (Root Directory)
```markdown
# Copilot Response

**Question:** How do I implement rate limiting in Python using decorators?

**Asked:** 2025-10-17 07:30:00 UTC

---

Here's how to implement rate limiting in Python using decorators:

[Detailed answer with code examples...]
```

### `responses/response_20251017_073000.md` (Archived)
Same content as above, but with a timestamp in the filename for historical tracking.

## Viewing Results

### In the Repository
- Check the latest commit for the new files
- Browse `response.md` for the latest answer
- Browse `responses/` directory for history

### Download Artifact
1. Go to Actions tab
2. Click on the workflow run
3. Download `copilot-response` artifact

### View in Workflow Summary
The workflow creates a summary with:
- Your question
- File locations
- Links to download artifacts

## Use Cases

- 📚 Build a knowledge base of technical Q&A
- 🎓 Learn best practices and patterns
- 💡 Get implementation guidance
- 🔍 Research architectural decisions
- 📝 Document team decisions with AI assistance

## Tips

- **Be Specific**: More detailed questions get better answers
- **Include Context**: Mention your tech stack or constraints
- **Ask Follow-ups**: Run multiple queries to dive deeper
- **Review Answers**: Always verify and test suggested code
- **Archive Important Answers**: The `responses/` directory keeps history
