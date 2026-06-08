import gradio as gr
from ingest import load_documents, chunk_document
from retriever import embed_and_store, retrieve, get_collection
from generator import generate_response


def run_ingestion():
    collection = get_collection()

    if collection.count() > 0:
        print(f"Vector store already populated ({collection.count()} chunks). Skipping ingestion.")
        print("To re-ingest, delete ./chroma_db and restart.")
        return

    print("Ingesting documents...")
    documents = load_documents()
    all_chunks = []

    for doc in documents:
        chunks = chunk_document(doc["text"], doc["source"])
        all_chunks.extend(chunks)

    if all_chunks:
        embed_and_store(all_chunks)
        print(f"Ingestion complete. {len(all_chunks)} chunks stored.")
    else:
        print("\n⚠️  No chunks produced. Add .txt files to the documents/ folder.\n")


def chat(message, history):
    if not message.strip():
        return ""
    retrieved = retrieve(message)
    return generate_response(message, retrieved)


with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="violet"),
    title="Supernote Unofficial Guide",
) as demo:

    gr.HTML("""
        <div style="text-align:center; padding:1.25rem 0 0.5rem;">
            <h1 style="font-size:2rem; font-weight:700; color:#4c1d95; margin:0;">
                📓 Supernote Unofficial Guide
            </h1>
            <p style="color:#6b7280; font-size:1rem; margin:0.4rem 0 0;">
                Community tips for Supernote users — especially bullet journaling.
            </p>
        </div>
    """)

    with gr.Row():
        with gr.Column(scale=3):
            gr.ChatInterface(
                fn=chat,
                type="messages",
                chatbot=gr.Chatbot(
                    height=440,
                    type="messages",
                    placeholder=(
                        "<div style='text-align:center; color:#9ca3af; margin-top:3rem;'>"
                        "Ask anything about using your Supernote 📝"
                        "</div>"
                    ),
                ),
                textbox=gr.Textbox(
                    placeholder='e.g. "How do I set up a bullet journal on the Supernote?"',
                    container=False,
                    scale=7,
                ),
                examples=[
                    "How do I set up a bullet journal on the Supernote?",
                    "What templates work best for daily logs?",
                    "How do I convert handwriting to text?",
                    "What is the best way to sync my notes?",
                    "How does the Supernote compare to the reMarkable for BuJo?",
                    "How do I organize my notebooks?",
                    "What pen settings do people recommend?",
                ],
                cache_examples=False,
            )

        with gr.Column(scale=1, min_width=180):
            gr.HTML("""
                <div style="background:#f5f3ff; border:1px solid #ddd6fe;
                            border-radius:10px; padding:1rem; margin-top:0.5rem;">
                    <p style="font-size:0.8rem; font-weight:700; color:#4c1d95;
                               margin:0 0 0.5rem; letter-spacing:0.05em;">
                        📚 SOURCES
                    </p>
                    <p style="font-size:0.8rem; color:#5b21b6; margin:0; line-height:1.7;">
                        Answers are grounded in community posts from r/Supernote.
                        If a tip isn't in the sources, the system will say so.
                    </p>
                    <hr style="border:none; border-top:1px solid #ddd6fe; margin:0.75rem 0;">
                    <p style="font-size:0.75rem; color:#7c3aed; margin:0; line-height:1.5;">
                        All answers include a source citation so you know where the tip came from.
                    </p>
                </div>
            """)


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  Supernote Unofficial Guide — starting up")
    print("=" * 50 + "\n")
    run_ingestion()
    demo.launch()
