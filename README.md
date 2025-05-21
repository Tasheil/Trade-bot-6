# 📈 Forex Trade Assistant (FastAPI Version)

This app receives a forex chart (image) and news input, then uses GPT-4 Vision to return a trade suggestion.

## 🔧 Setup

1. Clone the repo and install requirements:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file based on `.env.example`:

```
OPENAI_API_KEY=sk-...
```

3. Run the server locally:

```bash
uvicorn main:app --reload
```

## 🚀 API Endpoint

**POST** `/analyze`

- `image`: forex chart (file)
- `news`: string describing news/headline

Returns:
```json
{
  "result": "Buy EUR/USD because..."
}
```
