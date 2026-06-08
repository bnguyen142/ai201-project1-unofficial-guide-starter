# The Unofficial Guide — Project 1

---

## Domain

Supernote devices are eink devices that promises to replace paper notebooks while still retaining the writing experience. This is an unofficial guide on how to use the device and common mistakes. The official website covers basic setup and does a poor job explaining the concept behind each feature. The sources come from real users — reddit forums, youtube video and bloggers — who are passionate about the topic, share real world use of the device, and cover common pitfalls and how to get over them.

---

## Document Sources

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | r/Supernote — Rookie Mistakes thread | Reddit thread | https://www.reddit.com/r/Supernote/comments/1ieidi5/rookie_mistakes/ |
| 2 | Sheila Mac Adventures — Prepping Your Supernote | Blog post | https://www.sheilamacadventures.com/organization/prepsupernote |
| 3 | Sheila Mac Adventures — My Supernote Setup | Blog post | https://www.sheilamacadventures.com/organization/mysupernotesetup/ |
| 4 | Sheila Mac Adventures — Syncing Between Devices | Blog post | https://www.sheilamacadventures.com/howto/syncsupernote |
| 5 | Sheila Mac Adventures — Planning Workflow | Blog post | https://www.sheilamacadventures.com/snworkflows/planningsupernote |
| 6 | Sheila Mac Adventures — Mastering Digital Organization | Blog post | https://www.sheilamacadventures.com/organization/masteringdigitalorganization/ |
| 7 | Sheila Mac Adventures — Second Brain with Supernote | Blog post | https://www.sheilamacadventures.com/secondbrain/secondbrain1 |
| 8 | YouTube — "In-Depth Complete Guide to the Supernote Manta" | Video transcript | https://www.youtube.com/watch?v=N18W_4Xi_Ck |
| 9 | Sheila Mac Adventures — Studying with Supernote | Blog post | https://www.sheilamacadventures.com/snworkflows/studying1 |
| 10 | Sheila Mac Adventures — Manta User Experience | Blog post | https://www.sheilamacadventures.com/userexperience/manta |

---

## Chunking Strategy

**Chunk size:** 400 characters

**Overlap:** 50 characters

**Why these choices fit your documents:** My documents is a mix of short Reddit comments and structured blog tips — most individual tips fit within 300–400 characters. A 400-char chunk captures one complete thought without merging unrelated tips. The 50-char overlap ensures a tip that runs slightly past the boundary can still be retrieved from either chunk.

**Preprocessing:** Reddit copy-paste content included navigation boilerplate (subreddit links, vote counts, permalink text). A regex cleaning function stripped these before chunking. YouTube transcript was manually cleaned to remove timestamps, music markers, and filler words, then restructured into labeled sections.

**Final chunk count:** 72 chunks across 10 documents

### Sample Chunks

**Chunk 1** — Source: Rookie Mistakes
```
t notebook that you can use to test out any features you are unclear on -- easy way to
tool around and figure out the SN system in a low stakes environment.

Lastly, create a Jot Note and pin it to your quick access menu -- this is where you can
quickly add anything you would have scribbled on a napkin or sticky note.
```

**Chunk 2** — Source: Youtube Manta Guide
```
the previous generation. The screen is a plastic (Carter Mobius) screen, which is nicer
to write on than glass. No front light — seek out well-lit spaces. The gap between the
pen and the screen surface is reduced compared to the previous generation.

=== PEN & WRITING FEEL ===
Ceramic nibs on the Supernote never wear down and don't need replacing. The Heart of
Metal pen is recommended for most users.
```

**Chunk 3** — Source: Planning Workflow
```
e need to switch between analog and digital planning tools.

Routine Structure:
- Monthly planning: duplicate templates and set goals
- Weekly spreads: handle scheduling and habit tracking
- Daily pages: capture tasks and reflections

Review Process:
Conduct periodic reviews at week or month's end, marking completed items and archiving pages.
```

**Chunk 4** — Source: Digital Organization
```
folders. Instead, aim for a shallow hierarchy with only a few levels of nesting." Two
levels is usually enough on the Supernote.

3. Use Descriptive Naming
Apply clear, concise folder names that accurately describe their contents while avoiding
vague terminology. Avoid generic names like "Notes" or "Misc."

4. Archive Regularly
Review and archive outdated notes periodically to maintain a lean, efficient system.
```

**Chunk 5** — Source: Sync Supernote
```
ynced last and which device you are currently writing on" to prevent issues.

Additional cautions include:
- Don't open files on other devices while actively editing them elsewhere
- Watch for accidental page additions that occur when making changes to a file open in
  multiple locations simultaneously
- Such modifications cause "conflicting files when syncing"
```

---

## Embedding Model

**Model used:** all-MiniLM-L6-v2 via sentence-transformers

**Production tradeoff reflection:** If documents were a lot larger they will hit the higher context limit. Any document that needs a larger chunk size to capture the full idea — like a surgical SOP or long technical manual — may not be a good candidate for our current model. We would have to use a larger and probably not free model. The danger of not having a big enough context window is that some ideas will be cut off and not included in the embedding process, which ends with the answer not being complete. 
---

## Retrieval Test Results

**Query 1:** What is the most common mistake new Supernote users make with PDFs?

Top returned chunks:
- [rookie_mistakes_1] Source: Rookie Mistakes — *"Buying a lot of PDF planner/notebook documents to use BEFORE I had foundational knowledge of how the SN system works. Using said PDF's as a document vs. adding to 'mystyle' to use as a template..."*
- [rookie_mistakes_3] Source: Rookie Mistakes — *"You get the function of any of the embedded links on the PDF... Adding it as a template I keep that PLUS the notes 'bells & whistles' on top..."*

Why these chunks are relevant: Both chunks directly describe the PDF mistake and its fix. The first chunk is the original post describing the exact error. The second chunk explains what you gain by using PDFs as templates — keywords, headers, lasso-to-todo. Together they give a complete answer.

---

**Query 2:** What is the correct way to sync between two Supernote devices to avoid file conflicts?

Top returned chunks:
- [sync_supernote_1] Source: Sync Supernote — *"The recommended workflow involves alternating between devices: 1. Write on your first device (Nomad) 2. Sync that device completely 3. Once finished, sync your second device..."*
- [sync_supernote_2] Source: Sync Supernote — *"Don't open files on other devices while actively editing them elsewhere. Watch for accidental page additions that occur when making changes to a file open in multiple locations..."*

Why these chunks are relevant: The first chunk gives the step-by-step process. The second gives the cautions — what causes conflicts. Together they fully answer the question from the same source document.

---

**Query 3:** What is the Digest feature on the Supernote and how do you add something to it?

Top returned chunks:
- [youtube_manta_guide_8] Source: Youtube Manta Guide — *"Digest feature: add double square brackets around any handwritten text to send it to a global Digest. From anywhere on the device, you can access all your digested notes..."*

Why this chunk is relevant: This chunk comes directly from the YouTube guide's planning features section which explicitly describes the Digest mechanism step by step. The query and the chunk share the same vocabulary — "Digest feature" and "double square brackets."

---

## Grounded Generation

**System prompt grounding instruction:**

```
You are a helpful assistant for Supernote users, especially those interested in bullet
journaling (BuJo) on the Supernote.

Answer questions using ONLY the community tips and information provided in the context below.
Do not use any outside knowledge or general information you may have about the Supernote
or bullet journaling.

For every answer:
- Cite the source document(s) your answer draws from, like: (Source: <document name>)
- If multiple sources agree, cite all of them
- If the provided context does not contain enough information to answer the question,
  respond with exactly: "I don't have enough information on that in my sources.
  Try checking r/Supernote directly for more details."

Do not make up information or speculate beyond what the documents say.
```

**How source attribution is surfaced in the response:** The system prompt instructs the model to cite the source document name inline with every answer using the format `(Source: <document name>)`. This is enforced by instruction — the model is told explicitly to include it in every response, not left optional.

### Example Responses

**Example 1 — Accurate, grounded response:**

Query: *What is the most common mistake new Supernote users make with PDFs, and what is the correct approach?*

Response: *"The most common mistake new Supernote users make with PDFs is buying a lot of PDF planner/notebook documents to use BEFORE having foundational knowledge of how the SN system works, and then using them without utilizing the note features of the Supernote (Source: Rookie Mistakes). The correct approach is to convert PDFs to note files, which allows for the use of embedded links, keywords, headers, lasso to add to to-do, and note-to-note copy/paste, making the PDF a fully functional note file (Source: Rookie Mistakes). Converting PDF to PNG first may also save storage space before using as a template (Source: Rookie Mistakes)."*

---

**Example 2 — Grounded response with specific mechanism:**

Query: *What is the correct way to sync between two Supernote devices to avoid file conflicts?*

Response: *"The correct way to sync between two Supernote devices to avoid file conflicts involves alternating between devices and being mindful of which device was synced last and which device you are currently writing on (Source: Sync Supernote). Additional cautions include not opening files on other devices while actively editing them elsewhere and watching for accidental page additions that occur when making changes to a file open in multiple locations simultaneously (Source: Sync Supernote)."*

---

**Out-of-scope query — System refusal:**

Query: *Does the Supernote have a built-in AI assistant or ChatGPT integration?*

Response: *"No, the Supernote does not have AI features, including a built-in AI assistant or ChatGPT integration. This is intentional, as stated in the source documents. (Source: Youtube Manta Guide)"*

This is a grounded negative answer — the system found the relevant chunk (YouTube guide explicitly states "there are no AI features — this is intentional") and cited it rather than hallucinating or refusing.

---

## Evaluation Report

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What is the most common mistake new Supernote users make with PDFs, and what is the correct approach? | Load PDFs into MyStyle as a template to get full note features | Correct — buying PDFs without foundational knowledge, convert to note file for full features. Bonus tip: PNG saves storage. (Source: Rookie Mistakes) | Relevant | Accurate |
| 2 | The Supernote doesn't have a native zoom feature. What workaround do users recommend? | Lasso to resize + portrait/landscape flip | "I don't have enough information on that in my sources." — refusal | Off-target | Inaccurate |
| 3 | What is the correct way to sync between two Supernote devices to avoid file conflicts? | Alternate devices, sync fully before switching, never open same file on both | Correct — alternate devices, track which synced last, don't open files simultaneously. (Source: Sync Supernote) | Relevant | Accurate |
| 4 | What is the Digest feature on the Supernote and how do you add something to it? | Double square brackets → global Digest, accessible from anywhere | Correct on core mechanic. Missed: adding notes to entries and linking back to source. (Source: Youtube Manta Guide) | Relevant | Accurate |
| 5 | What folder structure do experienced Supernote users recommend for beginners? | Two main folders (Notes + Documents), shallow hierarchy | Got shallow hierarchy and consolidation right, missed the Notes/Documents two-folder structure from other sources | Partially relevant | Partially accurate |

---

## Failure Case Analysis

**Question that failed:** The Supernote doesn't have a native zoom feature. What workaround do users recommend?

**What the system returned:** "I don't have enough information on that in my sources. Try checking r/Supernote directly for more details."

**Root cause (tied to a specific pipeline stage):** This is a retrieval failure at the embedding stage. The answer exists in rookie_mistakes.txt — the lasso resize trick and the portrait-to-landscape flip are both documented there. The failure happened because the query used the words "zoom feature" and "workaround" while the chunk describes the technique as "lasso what you want to zoom on, make it larger" and "flip from portrait to landscape." The all-MiniLM-L6-v2 embedding model could not bridge that vocabulary gap — the semantic distance between the query and the relevant chunk was too high, so no confident match was returned and the system triggered its refusal response.

**What you would change to fix it:** Two options: (1) Increase chunk size so each chunk carries more semantic context — a larger chunk containing both the lasso tip and the landscape flip would have a higher chance of matching the query. (2) Rewrite the query to match the document vocabulary — "how do I get a closer view of my notes" or "how do I resize notes on Supernote" would likely surface the correct chunk.

---

## Query Interface

The interface is a Gradio chat UI running at `http://localhost:7860`. 

**Input:** A text box where the user types a plain-language question about using the Supernote. The user submits by pressing Enter or clicking the Submit button.

**Output:** A chat response in the conversation window. Every response includes the answer followed by inline source citations in the format `(Source: <document name>)`. If the system cannot find relevant information, it returns a refusal message directing the user to r/Supernote.

**Sample interaction transcript:**

> **User:** How do I set up a bullet journal on the Supernote?
>
> **System:** To set up a bullet journal on the Supernote, start by importing a yearly planner template as a PDF into Supernote, then duplicate it for yearly, monthly, weekly, and daily spreads (Source: Planning Workflow). Use daily log pages for rapid logging of tasks, events, and notes, and use headers and keywords to navigate quickly between spreads (Source: Planning Workflow). For organization, keep a single BuJo notebook rather than splitting spreads across multiple folders — a minimalist folder structure works best (Source: Digital Organization). You can also use the To-Do function to select any handwritten task and add it to your global to-do list, which is accessible from anywhere on the device (Source: Youtube Manta Guide).

---

## Spec Reflection

**One way the spec helped you during implementation:**
Having the chunk size (400 characters, 50 overlap) already decided in planning.md meant the code came back with the right values immediately when generating ingest.py. Without that starting point I would have spent time guessing or debugging the wrong thing — the spec kept me from getting bogged down before the pipeline was even running.

**One way your implementation diverged from the spec, and why:**
The Q2 evaluation question revealed a case where the chunk size was too small to capture the zoom workaround — the lasso trick and portrait/landscape flip lived in separate chunks and neither matched the query vocabulary. If I were to optimize, I'd increase the chunk size and re-test that question. That said, returning a refusal rather than a wrong answer was the right safety tradeoff for this system.
---

## AI Usage

**Instance 1**

- *What I gave the AI:* The chunking strategy section from planning.md and the document types (Reddit comments, blog posts, YouTube transcript). Asked Claude to implement ingest.py with load_documents(), a clean_text() function to strip Reddit navigation boilerplate, and chunk_document() using 400-character chunks with 50-character overlap.
- *What it produced:* A complete ingest.py with all three functions. The clean_text() function used regex to strip Reddit-specific patterns like "permalinkembedsave", vote counts, and navigation links.
- *What I changed or overrode:* Verified chunk count came out to 72 and inspected sample chunks visually to confirm each chunk was a self-contained thought. Also manually cleaned the YouTube transcript before ingestion since the raw copy-paste included timestamps and music markers the regex didn't catch.

**Instance 2**

- *What I gave the AI:* The pipeline diagram and grounding requirement — that answers must come only from retrieved context and every response must cite its source document.
- *What it produced:* generator.py with a system prompt enforcing grounding, and app.py with a Gradio chat interface matching the rulesbot structure.
- *What I changed or overrode:* Reviewed the system prompt to confirm it explicitly prohibited answers outside retrieved context rather than just suggesting it. Tested grounding by running an out-of-scope question (does Supernote have AI features) to verify the system cited the source rather than hallucinating or giving a generic answer.
