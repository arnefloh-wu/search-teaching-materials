# Build scripts for the lecture slides

| Script | Builds |
|---|---|
| `build_loyalty.py` | `Customer_Loyalty_Churn_SoW_Lecture_WU.pptx` (English) |
| `build_loyalty_de.py` | `Kundenbindung_Churn_SoW_Vorlesung_WU.pptx` (German) |

Each script takes a template and an output path. Any deck on the WU 16:10 template with the layouts Titelfolie Kontakt, Titel und Inhalt, Kapitelfolie and Abschlussfolie Kontakt works, because the script removes all existing slides first. The committed decks themselves work as templates. Run from this folder, so the scripts find `icons/`:

```bash
pip install python-pptx lxml
python build_loyalty.py ../Customer_Loyalty_Churn_SoW_Lecture_WU.pptx ../Customer_Loyalty_Churn_SoW_Lecture_WU.pptx
python build_loyalty_de.py ../Kundenbindung_Churn_SoW_Vorlesung_WU.pptx ../Kundenbindung_Churn_SoW_Vorlesung_WU.pptx
```

To change a slide, edit its block in the script (each starts with a `# n  Title` comment) and rebuild; edits made in PowerPoint are lost at the next build.

Checks after a rebuild:

- `python overlap_check.py <deck.pptx> <deck.pdf>`: text that overlaps other text or runs out of its card. Needs PyMuPDF and a PDF export (LibreOffice: `soffice --headless --convert-to pdf deck.pptx`).
- The polish-slides skill's `check_deck.py` (not included here) for broken words, small fonts and leftover template text.

`icons/` holds the Lucide line icons the decks use, rendered to PNG in navy and white.
