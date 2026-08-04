# pycmudict

CMU Pronouncing Dictionary cross-reference bulk harvester grouped onto the
[harvestkit](https://github.com/LeMetadatarr/harvestkit) resumable-harvest
engine. Extracted from [metadatarr](https://github.com/TigreGotico/metadatarr)'s
scraper collection into its own standalone package.

## Sources

| Scraper | Registry name | Source |
| --- | --- | --- |
| `cmu_pronunciations` | `cmu_pronunciations` | CMU Pronouncing Dictionary, cross-referenced against sibling `*.jsonl` datasets in the output directory |

## Install

```bash
pip install pycmudict
# or, for the HuggingFace publisher (via harvestkit):
pip install "pycmudict[hf]"
# or, for Cloudflare-guarded sources:
pip install "pycmudict[stealth]"
```

## Usage

```bash
# list every registered scraper
pycmudict-harvest --list

# harvest one source (one-shot pass; scans sibling *.jsonl files in --output)
pycmudict-harvest cmu_pronunciations --output ~/.cache/metadatarr/scrapers/
```

Every scraper is a `harvestkit.engine.Source` subclass: checkpoint/dedup/
pagination/throttle are handled by the shared engine, each module only
answers `initial_cursor()` and `fetch(cursor)`. See
[harvestkit](https://github.com/LeMetadatarr/harvestkit) for the full engine
API.

## License

Apache-2.0
