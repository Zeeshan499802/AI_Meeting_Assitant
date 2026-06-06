# import streamlit as st
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # ── Page config (must be first Streamlit call) ────────────────────────────────
# st.set_page_config(
#     page_title="MeetMind · Meeting Intelligence",
#     page_icon="🎙️",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # ── Custom CSS ────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300&display=swap');

# /* ── Reset & Base ── */
# html, body, [class*="css"] {
#     font-family: 'DM Mono', monospace;
# }

# /* ── Background ── */
# .stApp {
#     background: #0a0a0f;
#     background-image:
#         radial-gradient(ellipse 80% 50% at 20% 10%, rgba(99,58,255,0.12) 0%, transparent 60%),
#         radial-gradient(ellipse 60% 40% at 80% 80%, rgba(0,210,180,0.08) 0%, transparent 55%);
# }

# /* ── Hide default Streamlit chrome ── */
# #MainMenu, footer, header { visibility: hidden; }
# .block-container { padding-top: 2rem; padding-bottom: 3rem; }

# /* ── Sidebar ── */
# [data-testid="stSidebar"] {
#     background: #0e0e16 !important;
#     border-right: 1px solid rgba(99,58,255,0.2);
# }
# [data-testid="stSidebar"] .stMarkdown p,
# [data-testid="stSidebar"] label { color: #a0a0c0 !important; }

# /* ── Hero header ── */
# .hero {
#     text-align: center;
#     padding: 2.5rem 1rem 1.5rem;
#     margin-bottom: 2rem;
# }
# .hero-badge {
#     display: inline-block;
#     background: rgba(99,58,255,0.15);
#     border: 1px solid rgba(99,58,255,0.35);
#     color: #a585ff;
#     font-size: 0.7rem;
#     letter-spacing: 0.2em;
#     text-transform: uppercase;
#     padding: 0.3rem 0.9rem;
#     border-radius: 100px;
#     margin-bottom: 1.2rem;
#     font-family: 'DM Mono', monospace;
# }
# .hero h1 {
#     font-family: 'Syne', sans-serif;
#     font-size: clamp(2.2rem, 5vw, 3.8rem);
#     font-weight: 800;
#     color: #f0f0ff;
#     line-height: 1.05;
#     margin: 0 0 0.6rem;
#     letter-spacing: -0.03em;
# }
# .hero h1 span {
#     background: linear-gradient(135deg, #a585ff 0%, #00d4b4 100%);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
# }
# .hero p {
#     color: #6b6b8a;
#     font-size: 0.9rem;
#     letter-spacing: 0.04em;
#     margin: 0;
# }

# /* ── Cards ── */
# .card {
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 16px;
#     padding: 1.5rem 1.6rem;
#     margin-bottom: 1.2rem;
#     position: relative;
#     overflow: hidden;
# }
# .card::before {
#     content: '';
#     position: absolute;
#     top: 0; left: 0; right: 0;
#     height: 1px;
#     background: linear-gradient(90deg, transparent, rgba(165,133,255,0.4), transparent);
# }
# .card-label {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.65rem;
#     letter-spacing: 0.18em;
#     text-transform: uppercase;
#     color: #a585ff;
#     margin-bottom: 0.7rem;
#     display: flex;
#     align-items: center;
#     gap: 0.5rem;
# }
# .card-label .dot {
#     width: 5px; height: 5px;
#     background: #a585ff;
#     border-radius: 50%;
#     display: inline-block;
# }
# .card-title {
#     font-family: 'Syne', sans-serif;
#     font-size: 1.6rem;
#     font-weight: 700;
#     color: #f0f0ff;
#     margin: 0;
#     letter-spacing: -0.02em;
# }
# .card-body {
#     color: #c0c0d8;
#     font-size: 0.88rem;
#     line-height: 1.8;
#     margin: 0;
# }

# /* ── List items (action items, decisions, questions) ── */
# .item-list {
#     list-style: none;
#     padding: 0; margin: 0;
# }
# .item-list li {
#     padding: 0.65rem 0.9rem;
#     margin-bottom: 0.5rem;
#     background: rgba(255,255,255,0.04);
#     border-radius: 8px;
#     border-left: 2px solid;
#     color: #c8c8e0;
#     font-size: 0.85rem;
#     line-height: 1.6;
# }
# .item-list.actions li  { border-color: #a585ff; }
# .item-list.decisions li { border-color: #00d4b4; }
# .item-list.questions li { border-color: #ff8c61; }

# /* ── Transcript box ── */
# .transcript-box {
#     background: #080810;
#     border: 1px solid rgba(255,255,255,0.06);
#     border-radius: 12px;
#     padding: 1.2rem 1.4rem;
#     font-family: 'DM Mono', monospace;
#     font-size: 0.8rem;
#     color: #8888aa;
#     line-height: 1.9;
#     max-height: 320px;
#     overflow-y: auto;
#     white-space: pre-wrap;
# }
# .transcript-box::-webkit-scrollbar { width: 4px; }
# .transcript-box::-webkit-scrollbar-track { background: transparent; }
# .transcript-box::-webkit-scrollbar-thumb { background: rgba(165,133,255,0.3); border-radius: 4px; }

# /* ── Status / progress ── */
# .status-row {
#     display: flex;
#     align-items: center;
#     gap: 0.7rem;
#     padding: 0.55rem 1rem;
#     background: rgba(255,255,255,0.03);
#     border-radius: 8px;
#     margin-bottom: 0.4rem;
#     font-size: 0.78rem;
#     color: #8888aa;
# }
# .status-row.done { color: #00d4b4; }
# .status-row.active { color: #a585ff; }
# .status-icon { font-size: 0.9rem; min-width: 1.2rem; }

# /* ── Q&A section ── */
# .qa-bubble {
#     padding: 0.9rem 1.1rem;
#     border-radius: 12px;
#     margin-bottom: 0.7rem;
#     font-size: 0.85rem;
#     line-height: 1.7;
# }
# .qa-bubble.user {
#     background: rgba(99,58,255,0.15);
#     border: 1px solid rgba(99,58,255,0.2);
#     color: #d0c8ff;
#     margin-left: 2rem;
# }
# .qa-bubble.assistant {
#     background: rgba(0,212,180,0.08);
#     border: 1px solid rgba(0,212,180,0.15);
#     color: #c0e8e4;
#     margin-right: 2rem;
# }
# .qa-label {
#     font-size: 0.62rem;
#     letter-spacing: 0.15em;
#     text-transform: uppercase;
#     opacity: 0.55;
#     margin-bottom: 0.3rem;
#     font-family: 'DM Mono', monospace;
# }

# /* ── Stat pills ── */
# .stats-row {
#     display: flex;
#     gap: 0.8rem;
#     flex-wrap: wrap;
#     margin-bottom: 1.5rem;
# }
# .stat-pill {
#     flex: 1;
#     min-width: 100px;
#     background: rgba(255,255,255,0.04);
#     border: 1px solid rgba(255,255,255,0.08);
#     border-radius: 12px;
#     padding: 0.9rem 1rem;
#     text-align: center;
# }
# .stat-pill .num {
#     font-family: 'Syne', sans-serif;
#     font-size: 1.8rem;
#     font-weight: 700;
#     color: #a585ff;
#     line-height: 1;
#     display: block;
# }
# .stat-pill .lbl {
#     font-size: 0.65rem;
#     letter-spacing: 0.12em;
#     text-transform: uppercase;
#     color: #5a5a7a;
#     margin-top: 0.3rem;
#     display: block;
# }

# /* ── Buttons ── */
# .stButton > button {
#     background: linear-gradient(135deg, #6340ff, #4a28cc) !important;
#     color: #fff !important;
#     border: none !important;
#     border-radius: 10px !important;
#     padding: 0.65rem 1.6rem !important;
#     font-family: 'Syne', sans-serif !important;
#     font-weight: 600 !important;
#     font-size: 0.9rem !important;
#     letter-spacing: 0.02em !important;
#     transition: all 0.2s ease !important;
#     box-shadow: 0 4px 20px rgba(99,58,255,0.3) !important;
# }
# .stButton > button:hover {
#     transform: translateY(-1px) !important;
#     box-shadow: 0 6px 28px rgba(99,58,255,0.45) !important;
# }

# /* ── Input fields ── */
# .stTextInput > div > div > input,
# .stSelectbox > div > div {
#     background: rgba(255,255,255,0.04) !important;
#     border: 1px solid rgba(255,255,255,0.1) !important;
#     border-radius: 10px !important;
#     color: #e0e0f0 !important;
#     font-family: 'DM Mono', monospace !important;
# }
# .stTextInput > div > div > input:focus {
#     border-color: rgba(99,58,255,0.5) !important;
#     box-shadow: 0 0 0 2px rgba(99,58,255,0.15) !important;
# }

# /* ── File uploader ── */
# [data-testid="stFileUploader"] {
#     background: rgba(255,255,255,0.02) !important;
#     border: 2px dashed rgba(99,58,255,0.25) !important;
#     border-radius: 14px !important;
#     transition: border-color 0.2s;
# }
# [data-testid="stFileUploader"]:hover {
#     border-color: rgba(99,58,255,0.5) !important;
# }

# /* ── Tabs ── */
# .stTabs [data-baseweb="tab-list"] {
#     background: transparent !important;
#     gap: 0.3rem;
# }
# .stTabs [data-baseweb="tab"] {
#     background: rgba(255,255,255,0.04) !important;
#     border-radius: 8px !important;
#     color: #6b6b8a !important;
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.8rem !important;
#     letter-spacing: 0.05em !important;
#     border: 1px solid rgba(255,255,255,0.06) !important;
#     padding: 0.4rem 1rem !important;
# }
# .stTabs [aria-selected="true"] {
#     background: rgba(99,58,255,0.2) !important;
#     color: #c8b8ff !important;
#     border-color: rgba(99,58,255,0.4) !important;
# }
# .stTabs [data-baseweb="tab-highlight"] { background: transparent !important; }

# /* ── Divider ── */
# hr { border-color: rgba(255,255,255,0.06) !important; }

# /* ── Spinner ── */
# .stSpinner { color: #a585ff !important; }

# /* ── Alerts ── */
# .stSuccess {
#     background: rgba(0,212,180,0.1) !important;
#     border: 1px solid rgba(0,212,180,0.2) !important;
#     border-radius: 10px !important;
#     color: #00d4b4 !important;
# }
# .stError {
#     background: rgba(255,80,80,0.08) !important;
#     border: 1px solid rgba(255,80,80,0.2) !important;
#     border-radius: 10px !important;
# }

# /* ── Scrollbar global ── */
# ::-webkit-scrollbar { width: 5px; height: 5px; }
# ::-webkit-scrollbar-track { background: transparent; }
# ::-webkit-scrollbar-thumb { background: rgba(99,58,255,0.25); border-radius: 10px; }
# </style>
# """, unsafe_allow_html=True)


# # ── Helpers ──────────────────────────────────────────────────────────────────

# def parse_list_output(raw) -> list[str]:
#     """Turn whatever the extractor returns into a clean Python list of strings."""
#     if isinstance(raw, list):
#         return [str(i).strip() for i in raw if str(i).strip()]
#     if isinstance(raw, str):
#         lines = [l.strip().lstrip("-•*·1234567890.)").strip()
#                  for l in raw.splitlines() if l.strip()]
#         return [l for l in lines if l]
#     return [str(raw)]


# def render_list_card(label: str, icon: str, items: list[str], css_cls: str, color: str):
#     dot_color = {"actions": "#a585ff", "decisions": "#00d4b4", "questions": "#ff8c61"}.get(css_cls, "#a585ff")
#     items_html = "".join(f"<li>{item}</li>" for item in items) if items else "<li>None found.</li>"
#     st.markdown(f"""
#     <div class="card">
#         <div class="card-label">
#             <span class="dot" style="background:{dot_color}"></span>{icon} &nbsp;{label}
#         </div>
#         <ul class="item-list {css_cls}">{items_html}</ul>
#     </div>""", unsafe_allow_html=True)


# def status_row(icon: str, label: str, state: str = "done"):
#     st.markdown(f'<div class="status-row {state}"><span class="status-icon">{icon}</span>{label}</div>',
#                 unsafe_allow_html=True)


# # ── Session state init ────────────────────────────────────────────────────────
# for key in ["results", "chat_history", "pipeline_ran"]:
#     if key not in st.session_state:
#         st.session_state[key] = None if key != "chat_history" else []
#         if key == "pipeline_ran":
#             st.session_state[key] = False


# # ── Sidebar ───────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("""
#     <div style="padding:1.2rem 0 0.5rem">
#         <p style="font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:700;
#                   color:#f0f0ff;margin:0;letter-spacing:-0.01em;">🎙️ MeetMind</p>
#         <p style="font-size:0.65rem;color:#444466;letter-spacing:0.12em;
#                   text-transform:uppercase;margin:0.1rem 0 0;">Meeting Intelligence</p>
#     </div>
#     <hr style="margin:1rem 0">
#     """, unsafe_allow_html=True)

#     st.markdown('<p style="font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#555577;">Input Mode</p>',
#                 unsafe_allow_html=True)
#     input_mode = st.radio("", ["Upload Audio File", "Enter File Path"], label_visibility="collapsed")

#     st.markdown('<hr style="margin:0.8rem 0">', unsafe_allow_html=True)
#     st.markdown('<p style="font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#555577;">Language</p>',
#                 unsafe_allow_html=True)
#     lang_map = {"English": "en", "Spanish": "es", "French": "fr",
#                  "German": "de", "Arabic": "ar", "Urdu": "ur", "Auto-detect": "auto"}
#     lang_display = st.selectbox("", list(lang_map.keys()), label_visibility="collapsed")
#     language = lang_map[lang_display]

#     st.markdown('<hr style="margin:0.8rem 0">', unsafe_allow_html=True)
#     if st.session_state.pipeline_ran:
#         st.markdown('<p style="font-size:0.7rem;color:#00d4b4;letter-spacing:0.08em;">✓ Pipeline complete</p>',
#                     unsafe_allow_html=True)
#         if st.button("↺ Reset", use_container_width=True):
#             for k in ["results", "chat_history", "pipeline_ran"]:
#                 st.session_state[k] = None if k != "chat_history" else []
#                 if k == "pipeline_ran":
#                     st.session_state[k] = False
#             st.rerun()


# # ── Hero ──────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero">
#     <div class="hero-badge">AI-Powered Meeting Intelligence</div>
#     <h1>Turn meetings into<br><span>actionable insight</span></h1>
#     <p>Upload an audio recording · Get transcript, summary, decisions & more · Ask anything</p>
# </div>
# """, unsafe_allow_html=True)


# # ── Input section ─────────────────────────────────────────────────────────────
# if not st.session_state.pipeline_ran:
#     col1, col2 = st.columns([2, 1], gap="large")

#     with col1:
#         source_path = None

#         if input_mode == "Upload Audio File":
#             uploaded = st.file_uploader(
#                 "Drop your audio file here",
#                 type=["mp3", "mp4", "wav", "m4a", "ogg", "flac", "webm"],
#                 help="Supports MP3, MP4, WAV, M4A, OGG, FLAC, WEBM"
#             )
#             if uploaded:
#                 save_dir = "/tmp/meetmind_uploads"
#                 os.makedirs(save_dir, exist_ok=True)
#                 save_path = os.path.join(save_dir, uploaded.name)
#                 with open(save_path, "wb") as f:
#                     f.write(uploaded.getbuffer())
#                 source_path = save_path
#                 st.markdown(f'<p style="font-size:0.75rem;color:#00d4b4;margin-top:0.4rem;">✓ Saved → <code>{save_path}</code></p>',
#                             unsafe_allow_html=True)
#         else:
#             source_path = st.text_input(
#                 "Audio file path",
#                 placeholder="/path/to/meeting.mp3",
#                 help="Absolute path to the audio file on disk"
#             )

#     with col2:
#         st.markdown("<div style='height:1.6rem'></div>", unsafe_allow_html=True)
#         run_btn = st.button("🚀 Analyse Meeting", use_container_width=True,
#                             disabled=(not source_path))

#     # ── Run pipeline ──────────────────────────────────────────────────────────
#     if run_btn and source_path:
#         progress_placeholder = st.empty()
#         with progress_placeholder.container():
#             st.markdown("### Processing…")

#         steps = [
#             ("🔊", "Processing audio input…"),
#             ("✍️",  "Transcribing with Whisper…"),
#             ("🏷️", "Generating title…"),
#             ("📝", "Summarising transcript…"),
#             ("⚡", "Extracting action items…"),
#             ("🗳️", "Extracting key decisions…"),
#             ("❓", "Extracting questions…"),
#             ("🔗", "Building RAG chain…"),
#         ]

#         status_area = st.empty()
#         completed = []

#         def redraw_status(current_idx):
#             with status_area.container():
#                 for i, (icon, label) in enumerate(steps):
#                     if i < current_idx:
#                         status_row(icon, label, "done")
#                     elif i == current_idx:
#                         status_row("⟳", label, "active")

#         try:
#             from utils.audio_processor import process_input
#             from core.transcriber import transcribe_all
#             from core.sammrize import summarize, generate_title
#             from core.extrator import extract_actionable_items, extract_key_decisions, extract_questions
#             from core.rag_engine import build_rag_chain

#             redraw_status(0)
#             processed_audio = process_input(source_path)

#             redraw_status(1)
#             transcript = transcribe_all(processed_audio, language)

#             redraw_status(2)
#             title = generate_title(transcript)

#             redraw_status(3)
#             summary = summarize(transcript)

#             redraw_status(4)
#             action_items = extract_actionable_items(transcript)

#             redraw_status(5)
#             key_decisions = extract_key_decisions(transcript)

#             redraw_status(6)
#             questions = extract_questions(transcript)

#             redraw_status(7)
#             rag_chain = build_rag_chain(transcript)

#             st.session_state.results = {
#                 "title": title,
#                 "transcript": transcript,
#                 "summary": summary,
#                 "action_items": parse_list_output(action_items),
#                 "key_decisions": parse_list_output(key_decisions),
#                 "questions": parse_list_output(questions),
#                 "rag_chain": rag_chain,
#             }
#             st.session_state.pipeline_ran = True
#             status_area.empty()
#             progress_placeholder.empty()
#             st.rerun()

#         except Exception as e:
#             st.error(f"**Pipeline error:** {e}")


# # ── Results ───────────────────────────────────────────────────────────────────
# if st.session_state.pipeline_ran and st.session_state.results:
#     r = st.session_state.results

#     # Title card
#     st.markdown(f"""
#     <div class="card">
#         <div class="card-label"><span class="dot"></span>Meeting Title</div>
#         <p class="card-title">{r['title']}</p>
#     </div>
#     """, unsafe_allow_html=True)

#     # Stats row
#     word_count = len(r["transcript"].split()) if r["transcript"] else 0
#     st.markdown(f"""
#     <div class="stats-row">
#         <div class="stat-pill"><span class="num">{len(r["action_items"])}</span><span class="lbl">Action Items</span></div>
#         <div class="stat-pill"><span class="num">{len(r["key_decisions"])}</span><span class="lbl">Decisions</span></div>
#         <div class="stat-pill"><span class="num">{len(r["questions"])}</span><span class="lbl">Questions</span></div>
#         <div class="stat-pill"><span class="num">{word_count:,}</span><span class="lbl">Words</span></div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Tabs
#     tab_summary, tab_actions, tab_transcript, tab_qa = st.tabs(
#         ["📝  Summary", "⚡  Extractions", "📄  Transcript", "💬  Ask Anything"]
#     )

#     # ── Summary tab ──────────────────────────────────────────────────────────
#     with tab_summary:
#         st.markdown(f"""
#         <div class="card">
#             <div class="card-label"><span class="dot"></span>Summary</div>
#             <p class="card-body">{r['summary']}</p>
#         </div>
#         """, unsafe_allow_html=True)

#     # ── Extractions tab ──────────────────────────────────────────────────────
#     with tab_actions:
#         col_a, col_b = st.columns(2, gap="medium")
#         with col_a:
#             render_list_card("Action Items", "⚡", r["action_items"], "actions", "#a585ff")
#             render_list_card("Questions Raised", "❓", r["questions"], "questions", "#ff8c61")
#         with col_b:
#             render_list_card("Key Decisions", "🗳️", r["key_decisions"], "decisions", "#00d4b4")

#     # ── Transcript tab ───────────────────────────────────────────────────────
#     with tab_transcript:
#         st.markdown("""
#         <div class="card">
#             <div class="card-label"><span class="dot" style="background:#5588ff"></span>Full Transcript</div>
#         </div>
#         """, unsafe_allow_html=True)
#         st.markdown(f'<div class="transcript-box">{r["transcript"]}</div>', unsafe_allow_html=True)
#         st.download_button(
#             "⬇  Download Transcript",
#             data=r["transcript"],
#             file_name="transcript.txt",
#             mime="text/plain",
#         )

#     # ── Q&A tab ──────────────────────────────────────────────────────────────
#     with tab_qa:
#         st.markdown("""
#         <div class="card" style="margin-bottom:1.4rem">
#             <div class="card-label"><span class="dot" style="background:#ff8c61"></span>RAG-Powered Q&A</div>
#             <p class="card-body" style="font-size:0.8rem">Ask anything about this meeting.
#             The AI answers strictly from the transcript.</p>
#         </div>
#         """, unsafe_allow_html=True)

#         # Chat history
#         for msg in st.session_state.chat_history:
#             if msg["role"] == "user":
#                 st.markdown(f"""
#                 <div class="qa-bubble user">
#                     <div class="qa-label">You</div>
#                     {msg["content"]}
#                 </div>""", unsafe_allow_html=True)
#             else:
#                 st.markdown(f"""
#                 <div class="qa-bubble assistant">
#                     <div class="qa-label">MeetMind</div>
#                     {msg["content"]}
#                 </div>""", unsafe_allow_html=True)

#         # Input row
#         q_col, btn_col = st.columns([5, 1], gap="small")
#         with q_col:
#             user_q = st.text_input("Question", placeholder="What was decided about the budget?",
#                                    label_visibility="collapsed", key="qa_input")
#         with btn_col:
#             ask_btn = st.button("Ask →", use_container_width=True)

#         if ask_btn and user_q.strip():
#             from core.rag_engine import ask_question
#             st.session_state.chat_history.append({"role": "user", "content": user_q.strip()})
#             with st.spinner("Thinking…"):
#                 answer = ask_question(r["rag_chain"], user_q.strip())
#             st.session_state.chat_history.append({"role": "assistant", "content": answer})
#             st.rerun()

#         if st.session_state.chat_history:
#             if st.button("Clear chat", key="clear_chat"):
#                 st.session_state.chat_history = []
#                 st.rerun()















import streamlit as st
import os
import re
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="MeetMind · Meeting Intelligence",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════════════════════
#  CSS + ANIMATIONS
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown(r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap');

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body,[class*="css"],.stApp{font-family:'Plus Jakarta Sans',sans-serif}
#MainMenu,footer,header,[data-testid="stToolbar"],[data-testid="collapsedControl"]{display:none!important}
.block-container{padding:0!important;max-width:100%!important}

/* ── AURORA BG ── */
.stApp{background:#060612;min-height:100vh;overflow-x:hidden}
.stApp::before{
  content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 80vw 60vh at 15% 10%, rgba(100,40,255,0.16) 0%,transparent 65%),
    radial-gradient(ellipse 60vw 50vh at 85% 5%,  rgba(0,180,255,0.11) 0%,transparent 60%),
    radial-gradient(ellipse 50vw 70vh at 55% 95%, rgba(255,50,180,0.09) 0%,transparent 60%),
    radial-gradient(ellipse 40vw 40vh at 5%  80%, rgba(0,255,150,0.06) 0%,transparent 55%);
  animation:aurora 20s ease-in-out infinite alternate;
}
@keyframes aurora{
  0%  {transform:scale(1)   rotate(0deg);opacity:1}
  50% {transform:scale(1.06)rotate(1.2deg);opacity:.88}
  100%{transform:scale(.97) rotate(-.8deg);opacity:.95}
}

/* ── MAIN WRAPPER ── */
.mm-wrap{max-width:1120px;margin:0 auto;padding:2rem 2rem 5rem;position:relative;z-index:1}

/* ── HERO ── */
.mm-hero{text-align:center;padding:3.5rem 1rem 2.5rem;animation:fadeUp .8s cubic-bezier(.22,1,.36,1) both}
@keyframes fadeUp{from{opacity:0;transform:translateY(36px)}to{opacity:1;transform:none}}
.mm-badge{
  display:inline-flex;align-items:center;gap:.45rem;
  background:rgba(100,40,255,.12);border:1px solid rgba(100,40,255,.35);
  color:#c0a0ff;font-size:.65rem;letter-spacing:.22em;text-transform:uppercase;
  padding:.32rem 1rem;border-radius:100px;margin-bottom:1.4rem;
  font-family:'JetBrains Mono',monospace;animation:fadeUp .8s .08s both;
}
.mm-badge-dot{width:6px;height:6px;background:#8855ff;border-radius:50%;animation:blink 2s ease-in-out infinite}
@keyframes blink{0%,100%{box-shadow:0 0 0 0 rgba(136,85,255,.7)}50%{box-shadow:0 0 0 6px rgba(136,85,255,0)}}
.mm-h1{
  font-family:'Syne',sans-serif;font-size:clamp(2.5rem,5.5vw,5rem);
  font-weight:800;color:#f0f0ff;line-height:1.0;letter-spacing:-.04em;
  margin-bottom:1rem;animation:fadeUp .8s .15s both;
}
.mm-h1 .g{
  background:linear-gradient(130deg,#a07cff 0%,#00cfff 45%,#ff45c5 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;background-size:200%;
  animation:gradMove 7s ease-in-out infinite alternate;
}
@keyframes gradMove{0%{background-position:0%}100%{background-position:100%}}
.mm-sub{color:rgba(150,150,200,.7);font-size:1rem;max-width:500px;margin:0 auto;line-height:1.7;animation:fadeUp .8s .22s both}

/* ── GLASS CARD ── */
.glass{
  background:rgba(255,255,255,.033);
  backdrop-filter:blur(20px) saturate(160%);
  -webkit-backdrop-filter:blur(20px) saturate(160%);
  border:1px solid rgba(255,255,255,.075);
  border-radius:20px;padding:1.8rem 2rem;
  position:relative;overflow:hidden;
  transition:border-color .3s,transform .3s,box-shadow .3s;
  animation:cardIn .65s cubic-bezier(.22,1,.36,1) both;
}
@keyframes cardIn{from{opacity:0;transform:translateY(22px) scale(.98)}to{opacity:1;transform:none}}
.glass::before{
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(150,110,255,.55),rgba(0,200,255,.4),transparent);
}
.glass:hover{border-color:rgba(100,40,255,.2);box-shadow:0 0 50px rgba(100,40,255,.07);transform:translateY(-2px)}

/* ── LABELS ── */
.lbl{
  font-family:'JetBrains Mono',monospace;font-size:.62rem;
  letter-spacing:.2em;text-transform:uppercase;color:#7a60bb;
  display:flex;align-items:center;gap:.5rem;margin-bottom:.85rem;
}
.lbl-bar{width:16px;height:2px;background:linear-gradient(90deg,#7b5fff,#00d4ff);border-radius:2px}

/* ── INPUT TABS (mode selector) ── */
.mode-tabs{display:flex;gap:.5rem;margin-bottom:1.4rem}
.mode-tab{
  flex:1;padding:.65rem 1rem;border-radius:12px;border:1.5px solid rgba(255,255,255,.08);
  background:rgba(255,255,255,.03);color:rgba(160,155,200,.55);
  font-size:.88rem;font-weight:600;text-align:center;cursor:pointer;
  transition:all .25s ease;font-family:'Plus Jakarta Sans',sans-serif;
}
.mode-tab.active{
  background:rgba(100,40,255,.15);border-color:rgba(100,40,255,.4);
  color:#c5aaff;box-shadow:0 0 20px rgba(100,40,255,.1);
}
.mode-tab:hover:not(.active){border-color:rgba(255,255,255,.15);color:rgba(180,175,220,.7)}

/* ── STREAMLIT WIDGET POLISH ── */
.stTextInput>div>div>input{
  background:rgba(255,255,255,.05)!important;
  border:1.5px solid rgba(255,255,255,.1)!important;
  border-radius:12px!important;color:#e8e8f8!important;
  font-family:'JetBrains Mono',monospace!important;
  font-size:.87rem!important;padding:.75rem 1rem!important;
  transition:all .25s ease!important;
}
.stTextInput>div>div>input:focus{
  border-color:rgba(120,80,255,.65)!important;
  box-shadow:0 0 0 3px rgba(120,80,255,.12),0 0 25px rgba(120,80,255,.07)!important;
  background:rgba(120,80,255,.06)!important;
}
.stTextInput>label{color:#7a60bb!important;font-size:.65rem!important;font-family:'JetBrains Mono',monospace!important;letter-spacing:.15em!important;text-transform:uppercase!important}

.stSelectbox>div>div{
  background:rgba(255,255,255,.05)!important;border:1.5px solid rgba(255,255,255,.1)!important;
  border-radius:12px!important;color:#e8e8f8!important;transition:all .25s!important;
}
.stSelectbox>div>div:focus-within{border-color:rgba(120,80,255,.6)!important;box-shadow:0 0 0 3px rgba(120,80,255,.12)!important}
.stSelectbox>label{color:#7a60bb!important;font-size:.65rem!important;font-family:'JetBrains Mono',monospace!important;letter-spacing:.15em!important;text-transform:uppercase!important}

[data-testid="stFileUploader"]{
  background:rgba(100,40,255,.04)!important;
  border:2px dashed rgba(100,40,255,.25)!important;
  border-radius:16px!important;transition:all .3s!important;
}
[data-testid="stFileUploader"]:hover{
  border-color:rgba(100,40,255,.55)!important;
  background:rgba(100,40,255,.08)!important;
  box-shadow:0 0 35px rgba(100,40,255,.08)!important;
}

/* ── PRIMARY BUTTON ── */
.stButton>button{
  background:linear-gradient(135deg,#7040ff 0%,#4820cc 100%)!important;
  color:#fff!important;border:none!important;border-radius:14px!important;
  padding:.82rem 2.2rem!important;font-family:'Syne',sans-serif!important;
  font-weight:700!important;font-size:.95rem!important;letter-spacing:.01em!important;
  width:100%!important;cursor:pointer!important;overflow:hidden!important;
  transition:all .3s cubic-bezier(.22,1,.36,1)!important;
  box-shadow:0 4px 28px rgba(112,64,255,.38)!important;
}
.stButton>button:hover{
  transform:translateY(-3px) scale(1.02)!important;
  box-shadow:0 12px 45px rgba(112,64,255,.52),0 0 70px rgba(112,64,255,.14)!important;
}
.stButton>button:active{transform:translateY(0) scale(.99)!important}
.stButton>button:disabled{
  background:rgba(255,255,255,.05)!important;color:rgba(255,255,255,.22)!important;
  box-shadow:none!important;transform:none!important;cursor:not-allowed!important;
}
.stDownloadButton>button{
  background:rgba(0,205,255,.09)!important;border:1px solid rgba(0,205,255,.28)!important;
  color:#00cdff!important;border-radius:10px!important;padding:.6rem 1.4rem!important;
  font-family:'Plus Jakarta Sans',sans-serif!important;font-weight:600!important;
  font-size:.85rem!important;transition:all .25s!important;
  box-shadow:none!important;width:auto!important;
}
.stDownloadButton>button:hover{background:rgba(0,205,255,.17)!important;box-shadow:0 0 22px rgba(0,205,255,.15)!important;transform:translateY(-1px)!important}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"]{
  background:rgba(255,255,255,.025)!important;border-radius:14px!important;
  border:1px solid rgba(255,255,255,.065)!important;padding:4px!important;gap:3px!important;
}
.stTabs [data-baseweb="tab"]{
  background:transparent!important;border-radius:10px!important;
  color:rgba(155,145,200,.55)!important;font-family:'Syne',sans-serif!important;
  font-size:.87rem!important;font-weight:600!important;
  border:none!important;padding:.55rem 1.3rem!important;transition:all .25s!important;
}
.stTabs [data-baseweb="tab"]:hover{color:rgba(200,180,255,.8)!important;background:rgba(100,40,255,.09)!important}
.stTabs [aria-selected="true"]{background:rgba(100,40,255,.18)!important;color:#d0b8ff!important;box-shadow:0 0 22px rgba(100,40,255,.14)!important}
.stTabs [data-baseweb="tab-highlight"]{display:none!important}
[data-testid="stTabsContent"]{padding-top:1.5rem!important;animation:fadeUp .4s cubic-bezier(.22,1,.36,1)}

/* ── STATS GRID ── */
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:.9rem;margin:1.4rem 0}
.stat-c{
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.065);
  border-radius:16px;padding:1.1rem 1rem;text-align:center;
  transition:all .3s;cursor:default;position:relative;overflow:hidden;
}
.stat-c::after{
  content:'';position:absolute;bottom:0;left:0;right:0;height:2px;
  background:var(--ac,linear-gradient(90deg,#7b5fff,#00d4ff));
  transform:scaleX(0);transition:transform .3s;
}
.stat-c:hover::after{transform:scaleX(1)}
.stat-c:hover{transform:translateY(-4px);border-color:rgba(100,40,255,.22);box-shadow:0 14px 40px rgba(0,0,0,.28)}
.stat-c:nth-child(1){--ac:linear-gradient(90deg,#7b5fff,#a07cff)}
.stat-c:nth-child(2){--ac:linear-gradient(90deg,#00d4ff,#00ffaa)}
.stat-c:nth-child(3){--ac:linear-gradient(90deg,#ff45c5,#ff8060)}
.stat-c:nth-child(4){--ac:linear-gradient(90deg,#00ffaa,#00d4ff)}
.stat-n{
  font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;line-height:1;
  background:linear-gradient(135deg,#a07cff,#00d4ff);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  display:block;margin-bottom:.25rem;
}
.stat-c:nth-child(2) .stat-n{background-image:linear-gradient(135deg,#00d4ff,#00ffaa)}
.stat-c:nth-child(3) .stat-n{background-image:linear-gradient(135deg,#ff45c5,#ff8060)}
.stat-c:nth-child(4) .stat-n{background-image:linear-gradient(135deg,#00ffaa,#a07cff)}
.stat-l{font-size:.63rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(130,120,180,.55);font-family:'JetBrains Mono',monospace}

/* ── TITLE CARD ── */
.title-card{
  background:linear-gradient(135deg,rgba(100,40,255,.1),rgba(0,200,255,.06));
  border:1px solid rgba(100,40,255,.22);border-radius:20px;
  padding:1.8rem 2.2rem;margin-bottom:1.4rem;position:relative;overflow:hidden;
}
.title-card::before{
  content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,#7040ff,#00cfff,#ff45c5);
  background-size:200% 100%;animation:shimmer 4s linear infinite;
}
@keyframes shimmer{0%{background-position:200%}100%{background-position:-200%}}
.title-ey{font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:#7a60bb;margin-bottom:.5rem}
.title-tx{font-family:'Syne',sans-serif;font-size:clamp(1.3rem,2.8vw,2rem);font-weight:700;color:#f0f0ff;line-height:1.2;letter-spacing:-.02em;word-break:break-word}

/* ── ITEM PILLS ── */
.item{
  display:flex;align-items:flex-start;gap:.7rem;
  padding:.8rem 1.1rem;margin-bottom:.5rem;
  background:rgba(255,255,255,.03);border-radius:12px;border-left:3px solid;
  font-size:.87rem;color:rgba(210,210,240,.82);line-height:1.65;
  word-break:break-word;white-space:pre-wrap;
  transition:all .22s;animation:itemIn .45s cubic-bezier(.22,1,.36,1) both;
}
@keyframes itemIn{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:none}}
.item:hover{background:rgba(255,255,255,.055);transform:translateX(5px)}
.item.ac{border-color:#8855ff}
.item.dc{border-color:#00d4ff}
.item.qc{border-color:#ff45c5}
.item-ic{font-size:.95rem;flex-shrink:0;margin-top:.1rem}

/* ── SUMMARY TEXT ── */
.sum-body{font-size:.93rem;color:rgba(210,208,242,.82);line-height:1.88;word-break:break-word;white-space:pre-wrap}

/* ── TRANSCRIPT BOX ── */
.tx-box{
  background:rgba(0,0,0,.32);border:1px solid rgba(255,255,255,.055);
  border-radius:14px;padding:1.5rem;max-height:420px;overflow-y:auto;
  font-family:'JetBrains Mono',monospace;font-size:.78rem;
  color:rgba(155,155,200,.72);line-height:1.95;
  word-break:break-word;white-space:pre-wrap;
}
.tx-box::-webkit-scrollbar{width:4px}
.tx-box::-webkit-scrollbar-thumb{background:rgba(100,40,255,.3);border-radius:4px}

/* ── CHAT ── */
.chat-scroll{max-height:440px;overflow-y:auto;padding-right:.4rem;margin-bottom:1.1rem}
.chat-scroll::-webkit-scrollbar{width:4px}
.chat-scroll::-webkit-scrollbar-thumb{background:rgba(100,40,255,.25);border-radius:4px}
.bubble{
  padding:.9rem 1.2rem;border-radius:16px;margin-bottom:.7rem;
  font-size:.88rem;line-height:1.72;word-break:break-word;white-space:pre-wrap;
  animation:bubIn .3s cubic-bezier(.22,1,.36,1);
}
@keyframes bubIn{from{opacity:0;transform:translateY(8px) scale(.97)}to{opacity:1;transform:none}}
.bubble.u{background:rgba(100,40,255,.13);border:1px solid rgba(100,40,255,.22);color:#d6c4ff;margin-left:2.5rem;border-bottom-right-radius:4px}
.bubble.b{background:rgba(0,200,255,.07);border:1px solid rgba(0,200,255,.15);color:#b5e5f0;margin-right:2.5rem;border-bottom-left-radius:4px}
.bm{font-family:'JetBrains Mono',monospace;font-size:.57rem;letter-spacing:.15em;text-transform:uppercase;opacity:.4;margin-bottom:.3rem}

/* ── PIPELINE STEPS ── */
.p-step{
  display:flex;align-items:center;gap:.8rem;padding:.6rem 1rem;
  border-radius:10px;margin-bottom:.38rem;font-size:.84rem;font-weight:500;
  transition:all .3s;
}
.p-step.done{background:rgba(0,255,150,.06);color:#00ffaa;border:1px solid rgba(0,255,150,.12)}
.p-step.active{background:rgba(100,40,255,.12);color:#c0a0ff;border:1px solid rgba(100,40,255,.26);animation:stepPulse 1.6s ease-in-out infinite}
.p-step.pending{background:rgba(255,255,255,.02);color:rgba(130,120,180,.4);border:1px solid rgba(255,255,255,.04)}
@keyframes stepPulse{0%,100%{box-shadow:0 0 0 0 rgba(100,40,255,.2)}50%{box-shadow:0 0 0 7px rgba(100,40,255,0)}}
.p-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0}
.done .p-dot{background:#00ffaa}
.active .p-dot{background:#a07cff;animation:dotRot 1s linear infinite;border-radius:2px}
@keyframes dotRot{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}
.pending .p-dot{background:rgba(130,120,180,.22)}

/* ── SECTION HEAD ── */
.sh{
  font-family:'Syne',sans-serif;font-size:1.1rem;font-weight:700;
  color:#e8e4ff;letter-spacing:-.01em;margin-bottom:.9rem;
  display:flex;align-items:center;gap:.5rem;
}
.sh::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,rgba(100,40,255,.3),transparent);margin-left:.5rem}

/* ── EMPTY ── */
.empty{text-align:center;padding:2rem 1rem;color:rgba(130,120,180,.4);font-size:.82rem;font-family:'JetBrains Mono',monospace}
.empty .ei{font-size:1.8rem;margin-bottom:.45rem}

/* ── SUCCESS / ERROR / INFO ── */
.stSuccess{background:rgba(0,255,150,.07)!important;border:1px solid rgba(0,255,150,.2)!important;border-radius:12px!important;color:#00ffaa!important}
.stError{background:rgba(255,55,55,.07)!important;border:1px solid rgba(255,55,55,.2)!important;border-radius:12px!important}
.stInfo{background:rgba(0,180,255,.07)!important;border:1px solid rgba(0,180,255,.2)!important;border-radius:12px!important}
.stWarning{background:rgba(255,180,0,.07)!important;border:1px solid rgba(255,180,0,.2)!important;border-radius:12px!important}
.stSpinner>div{border-top-color:#7040ff!important}
hr{border-color:rgba(255,255,255,.06)!important;margin:1.4rem 0!important}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(100,40,255,.28);border-radius:10px}

/* ── URL INPUT SPECIAL ── */
.url-hint{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:rgba(120,110,180,.55);margin-top:.5rem;line-height:1.6}
.source-preview{
  background:rgba(0,200,255,.05);border:1px solid rgba(0,200,255,.18);
  border-radius:10px;padding:.65rem 1rem;margin-top:.6rem;
  font-family:'JetBrains Mono',monospace;font-size:.75rem;color:#80d8f0;
  word-break:break-all;display:flex;align-items:center;gap:.5rem;
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════════════════════
def is_youtube_url(s: str) -> bool:
    s = s.strip()
    return bool(re.search(r'(youtube\.com/watch|youtu\.be/|youtube\.com/shorts)', s))

def is_url(s: str) -> bool:
    return s.strip().startswith(("http://", "https://"))

def parse_list(raw) -> list:
    if isinstance(raw, list):
        return [str(i).strip() for i in raw if str(i).strip()]
    if isinstance(raw, str):
        lines = [
            l.strip().lstrip("-•*·1234567890.)> ").strip()
            for l in raw.splitlines()
        ]
        return [l for l in lines if l and len(l) > 2]
    return [str(raw)] if raw else []

def render_items(items: list, kind: str, icon: str):
    if not items:
        st.markdown('<div class="empty"><div class="ei">🔍</div>None detected.</div>', unsafe_allow_html=True)
        return
    for i, item in enumerate(items):
        st.markdown(
            f'<div class="item {kind}" style="animation-delay:{i*0.04:.2f}s">'
            f'<span class="item-ic">{icon}</span>'
            f'<span style="flex:1">{item}</span>'
            f'</div>',
            unsafe_allow_html=True
        )

def draw_pipeline(current: int, steps: list):
    html = '<div class="glass" style="max-width:720px;margin:0 auto">'
    html += '<div class="lbl"><span class="lbl-bar"></span>Analysis Pipeline</div>'
    for i, (ic, lb) in enumerate(steps):
        cls = "done" if i < current else ("active" if i == current else "pending")
        html += f'<div class="p-step {cls}"><div class="p-dot"></div><span>{ic}&nbsp; {lb}</span></div>'
    html += '</div>'
    return html


# ═══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════════════════════════════════════════════════
DEFAULTS = {"results": None, "chat": [], "done": False, "mode": "upload"}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ═══════════════════════════════════════════════════════════════════════════════
#  PAGE CONTENT
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="mm-wrap">', unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="mm-hero">
  <div class="mm-badge"><span class="mm-badge-dot"></span>AI · Meeting Intelligence · v3</div>
  <h1 class="mm-h1">Your meetings,<br><span class="g">finally understood.</span></h1>
  <p class="mm-sub">Upload audio, paste a file path, or drop a YouTube link — get instant transcription, smart summaries, action items & live Q&A.</p>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
#  INPUT PANEL
# ═══════════════════════════════════════════════════════════════════════════════
if not st.session_state.done:

    # ── Mode selector ──────────────────────────────────────────────────────
    m = st.session_state.mode
    tab_html = f"""
    <div class="mode-tabs">
      <div class="mode-tab {'active' if m=='upload' else ''}" 
           onclick="window.parent.postMessage({{type:'streamlit:setComponentValue',value:'upload'}},'*')" 
           id="tab-upload">🎵&nbsp; Upload File</div>
      <div class="mode-tab {'active' if m=='path' else ''}"
           onclick="window.parent.postMessage({{type:'streamlit:setComponentValue',value:'path'}},'*')"
           id="tab-path">📂&nbsp; File Path</div>
      <div class="mode-tab {'active' if m=='youtube' else ''}"
           onclick="window.parent.postMessage({{type:'streamlit:setComponentValue',value:'youtube'}},'*')"
           id="tab-youtube">▶️&nbsp; YouTube / URL</div>
    </div>"""
    # Use actual Streamlit radio styled as tabs
    mode_choice = st.radio(
        "INPUT MODE",
        ["🎵  Upload File", "📂  File Path", "▶️  YouTube / URL"],
        horizontal=True,
        label_visibility="collapsed",
        key="mode_radio",
    )
    mode_key = {"🎵  Upload File": "upload", "📂  File Path": "path", "▶️  YouTube / URL": "youtube"}[mode_choice]

    st.markdown('<div class="glass" style="max-width:860px;margin:0 auto 1.4rem">', unsafe_allow_html=True)
    st.markdown('<div class="lbl"><span class="lbl-bar"></span>Configure your analysis</div>', unsafe_allow_html=True)

    source_path = None
    valid_source = False

    # ── Mode: Upload ───────────────────────────────────────────────────────
    if mode_key == "upload":
        up = st.file_uploader(
            "Drag & drop your audio file, or click to browse",
            type=["mp3", "wav", "m4a", "mp4", "ogg", "flac", "webm", "aac"],
            label_visibility="visible",
        )
        if up:
            d = "/tmp/meetmind_up"
            os.makedirs(d, exist_ok=True)
            save = os.path.join(d, up.name)
            with open(save, "wb") as f:
                f.write(up.getbuffer())
            source_path = save
            valid_source = True
            size_kb = up.size / 1024
            size_str = f"{size_kb:.0f} KB" if size_kb < 1024 else f"{size_kb/1024:.1f} MB"
            st.success(f"✓  **{up.name}** · {size_str} · Ready to analyse")

    # ── Mode: File path ────────────────────────────────────────────────────
    elif mode_key == "path":
        raw_path = st.text_input(
            "ABSOLUTE FILE PATH",
            placeholder="/home/user/recordings/standup.mp3",
            key="fp_input",
        )
        if raw_path:
            if os.path.exists(raw_path.strip()):
                source_path = raw_path.strip()
                valid_source = True
                st.markdown(f'<div class="source-preview">✓ &nbsp;{source_path}</div>', unsafe_allow_html=True)
            else:
                st.error("⚠  File not found at that path. Check spelling and try again.")

    # ── Mode: YouTube / URL ────────────────────────────────────────────────
    else:
        yt_url = st.text_input(
            "YOUTUBE LINK OR AUDIO URL",
            placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            key="yt_input",
        )
        st.markdown("""
        <div class="url-hint">
          ✦ Supports: YouTube videos, YouTube Shorts, direct audio URLs (.mp3, .wav, etc.)<br>
          ✦ For YouTube, <code>yt-dlp</code> must be installed: <code>pip install yt-dlp</code><br>
          ✦ For URLs, <code>requests</code> will stream the file automatically
        </div>""", unsafe_allow_html=True)

        if yt_url and yt_url.strip():
            url = yt_url.strip()
            if is_youtube_url(url) or is_url(url):
                source_path = url
                valid_source = True
                icon = "▶️" if is_youtube_url(url) else "🔗"
                st.markdown(f'<div class="source-preview">{icon} &nbsp;{url}</div>', unsafe_allow_html=True)
            else:
                st.warning("⚠  Paste a full YouTube URL (https://...) or a direct audio URL.")

    # ── Language ───────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    lang_map = {
        "🇺🇸 English": "en", "🇪🇸 Spanish": "es", "🇫🇷 French": "fr",
        "🇩🇪 German": "de", "🇸🇦 Arabic": "ar", "🇵🇰 Urdu": "ur",
        "🌐 Auto-detect": "auto",
    }
    col_lang, col_btn = st.columns([1, 1.6], gap="large")
    with col_lang:
        lang_key = st.selectbox("LANGUAGE", list(lang_map.keys()), key="lang_sel")
        language = lang_map[lang_key]
    with col_btn:
        st.markdown("<div style='height:1.9rem'></div>", unsafe_allow_html=True)
        analyse_btn = st.button(
            "🔍  Analyse Meeting",
            disabled=not valid_source,
            use_container_width=True,
            key="analyse_btn",
        )

    st.markdown("</div>", unsafe_allow_html=True)  # close glass

    # ═══════════════════════════════════════════════════════════════════════
    #  PIPELINE EXECUTION
    # ═══════════════════════════════════════════════════════════════════════
    if analyse_btn and valid_source and source_path:

        STEPS = [
            ("🔊", "Processing audio source"),
            ("✍️",  "Transcribing with Whisper"),
            ("🏷️", "Generating meeting title"),
            ("📝", "Summarising transcript"),
            ("⚡", "Extracting action items"),
            ("🗳️", "Extracting key decisions"),
            ("❓", "Extracting questions raised"),
            ("🔗", "Building RAG retrieval chain"),
        ]

        prog = st.empty()

        def update(step):
            prog.markdown(draw_pipeline(step, STEPS), unsafe_allow_html=True)

        try:
            # ── Handle YouTube / URL download first ──────────────────────
            actual_source = source_path

            if is_youtube_url(source_path):
                update(0)
                import subprocess, tempfile
                dl_dir = tempfile.mkdtemp()
                out_tmpl = os.path.join(dl_dir, "audio.%(ext)s")
                result = subprocess.run(
                    ["yt-dlp", "-x", "--audio-format", "mp3",
                     "--audio-quality", "0", "-o", out_tmpl, source_path],
                    capture_output=True, text=True
                )
                if result.returncode != 0:
                    raise RuntimeError(f"yt-dlp failed:\n{result.stderr}")
                mp3_files = [f for f in os.listdir(dl_dir) if f.endswith(".mp3")]
                if not mp3_files:
                    raise RuntimeError("yt-dlp ran but produced no audio file.")
                actual_source = os.path.join(dl_dir, mp3_files[0])
                st.success(f"✓ YouTube audio downloaded: {mp3_files[0]}")

            elif is_url(source_path) and not is_youtube_url(source_path):
                update(0)
                import requests, tempfile
                r = requests.get(source_path, stream=True, timeout=60)
                r.raise_for_status()
                ext = source_path.split("?")[0].rsplit(".", 1)[-1] or "mp3"
                tmp = tempfile.NamedTemporaryFile(suffix=f".{ext}", delete=False)
                for chunk in r.iter_content(chunk_size=8192):
                    tmp.write(chunk)
                tmp.close()
                actual_source = tmp.name
                st.success(f"✓ Audio downloaded from URL.")

            # ── Core pipeline ─────────────────────────────────────────────
            from utils.audio_processor import process_input
            from core.transcriber import transcribe_all
            from core.sammrize import summarize, generate_title
            from core.extrator import extract_actionable_items, extract_key_decisions, extract_questions
            from core.rag_engine import build_rag_chain

            update(0); audio      = process_input(actual_source)
            update(1); transcript = transcribe_all(audio, language)
            update(2); title      = generate_title(transcript)
            update(3); summary    = summarize(transcript)
            update(4); actions    = parse_list(extract_actionable_items(transcript))
            update(5); decisions  = parse_list(extract_key_decisions(transcript))
            update(6); questions  = parse_list(extract_questions(transcript))
            update(7); rag_chain  = build_rag_chain(transcript)

            st.session_state.results = dict(
                title=title, transcript=transcript, summary=summary,
                actions=actions, decisions=decisions, questions=questions,
                rag_chain=rag_chain,
            )
            st.session_state.done = True
            prog.empty()
            st.rerun()

        except ImportError as e:
            prog.empty()
            st.error(f"**Import error** — make sure all modules are installed:\n\n`{e}`")
        except Exception as e:
            prog.empty()
            st.error(f"**Pipeline error:**\n\n{e}")


# ═══════════════════════════════════════════════════════════════════════════════
#  RESULTS DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.done and st.session_state.results:
    r = st.session_state.results

    # top bar
    _, rc = st.columns([5, 1])
    with rc:
        if st.button("↺  New Meeting", use_container_width=True, key="reset_btn"):
            for k, v in DEFAULTS.items():
                st.session_state[k] = v
            st.rerun()

    # Title card
    st.markdown(f"""
    <div class="title-card">
      <div class="title-ey">📋 Meeting Title</div>
      <div class="title-tx">{r['title']}</div>
    </div>""", unsafe_allow_html=True)

    # Stats ribbon
    wc = len(r["transcript"].split()) if r["transcript"] else 0
    st.markdown(f"""
    <div class="stats-grid">
      <div class="stat-c"><span class="stat-n">{len(r["actions"])}</span><span class="stat-l">Action Items</span></div>
      <div class="stat-c"><span class="stat-n">{len(r["decisions"])}</span><span class="stat-l">Key Decisions</span></div>
      <div class="stat-c"><span class="stat-n">{len(r["questions"])}</span><span class="stat-l">Questions</span></div>
      <div class="stat-c"><span class="stat-n">{wc:,}</span><span class="stat-l">Words</span></div>
    </div>""", unsafe_allow_html=True)

    # TABS
    t1, t2, t3, t4 = st.tabs(["📝  Summary", "⚡  Extractions", "📄  Transcript", "💬  Ask Anything"])

    # ── SUMMARY ────────────────────────────────────────────────────────────
    with t1:
        st.markdown('<div class="sh">Meeting Summary</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass"><p class="sum-body">{r["summary"]}</p></div>', unsafe_allow_html=True)

    # ── EXTRACTIONS ────────────────────────────────────────────────────────
    with t2:
        ca, cb = st.columns(2, gap="large")
        with ca:
            st.markdown('<div class="sh">⚡ Action Items</div>', unsafe_allow_html=True)
            render_items(r["actions"], "ac", "⚡")
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown('<div class="sh">❓ Questions Raised</div>', unsafe_allow_html=True)
            render_items(r["questions"], "qc", "❓")
        with cb:
            st.markdown('<div class="sh">🗳️ Key Decisions</div>', unsafe_allow_html=True)
            render_items(r["decisions"], "dc", "🗳️")

    # ── TRANSCRIPT ─────────────────────────────────────────────────────────
    with t3:
        st.markdown('<div class="sh">Full Transcript</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tx-box">{r["transcript"]}</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        dl_c, _ = st.columns([1, 3])
        with dl_c:
            st.download_button("⬇  Download .txt", data=r["transcript"],
                               file_name="transcript.txt", mime="text/plain")

    # ── Q&A ────────────────────────────────────────────────────────────────
    with t4:
        st.markdown('<div class="sh">💬 RAG-Powered Q&A</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="glass" style="margin-bottom:1.1rem;padding:.9rem 1.3rem">
          <span style="font-size:.82rem;color:rgba(155,145,200,.6)">
          Ask anything about this meeting — answers come strictly from the transcript.
          </span>
        </div>""", unsafe_allow_html=True)

        # Chat history
        if st.session_state.chat:
            html = '<div class="chat-scroll">'
            for msg in st.session_state.chat:
                cls = "u" if msg["role"] == "user" else "b"
                who = "You" if msg["role"] == "user" else "MeetMind AI"
                html += f'<div class="bubble {cls}"><div class="bm">{who}</div>{msg["content"]}</div>'
            html += '</div>'
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.markdown('<div class="empty"><div class="ei">💬</div>No questions yet — ask something!</div>',
                        unsafe_allow_html=True)

        q_c, b_c = st.columns([5, 1], gap="small")
        with q_c:
            user_q = st.text_input("Ask a question…", placeholder="What was decided about the roadmap?",
                                   label_visibility="collapsed", key="qa_inp")
        with b_c:
            ask_b = st.button("Ask →", use_container_width=True, key="ask_b")

        if ask_b and user_q.strip():
            from core.rag_engine import ask_question
            st.session_state.chat.append({"role": "user", "content": user_q.strip()})
            with st.spinner("Thinking…"):
                ans = ask_question(r["rag_chain"], user_q.strip())
            st.session_state.chat.append({"role": "assistant", "content": ans})
            st.rerun()

        if st.session_state.chat:
            cl, _ = st.columns([1, 4])
            with cl:
                if st.button("🗑  Clear", key="clr_chat"):
                    st.session_state.chat = []
                    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)  # close mm-wrap