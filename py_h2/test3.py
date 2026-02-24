document = "  URGENT_final_contract_v2.PDF  ".strip().lower()
if document.startswith("urgent") and document.endswith(".pdf") and "contract" in document:
    print("CRITICAL: Priority handling required!")
else:
    print("Normal document!")
