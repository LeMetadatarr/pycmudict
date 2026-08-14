# Dataset

This repo produces the `cmu_pronunciations` dataset: ARPAbet pronunciations for drug and substance names. It downloads the CMU Pronouncing Dictionary once, scans the sibling `*.jsonl` datasets in the output directory for known name fields, and emits one row per matched term and pronunciation variant.

One row represents one pronunciation variant of one term.

## Format

The output is a JSONL file at `{output_dir}/cmu_pronunciations.jsonl`. Each line is a flat JSON object with these fields:

| Field | Type | Description |
| --- | --- | --- |
| `term` | string | Drug or substance name |
| `arpabet` | string | ARPAbet pronunciation, space-separated phonemes |
| `variant_num` | integer | Pronunciation variant number, starting at 1 |
| `source_file` | string | Source file or compound marker, e.g. `cmudict.dict` or `cmudict.dict+compound` |

## How to generate

Install the package:

```bash
pip install pycmudict
```

This scraper is a cross-reference pass, not a paginated crawl. It needs other drug or substance datasets in the same output directory first. Then run:

```bash
pycmudict-harvest cmu_pronunciations --output ~/.cache/metadatarr/scrapers/
```

Python equivalent:

```python
from pathlib import Path
from pycmudict.harvest.cmu_pronunciations import CmuPronunciationsSource

src = CmuPronunciationsSource()
src.run(Path.home() / ".cache/metadatarr/scrapers")
```

## Publish on Hugging Face

Yes. The dataset is a focused pronunciation lexicon for pharmaceutical and substance names. It is small, deterministic, and useful for speech and language models that must pronounce drug names.

## ML tasks served

- Grapheme-to-phoneme conversion for specialized vocabularies.
- ASR lexicon expansion for drug names.
- TTS pronunciation dictionary construction.
- Named-entity recognition and normalization for medication names.
