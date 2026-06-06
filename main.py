# from dotenv import load_dotenv
# from utils.audio_processor import process_input
# from core.transcriber import transcribe_all
# from core.sammrize import summarize, generate_title
# from core.extrator import extract_actionable_items, extract_key_decisions, extract_questions
# from core.rag_engine import build_rag_chain, load_rag_chain, ask_question

# load_dotenv()

# def run_pipeline(source:str, language:str = "en")->dict:
#     print("Processing audio...")
#     processed_audio = process_input(source)

#     print("Transcribing audio...")
#     transcript = transcribe_all(processed_audio, language)

#     print("Generating title...")
#     title = generate_title(transcript)

#     print("Generating summary...")
#     summary = summarize(transcript)

#     action_items = extract_actionable_items(transcript)
#     key_decisions = extract_key_decisions(transcript)
#     questions = extract_questions(transcript)
#     print("Building RAG chain...")

#     rag_chain = build_rag_chain(transcript) 

#     return {
#         "title": title,
#         "transcript": transcript,
#         "summary": summary,
#         "action_items": action_items,
#         "key_decisions": key_decisions,
#         "questions": questions,
#         "rag_chain": rag_chain  
#     }

# if __name__ == "__main__":
#     source = input("Enter the path to the audio file: ").strip()
#     language = input("Enter the language of the audio (default: en): ").strip() or "en"
#     results = run_pipeline(source, language)

#     print("\n--- Meeting Summary ---")
#     print("Title:", results["title"])
#     print("Summary:", results["summary"])
#     print("\n--- Actionable Items ---")
#     print(results["action_items"])
#     print("\n--- Key Decisions ---")
#     print(results["key_decisions"])
#     print("\n--- Questions ---")
#     print(results["questions"])
#     print("\nYou can now ask questions about the meeting using the RAG chain.")
#     rag_chain = results["rag_chain"]
#     while True:
#         question = input("\nEnter your question (or 'exit' to quit): ").strip()
#         if question.lower() == "exit":
#             print("Goodbye!")
#             break
#         if not question:
#             continue
#         answer = ask_question(rag_chain, question)
#         print("Answer:", answer)


from dotenv import load_dotenv
from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.sammrize import summarize, generate_title
from core.extrator import (
    extract_actionable_items,
    extract_key_decisions,
    extract_questions
)
from core.rag_engine import build_rag_chain, ask_question   # 🔥 FIX: load_rag_chain remove (unused)

load_dotenv()


def run_pipeline(source: str, language: str = "en") -> dict:
    print("Processing audio...")
    processed_audio = process_input(source)

    print("Transcribing audio...")
    transcript = transcribe_all(processed_audio, language)

    # 🔥 FIX 1: Add safety check (empty transcript crash prevention)
    if not transcript or len(transcript.strip()) == 0:
        raise ValueError("Transcript is empty. Audio processing failed.")

    print("Generating title...")
    title = generate_title(transcript)

    print("Generating summary...")
    summary = summarize(transcript)

    action_items = extract_actionable_items(transcript)
    key_decisions = extract_key_decisions(transcript)
    questions = extract_questions(transcript)

    print("Building RAG chain...")

    # 🔥 FIX 2: Try/except added (deployment safe)
    try:
        rag_chain = build_rag_chain(transcript)
    except Exception as e:
        print("RAG chain build failed:", str(e))
        rag_chain = None   # 🔥 prevents app crash on Streamlit

    return {
        "title": title,
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items,
        "key_decisions": key_decisions,
        "questions": questions,
        "rag_chain": rag_chain
    }


if __name__ == "__main__":
    source = input("Enter the path to the audio file: ").strip()
    language = input("Enter language (default: en): ").strip() or "en"

    results = run_pipeline(source, language)

    print("\n--- Meeting Summary ---")
    print("Title:", results["title"])
    print("Summary:", results["summary"])

    print("\n--- Actionable Items ---")
    print(results["action_items"])

    print("\n--- Key Decisions ---")
    print(results["key_decisions"])

    print("\n--- Questions ---")
    print(results["questions"])

    print("\nYou can now ask questions about the meeting using RAG.")

    rag_chain = results["rag_chain"]

    # 🔥 FIX 3: Safe RAG loop (deployment safe)
    if rag_chain is None:
        print("RAG is not available. Exiting question mode.")
    else:
        while True:
            question = input("\nEnter your question (or 'exit'): ").strip()

            if question.lower() == "exit":
                print("Goodbye!")
                break

            if not question:
                continue

            try:
                answer = ask_question(rag_chain, question)
                print("Answer:", answer)
            except Exception as e:
                print("Error answering question:", str(e))