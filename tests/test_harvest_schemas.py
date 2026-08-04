"""Row-schema equivalence tests for the CMU pronunciations scraper.

Relocated verbatim (assertions untouched) from metadatarr's
test_scrapers_batch4.py, keeping only the tests for the scraper that
lives in this package, re-pointed at pycmudict.harvest.*. These lock the
exact flat-row shape the scraper emits (the contract the LeData datasets
depend on) against a realistic upstream sample, so a future engine change
can't silently alter the output schema.
"""
from __future__ import annotations

from harvestkit.engine import all_sources

from pycmudict.harvest.cmu_pronunciations import CmuPronunciationsSource


def test_cmu_pronunciations_map_row_schema():
    src = CmuPronunciationsSource()
    row = src.map_row("aspirin", "AE1 S P ER0 IH0 N", 1, "cmudict.dict")
    assert row == {
        "term": "aspirin", "arpabet": "AE1 S P ER0 IH0 N",
        "variant_num": 1, "source_file": "cmudict.dict",
    }
    assert set(row) == {"term", "arpabet", "variant_num", "source_file"}


def test_cmu_pronunciations_fetch_matches_and_compounds(tmp_path):
    (tmp_path / "cmudict.dict").write_text(
        "aspirin AE1 S P ER0 IH0 N\n"
        "amoxicillin AH0 M AA2 K S AH0 S IH1 L IH0 N\n"
        "clavulanate K L AE1 V Y AH0 L AH0 N EY2 T\n",
        encoding="utf-8",
    )
    (tmp_path / "other_drugs.jsonl").write_text(
        '{"generic_name": "Aspirin"}\n'
        '{"generic_name": "amoxicillin clavulanate"}\n'
        '{"generic_name": "unknownium"}\n',
        encoding="utf-8",
    )

    src = CmuPronunciationsSource()
    src._output_dir = tmp_path
    rows, cursor = src.fetch(0)
    assert cursor is None
    terms = {r["term"]: r for r in rows}
    assert terms["aspirin"]["variant_num"] == 1
    assert terms["amoxicillin clavulanate"]["source_file"] == "cmudict.dict+compound"
    assert "unknownium" not in terms


def test_cmu_pronunciations_fetch_none_cursor_is_noop():
    src = CmuPronunciationsSource()
    rows, cursor = src.fetch(None)
    assert rows == []
    assert cursor is None


def test_cmu_pronunciations_registered():
    assert all_sources().get("cmu_pronunciations") is CmuPronunciationsSource
