from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

_client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """You are a helpful assistant for Supernote users, especially those interested in bullet journaling (BuJo) on the Supernote.

Answer questions using ONLY the community tips and information provided in the context below.
Do not use any outside knowledge or general information you may have about the Supernote or bullet journaling.

For every answer:
- Cite the source document(s) your answer draws from, like: (Source: <document name>)
- If multiple sources agree, cite all of them
- If the provided context does not contain enough information to answer the question, respond with exactly:
  "I don't have enough information on that in my sources. Try checking r/Supernote directly for more details."

Do not make up information or speculate beyond what the documents say."""


def generate_response(query, retrieved_chunks):
    """Generate a grounded answer from retrieved community tip chunks."""
    if not retrieved_chunks:
        return (
            "I don't have enough information on that in my sources. "
            "Try checking r/Supernote directly for more details."
        )

    context = ""
    for chunk in retrieved_chunks:
        context += f"Source: {chunk['source']}\n{chunk['text']}\n---\n"

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"},
    ]

    response = _client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
    )
    return response.choices[0].message.content
