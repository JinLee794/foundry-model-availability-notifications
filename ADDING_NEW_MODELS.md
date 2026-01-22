# Adding Support for Additional Model Families

This document explains how to add support for non-OpenAI model families (such as Phi, Mistral, Qwen, gpt-oss, etc.) to the model availability tracking system.

## Current Status

The system currently monitors **OpenAI models only** from the Azure AI documentation repository. These models are documented in markdown tables at:
```
articles/ai-foundry/openai/includes/model-matrix/
```

## Requested Model Families

The following model families have been requested for inclusion:
- **Phi** (Microsoft's small language models: Phi-3, etc.)
- **Mistral** (Mistral AI models: Mistral-7B, Mistral-Large, etc.)
- **Qwen** (Alibaba's Qwen models)
- **gpt-oss-20b** (OpenAI's open-weight model)

## How the System Works

The monitoring system:
1. Fetches markdown files from configured directories in the Azure AI docs GitHub repository
2. Parses tables in these markdown files to extract:
   - Model names (from table column headers)
   - Azure regions (from table rows)
   - Availability status (✅ checkmarks in table cells)
3. Stores the availability data in JSON format
4. Detects changes and creates notifications

## Adding New Model Sources

### Option 1: Via Code (When Azure Documents Models Similarly)

If Azure adds model-matrix directories for non-OpenAI models, edit `.region-watch/diff_regions.py`:

```python
MODEL_MATRIX_DIRS = [
    "articles/ai-foundry/openai/includes/model-matrix",  # OpenAI models
    "articles/ai-foundry/foundry-models/includes/model-matrix",  # Uncomment if this exists
    "articles/ai-foundry/models/includes/model-matrix",  # Uncomment if this exists
]
```

### Option 2: Via Environment Variable (Temporary/Testing)

Set the `MODEL_MATRIX_EXTRA_DIRS` environment variable:

```bash
# Single directory
export MODEL_MATRIX_EXTRA_DIRS="articles/ai-foundry/foundry-models/includes/model-matrix"

# Multiple directories (comma-separated)
export MODEL_MATRIX_EXTRA_DIRS="articles/ai-foundry/foundry-models/includes/model-matrix,articles/ai-foundry/models/includes/model-matrix"
```

Or in GitHub Actions workflow (`.github/workflows/region-watch.yml`):

```yaml
- name: Run diff
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    MODEL_MATRIX_EXTRA_DIRS: "articles/ai-foundry/foundry-models/includes/model-matrix"
  run: |
    python .region-watch/diff_regions.py > region_diff.json
```

## Verifying Azure Documentation

Before adding a new directory, verify it exists and contains the expected format:

1. Visit the Azure AI docs repository:
   ```
   https://github.com/MicrosoftDocs/azure-ai-docs
   ```

2. Navigate to potential directories:
   ```
   articles/ai-foundry/foundry-models/includes/model-matrix/
   articles/ai-foundry/models/includes/model-matrix/
   articles/machine-learning/includes/model-matrix/
   ```

3. Look for markdown files (`.md`) containing tables with:
   - Model names in column headers
   - Region names in row headers
   - ✅ checkmarks indicating availability

## Current Limitations

As of now:
- **No similar model-matrix documentation exists** for Phi, Mistral, Qwen, or gpt-oss models in the Azure AI docs repository
- These models are available on Azure but documented differently (via Model Catalog, deployment guides, etc.)
- Regional availability is not published in the same machine-readable table format

## Alternative Approaches

If Azure doesn't provide model-matrix tables for these models, alternatives include:

1. **Azure API Integration**: Query the Azure AI Model Catalog API for availability
2. **Manual Configuration**: Maintain a static list of models and regions
3. **Web Scraping**: Parse the Azure AI Studio website (not recommended)
4. **Wait for Documentation**: Monitor the Azure docs repo for new model-matrix directories

## Monitoring for Updates

To check if Azure adds support:

1. Watch the Azure AI docs repository:
   ```
   https://github.com/MicrosoftDocs/azure-ai-docs
   ```

2. Search for "Phi", "Mistral", "Qwen", or "gpt-oss" with "regional" or "availability"

3. Check commit history in these directories:
   ```
   articles/ai-foundry/foundry-models/
   articles/ai-foundry/models/
   ```

## Testing Your Changes

After adding a new directory:

```bash
# Run the diff script
python .region-watch/diff_regions.py > test_output.json

# Check if new models are discovered
cat test_output.json | jq '.current | keys'

# Look for your model families (phi, mistral, qwen, gpt-oss)
cat test_output.json | jq '.current | keys | map(select(test("phi|mistral|qwen|gpt-oss"; "i")))'
```

## Questions or Issues?

If you discover new model-matrix directories or alternative data sources, please:
1. Update `MODEL_MATRIX_DIRS` in `.region-watch/diff_regions.py`
2. Test the changes
3. Update this documentation
4. Submit a pull request

---

**Last Updated**: January 2026
**Status**: Monitoring OpenAI models only. Non-OpenAI models (Phi, Mistral, Qwen, gpt-oss) pending Azure documentation.
