"""The Tired Dark Lord: a 100-word villain monologue.

Writes one fixed monologue to entry.txt in the harness output
directory ($MAKEFUN_OUTPUT_DIR, else /output). Deterministic:
same bytes on every run. Stdlib only, no network.
"""

import os

MONOLOGUE = (
    "Come in. Mind the step \u2014 it bites.\n"
    "No, don't kneel. My knees gave out in the war of the Nine Banners, "
    "and no one knelt for me.\n"
    "You want the crown? It's there. On the hook. Next to my coat.\n"
    "Three kings have died for it. I signed each death with a quill "
    "I stole from my brother.\n"
    "He writes me. Every week. 'Forgive me.' I keep them in a tin.\n"
    "The eclipse comes tonight. My ravens are fed. The gate is shut.\n"
    "Take it, if you can lift it.\n"
    "It weighs more than it looks.\n"
    "...It always did.\n"
)


def main() -> None:
    # Gate: the scorer needs 1-600 chars of UTF-8; the brief asks
    # for about 100 words. Fail loudly here rather than shipping
    # a text the judge would never see.
    words = MONOLOGUE.split()
    assert 1 <= len(MONOLOGUE) <= 600, "monologue out of char range"
    assert 95 <= len(words) <= 105, "monologue off the 100-word mark"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
