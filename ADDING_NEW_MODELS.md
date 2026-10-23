# Adding Support for Additional Model Families

This document explains how the model availability tracker finds its data and how to add new sources.

## Data Sources

Availability is scraped from public Microsoft Learn pages. Learn returns a page's Markdown when it is
requested with an `Accept: text/markdown` header. (The `MicrosoftDocs/azure-ai-docs` GitHub repository
that previously backed these pages is no longer public.)

| Learn page | Deployment types tracked |
|------------|--------------------------|
| [Region availability for Foundry Models sold by Azure](https://learn.microsoft.com/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability) | Global, Data Zone and Regional Standard; Global, Data Zone and Regional Provisioned; Global and Data Zone Batch |
| [Foundry Models from partners and community](https://learn.microsoft.com/azure/foundry/foundry-models/concepts/models-from-partners) | Partner Global Standard and Data Zone Standard |
| [Priority processing](https://learn.microsoft.com/azure/foundry/openai/concepts/priority-processing) | Global Standard and Data Zone Standard priority processing |
| [Foundry Models sold by Azure in Azure Government](https://learn.microsoft.com/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-gov) | Azure Government Data Zone, Standard and Provisioned |

## How the System Works

`.region-watch/diff_regions.py`:
1. Fetches each page in `LEARN_SOURCES` as Markdown
2. Tracks the heading that names the deployment type for each table (an `##`/`###` heading or a tab)
   and maps it to a snapshot SKU key through the source's `sections` table
3. Parses the tables (either models × region codes or regions × models) for ✅ cells
4. Compares the result with `.region-watch/regions_snapshot.json`, records changes and writes the new snapshot

The script exits with an error and leaves the snapshot untouched if a page can't be fetched, a page
yields no availability tables, or the scrape loses more than half of the models in the snapshot. Set
`ALLOW_SNAPSHOT_SHRINK=1` to accept a large drop that is expected.

Tables under headings that aren't in a source's `sections` table are skipped with a warning on stderr,
which is the signal that Microsoft added a new deployment type.

## Adding a New Source or Deployment Type

Edit `LEARN_SOURCES` in `.region-watch/diff_regions.py`:

```python
{
    "name": "my-new-page",
    "url": LEARN_BASE + "path/to/learn-page",
    "heading": "h2",                  # "h2", "h3" or "tab": where the deployment type is named
    "within_h2": "optional h2 text",  # only read tables under this h2 (lowercase)
    "sections": {
        "global standard": "standard-global",  # lowercase heading text -> SKU key
    },
},
```

Reuse an existing SKU key where the deployment type matches, so labels and explorer filters keep
working. For a new key, add a label to `SKU_LABEL_OVERRIDES` in `diff_regions.py` if needed, and map it to
an explorer deployment type in `SKU_KEY_TO_TYPE` in `generate_docs.py`.

## Filtering Models (Optional)

All models are included by default. To filter, set environment variables:

```bash
export MODEL_MATRIX_INCLUDE_MODELS="gpt-4,gpt-4o,phi-3"
export MODEL_MATRIX_EXCLUDE_MODELS="deprecated-model,test-model"
```

## Testing Your Changes

```bash
python .region-watch/diff_regions.py > test_output.json

# Model count and names
jq '.current | length' test_output.json
jq '.current | keys' test_output.json
```

Note that running the script updates `.region-watch/regions_snapshot.json`.
