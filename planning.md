# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

Supernote devices are eink devices that promises to replace paper notebooks while still retaining the writing experience. We will go over unofficial guide how to use the device and common mistakes. This comes from reddit forums, youtube video and blogger all users from different angles. The official website covers basic setup and does a horrible job of the concept behind each feature. The sources provided is from real users who are passionate about the topic and execute real world use of the device and share common pitfalls and how to get over them.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | r/Supernote — Rookie Mistakes thread | Common beginner errors and how to avoid them | https://www.reddit.com/r/Supernote/comments/1ieidi5/rookie_mistakes/ — documents/rookie_mistakes.txt |
| 2 | Sheila Mac Adventures — Prepping Your Supernote | Three-phase setup guide for new users | https://www.sheilamacadventures.com/organization/prepsupernote — documents/prep_supernote.txt |
| 3 | Sheila Mac Adventures — My Supernote Setup | 5-year refined organization system with folders, Quick Access, and Digest | https://www.sheilamacadventures.com/organization/mysupernotesetup/ — documents/my_supernote_setup.txt |
| 4 | Sheila Mac Adventures — Syncing Between Devices | Step-by-step guide to syncing Nomad and Manta without conflicts | https://www.sheilamacadventures.com/howto/syncsupernote — documents/sync_supernote.txt |
| 5 | Sheila Mac Adventures — Planning Workflow | BuJo-style planning with Supernote and Apple Calendar sync | https://www.sheilamacadventures.com/snworkflows/planningsupernote — documents/planning_workflow.txt |
| 6 | Sheila Mac Adventures — Mastering Digital Organization | Minimalist folder strategy for Supernote users | https://www.sheilamacadventures.com/organization/masteringdigitalorganization/ — documents/digital_organization.txt |
| 7 | Sheila Mac Adventures — Second Brain with Supernote | P.A.R.A. and C.O.D.E. system implementation on Supernote | https://www.sheilamacadventures.com/secondbrain/secondbrain1 — documents/second_brain.txt |
| 8 | YouTube — "In-Depth Complete Guide to the Supernote Manta" | Full device review: writing feel, planning features, sync, sideloading, drawing | https://www.youtube.com/watch?v=N18W_4Xi_Ck — documents/youtube_manta_guide.txt |
| 9 | Sheila Mac Adventures — Studying with Supernote | Cornell template + layer system for active recall study workflow | https://www.sheilamacadventures.com/snworkflows/studying1 — documents/studying_workflow.txt |
| 10 | Sheila Mac Adventures — Manta User Experience | 3-week Europe travel review: portability, durability, folio tips | https://www.sheilamacadventures.com/userexperience/manta — documents/manta_user_experience.txt |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
400 characters
**Overlap:**
50 characters
**Reasoning:**
My documents is a mix of short Reddit comments and structured blog tips — most individual tips fit within 300–400 characters. A 400-char chunk captures one complete thought without merging unrelated tips. The 50-char overlap ensures a tip that runs slightly past the boundary can still be retrieved from either chunk. The result was 72 chunks across 10 documents, which is functional but on the lower end.
---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2 via sentence-transformers
**Top-k:**
5 chunks per query
**Production tradeoff reflection:**
If documents were a lot larger they will hit the higher context limit. also any document that needs a larger chunk size to get the idea like an SOP to surgery may not be a good candidate to use our current model. We would have to use a larger and probably not free model. The danger of not big enough will be that some of the ideas will be cut off and not be included in the embedding process which ends with the answer not being complete
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is the most common mistake new Supernote users make with PDFs, and what is the correct approach?  | New users load PDFs as documents instead of adding them to MyStyle as a note template — losing all note features like keywords, headers, and the ability to add pages|
| 2 | The Supernote doesn't have a native zoom feature. What workaround do users recommend?| Use the lasso tool to select and resize content larger to zoom in, or flip from portrait to landscape for a zoomed view |
| 3 |What is the correct way to sync between two Supernote devices to avoid file conflicts? | Alternate between devices — sync device 1 fully before switching to device 2, never open the same file on both simultaneously|
| 4 | What is the Digest feature on the Supernote and how do you add something to it?| Add double square brackets around any handwritten text to send it to a global Digest accessible from anywhere on the device|
| 5 | What folder structure do experienced Supernote users recommend for beginners?| Two main folders — Notes for active notebooks and Documents for archived PDFs — with a shallow hierarchy of no more than two levels|

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Conflicting advice could lead to confusing answer. RAG system has no way to resolve these conflicts so will present both and combine together into a mess of answer

2. If idea excceds the 400 character and 50 character overlap it may get cutoff. An example is that if a whole paragraph is building a satiricial point but the chunks cuts off beofore the punchline, the retrieve chunk is taken out of context. It will take the wrong main message of that paragrapth

---

## Architecture

documents/*.txt
      │
      ▼
[Document Ingestion — ingest.py]
  load_documents() reads all .txt files from documents/
      │
      ▼
[Chunking — ingest.py]
  chunk_document() splits into 400-char chunks, 50-char overlap
      │
      ▼
[Embedding + Vector Store — retriever.py]
  all-MiniLM-L6-v2 via sentence-transformers
  stored in ChromaDB (./chroma_db)
      │
      ▼
[Retrieval — retriever.py]
  retrieve() returns top-5 closest chunks by cosine similarity
      │
      ▼
[Generation — generator.py]
  Groq llama-3.3-70b-versatile
  grounded system prompt + source citation
      │
      ▼
[Interface — app.py]
  Gradio chat UI at localhost:7860

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
Claude helped with ingest.py.Gave Claude the chunking strategy section and document types as input. It help check that the default chunking straegy would work with the documenets and verified we had 72 chucnk count and print out samples to visually see how it looked
**Milestone 4 — Embedding and retrieval:**
Used Claude to discuss model chose, context limits, and chunk size fit. Confirm that 256 token context limit was not exceeded. Also confirm top retrieval result y running 3 queries and verifying that return chunks were relevent
**Milestone 5 — Generation and interface:**
Claude assisted with genrated gernator.py and app.py. Reviewed system prompt, grounding, and source citaiton . Check source to verify answer with each question asked. Also asked a total off the wall quesiton to see if it would try to answer as well as test if app was only answering from source and from no where else