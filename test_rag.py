from rag_pipeline import retrieve_context


query = "A medicine can cure every disease."

context = retrieve_context(query)

print("\n--- Retrieved Knowledge ---\n")
print(context)