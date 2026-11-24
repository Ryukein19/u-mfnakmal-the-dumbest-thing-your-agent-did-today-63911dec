import os
# One-liner entry (123 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "My agent confidently summarized a meeting that never happened, complete with quotes from people who were never in the room."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
