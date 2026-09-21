import ollama

from rag_pipeline import retrieve_context


def analyze_claim(text):
    context = retrieve_context(text)

    prompt = f"""
You are CogniGuard, an AI misinformation risk analyzer.

Analyze the following claim:

CLAIM:
{text}

RETRIEVED KNOWLEDGE:
{context}

Provide your analysis in this format:

Risk Level: High Risk / Medium Risk / Low Risk / Needs Verification

Reason:
Explain briefly why the claim may require verification.

Evidence/Context:
Explain how the retrieved knowledge relates to the claim.

Warning Signals:
List important warning signals if present.

Verification Advice:
Explain what the user should verify and what type of reliable sources
could be useful.

Important rules:
- Do not automatically declare a claim true or false.
- Do not invent evidence or sources.
- If the available knowledge is insufficient, say that verification is needed.
- Use the retrieved knowledge as supporting context, not as absolute proof.
"""

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "risk": "AI + RAG Analysis",
        "reason": response["message"]["content"],
        "flags": []
    }