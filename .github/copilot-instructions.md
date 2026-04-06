---
description: "TechRescue project conventions: Python/Flask patterns, API response formats, chatbot behavior, and team standards."
applyTo: "**"
---

# TechRescue Project Guidelines

## Project Overview
TechRescue is a Flask-based chatbot that provides tech support for Windows and Linux systems using OpenAI's API.

**Structure**:
- `app.py` — Flask backend with routes and OpenAI integration
- `templates/` — Jinja2 HTML templates
- `static/` — CSS and static assets

---

## Code Conventions

### Python & Flask
- **Imports**: Group standard library, third-party, then local imports
- **Route naming**: Use lowercase with underscores (e.g., `/ask`, `/get-history`)
- **Error handling**: Wrap OpenAI API calls in try-except; return JSON error responses
- **Comments**: Use Bulgarian for user-facing strings, English for code documentation
- **Environment variables**: Load via `load_dotenv()`, never hardcode API keys

### OpenAI Integration
- **API calls**: Always check that `openai.api_key` is set before making requests
- **Response format**: Return JSON with `"response"` key containing the AI's message
- **Error handling**: Catch `openai.error.*` exceptions and return meaningful error messages
- **Prompt engineering**: Include OS context (Windows/Linux) to tailor responses

---

## API Response Format

All responses from Flask routes should return JSON:

```json
{
  "response": "The AI's message or result",
  "status": "success|error",
  "code": "optional_error_code"
}
```

### Example Success Response
```json
{
  "response": "Here's how to fix that Windows issue...",
  "status": "success"
}
```

### Example Error Response
```json
{
  "response": "API error: Could not connect to OpenAI",
  "status": "error",
  "code": "OPENAI_TIMEOUT"
}
```

---

## Chatbot Behavior

### OS Detection
- Receive `os` parameter from frontend (values: `windows`, `linux`)
- Tailor responses based on OS type
- Default to generic advice if OS is unknown

### Chat Context
- Currently, each message is independent (no session history)
- Future: Implement session-based conversation history

### Response Tone
- Professional, concise tech support
- Numbered steps for procedural guidance
- Links or file paths when relevant

---

## Testing Guidelines

- Test both Windows and Linux response paths
- Mock OpenAI API to avoid token usage during tests
- Validate JSON response structure
- Check error handling for network timeouts and invalid API keys

---

## Deployment Notes

- Environment variables required: `OPENAI_API_KEY`
- Use `debug=False` for production
- Validate all user inputs before passing to OpenAI
- Implement rate limiting on `/ask` endpoint for production

---

## Agent Assignment

| Task | Recommended Agent |
|------|-------------------|
| Flask routes, OpenAI integration, chatbot logic | Flask Debugger |
| HTML templates, CSS styling, UI/UX | Frontend Developer |
| Unit tests, test debugging, coverage | Testing Specialist |
| General coding questions | Default Agent |

