import os
from config import DOCS_PATH


def load_documents():
    """Load all .txt documents from the documents folder."""
    documents = []
    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            source_name = filename.replace(".txt", "").replace("_", " ").title()
            documents.append({
                "source": source_name,
                "filename": filename,
                "text": text,
            })
    print(f"Loaded {len(documents)} document(s): {[d['source'] for d in documents]}")
    return documents


def clean_text(text):
    """Remove common Reddit copy-paste noise."""
    import re
    # collapse excessive whitespace/newlines
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    # strip share/vote/award boilerplate lines
    boilerplate = re.compile(
        r"^(share|save|hide|report|reply|give award|level \d|more replies"
        r"|posted by|view entire discussion|continue this thread"
        r"|u/[\w\-]+|[0-9]+ points?|[0-9]+ comments?)\s*$",
        re.IGNORECASE | re.MULTILINE,
    )
    text = boilerplate.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def chunk_document(text, source_name):
    """
    Split a document into overlapping character chunks.

    chunk_size = 400: captures a full Reddit comment or paragraph,
                      long enough to carry a complete tip.
    overlap    =  50: preserves context at boundaries so a tip split
                      across two chunks remains retrievable.
    min_length =  60: drops whitespace artifacts and very short fragments.
    """
    chunk_size = 400
    overlap = 50
    min_length = 60

    text = clean_text(text)
    chunks = []
    prefix = source_name.lower().replace(" ", "_")
    counter = 0
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end].strip()

        if len(chunk_text) >= min_length:
            chunks.append({
                "text": chunk_text,
                "source": source_name,
                "chunk_id": f"{prefix}_{counter}",
            })
            counter += 1

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    documents = load_documents()
    total = 0
    for doc in documents:
        chunks = chunk_document(doc["text"], doc["source"])
        total += len(chunks)
        print(f"  {doc['source']}: {len(chunks)} chunks")
        for chunk in chunks[:2]:
            print(f"    [{chunk['chunk_id']}] {chunk['text'][:80]}...")
    print(f"\nTotal chunks: {total}")
