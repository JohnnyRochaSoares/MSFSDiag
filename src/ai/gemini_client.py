# ==== Imports ==== #
import json
from dataclasses import dataclass
import urllib.request
import urllib.error

# ==== AI Models ==== #
GEMINI_FLASH_LITE = "gemini-3.1-flash-lite"
GEMINI_FLASH      = "gemini-3.5-flash"

API_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"

# ==== Gemini Result Dataclass ==== #
@dataclass
class GeminiResult:
    success:  bool
    response: str
    error:    str = ""
       
# ==== Principal function ==== #
def ask_gemini(prompt: str, api_key: str, use_flash: bool = False) -> GeminiResult:

    if not use_flash:
        model = GEMINI_FLASH_LITE
    else:
        model = GEMINI_FLASH

    url = API_URL.format(model=model, key=api_key)

    payload = json.dumps({
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data    = payload,
        headers = {"Content-Type": "application/json"},
        method  = "POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            text = data["candidates"][0]["content"]["parts"][0]["text"]
            return GeminiResult(success=True, response=text, error="")
    except urllib.error.HTTPError as e:
        return GeminiResult(success=False, response="", error=e.read().decode("utf-8"))
    except Exception as e:
        return GeminiResult(success=False, response="", error=str(e))

