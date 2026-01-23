# Adding Support for Additional Model Families

This document explains how to add support for additional model families to the model availability tracking system.

## Current Status

The system currently monitors models from the Azure AI documentation repository from the following directories:
```
articles/ai-foundry/openai/includes/model-matrix/          # OpenAI models (enabled)
articles/ai-foundry/foundry-models/includes/model-matrix/  # Foundry models (enabled)
```

These models are documented in markdown tables with regional availability information.

## Model Families Currently Tracked

- **OpenAI models**: GPT-4, GPT-4o, GPT-3.5 Turbo, o1, o3, o4 series, DALL-E 3, Whisper, TTS, text embeddings
- **Foundry models**: Phi, Mistral, Qwen, gpt-oss, and other models documented in the foundry-models directory

## Default Behavior

**All models are included by default** - no filtering is applied unless explicitly configured via environment variables.

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

### Option 1: Via Code (Permanent)

Edit `.region-watch/diff_regions.py`:

```python
MODEL_MATRIX_DIRS = [
    "articles/ai-foundry/openai/includes/model-matrix",
    "articles/ai-foundry/foundry-models/includes/model-matrix",
    "articles/ai-foundry/models/includes/model-matrix",  # Add more directories as needed
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
    MODEL_MATRIX_EXTRA_DIRS: "articles/ai-foundry/models/includes/model-matrix"  # For additional directories
  run: |
    python .region-watch/diff_regions.py > region_diff.json
```

## Filtering Models (Optional)

By default, **all models from all configured directories are included**. This ensures the mkdocs pages show complete information.

To filter models, set environment variables:

```bash
# Include only specific models
export MODEL_MATRIX_INCLUDE_MODELS="gpt-4,gpt-4o,phi-3"

# Exclude specific models
export MODEL_MATRIX_EXCLUDE_MODELS="deprecated-model,test-model"
```

Note: Filtering is opt-in. If neither variable is set, all models are included.

## Verifying Azure Documentation

Before adding a new directory, verify it exists and contains the expected format:

1. Visit the Azure AI docs repository:
   ```
   https://github.com/MicrosoftDocs/azure-ai-docs
   ```

2. Navigate to potential directories:
   ```
   articles/ai-foundry/openai/includes/model-matrix/         # Enabled
   articles/ai-foundry/foundry-models/includes/model-matrix/ # Enabled
   articles/ai-foundry/models/includes/model-matrix/         # Available for addition
   articles/machine-learning/includes/model-matrix/
   ```

3. Look for markdown files (`.md`) containing tables with:
   - Model names in column headers
   - Region names in row headers
   - ✅ checkmarks indicating availability

## System Status

✅ **OpenAI models** - Fully tracked and monitored  
✅ **Foundry models** - Enabled and ready to track (phi, mistral, qwen, gpt-oss, etc.)  
⚠️ **Note**: The foundry-models directory may or may not exist in the Azure docs yet. The system will gracefully handle missing directories.

## Monitoring for Updates

To check if Azure adds new directories:

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

# Verify no filtering is applied by default (all models included)
cat test_output.json | jq '.current | length'
```

## Questions or Issues?

If you discover new model-matrix directories or alternative data sources, please:
1. Update `MODEL_MATRIX_DIRS` in `.region-watch/diff_regions.py`
2. Test the changes
3. Update this documentation
4. Submit a pull request

---

**Last Updated**: January 2026  
**Status**: Monitoring OpenAI and Foundry models. All models included by default for comprehensive mkdocs pages.
