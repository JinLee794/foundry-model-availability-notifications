# Azure AI Foundry Model Availability Tracker

Automatically track which Azure AI models are available in which regions. Get notified when new models or regions become available.

**View Live Dashboard**: [https://JinLee794.github.io/foundry-model-availability-notifications](https://JinLee794.github.io/foundry-model-availability-notifications)

## What Does This Do?

This project monitors Azure AI Foundry and:

- Checks model availability every 6 hours
- Detects when new models or regions are added/removed
- Creates GitHub issues to notify you of changes
- Publishes an interactive website showing all available models

## How It Works

```mermaid
flowchart LR
    A[Azure API] -->|Check every 6 hours| B[Compare Changes]
    B -->|Save results| C[JSON Files]
    C -->|Generate| D[Website]
    C -->|Generate| E[GitHub Issues]

    style C fill:#fff3e0
    style D fill:#e8f5e9
    style E fill:#f3e5f5
```

### Simple Explanation

1. **GitHub Actions runs every 6 hours**
   - Fetches current model data from Azure
   - Compares it to the previous snapshot

2. **If changes are detected:**
   - Saves the new data to `.region-watch/regions_snapshot.json`
   - Records the change in `.region-watch/history/`
   - Creates a GitHub issue describing what changed

3. **Website is automatically updated:**
   - Reads the JSON data files
   - Generates markdown pages with tables and filters
   - Builds a static site with MkDocs
   - Deploys to GitHub Pages

### The Data is the Source of Truth

Everything comes from the JSON files in `.region-watch/`:

- `regions_snapshot.json` - Current state of all models
- `history/diff-*.json` - Record of all changes over time

The website and notifications are just different ways to view this same data.

## Project Structure

```
├── .github/workflows/
│   ├── region-watch.yml       # Monitors Azure API every 6 hours
│   └── deploy-docs.yml        # Builds and deploys website
│
├── .region-watch/
│   ├── regions_snapshot.json  # Current model availability (source of truth)
│   ├── history/               # Historical changes
│   ├── diff_regions.py        # Detects changes
│   ├── fetch_prices.py        # Pulls list prices (Azure Retail Prices + Marketplace catalog APIs)
│   ├── pricing.json           # Token, media and PTU list prices (East US 2)
│   ├── fetch_retirements.py   # Pulls Microsoft's model retirement schedule (all providers)
│   ├── retirement_data.json   # Lifecycle stage, retirement date and replacement per model version
│   └── render_markdown.py     # Creates summary table
│
├── docs/                      # Generated website content
├── generate_docs.py           # Converts JSON to website pages
└── mkdocs.yml                 # Website configuration
```

## Quick Start

### View the Website

Visit [https://JinLee794.github.io/foundry-model-availability-notifications](https://JinLee794.github.io/foundry-model-availability-notifications)

### Run Locally

```bash
# Install dependencies
pip install mkdocs mkdocs-material

# Generate website pages from latest data
python generate_docs.py

# Preview the site at http://localhost:8000
mkdocs serve
```

### Manually Check for Changes

```bash
# Install dependencies
pip install requests

# Check current availability and detect changes
python .region-watch/diff_regions.py > region_diff.json

# View the changes
cat region_diff.json
```

## What Gets Generated

### Website Pages

- **Dashboard** - Instant model finder (press `Ctrl+K` / `Cmd+K`), KPI cards, interactive visuals (retirement runway timeline, lifecycle waffle, world availability map with top regions, provider × deployment-type matrix, monthly availability momentum), retirement watchlist, and latest availability changes
- **Explorer** - Single-pane grid of every model × region × deployment type with live filters, required-region selection, shareable URLs, CSV export and an "Expand table" full-window view (Esc to exit)
- **Models** - Model catalog: instant search plus provider-grouped cards showing region count, deployment options and lifecycle flags (retiring models also show their replacement), with a "Compare availability" link into the Explorer per provider. Each model page opens with a "Retiring → Move to" banner naming the replacement and the regions where it is not yet offered (also shown for GA models that already have a retirement date scheduled)
- **Deployment & PTU** - Deployment-type matrix (where inference runs × how you pay, plus Batch and Partner) linking each type into the Explorer, followed by a plain-language provisioned throughput guide based on Microsoft Learn, with a quick PTU estimator and links to the Foundry capacity calculator
- **Cost planner** - Describe a workload (requests/day, input/output tokens, cache and batch share, deployment type) or pick a preset, then compare projected monthly pay-as-you-go cost across every priced model (the default) or a narrower set in a stacked bar chart (input / cached / output). A PTU panel plots pay-as-you-go against hourly and 1-year reserved PTU as volume grows and calls out the break-even point. Model sets include all models (default), retiring → replacements (every model in a retirement window, plus its named replacement), popular, under $1 per 1M and partner models; state lives in the URL and the price sheet exports to CSV. A Media & audio estimator compares image, speech, video, document and search models by monthly volume (images, minutes, seconds, pages, queries); per-image and per-minute figures for token-billed models use editable assumptions
- **Lifecycle** - A plain-language retirement explainer. It covers:
  - The five stages and the GA timeline.
  - A before/after view of what happens to a deployment on retirement day, for pay-as-you-go, PTU, Batch, preview and fine-tuned deployments.
  - How each upgrade setting behaves.
  - Whether the replacement stays in your region or data zone, with live region coverage for each named replacement.
  - A countdown to retirement, an FAQ, and badge and API reference.
- **Retirements** - Interactive retirement planner: horizon tabs (this month, next month, 3/6/12 months), a calendar with retirement chips and deprecated-window spans (or a mini-month overview for longer horizons), a Gantt-style timeline view, search and category filters, and a plain-language agenda with replacements; followed by the full schedule table
- **Change History** - Timeline of all availability changes
- **Individual Model Pages** - Per-version lifecycle tracks, next retirement, a pricing card (blended price, per-deployment price table, PTU rates and the cost change of moving to the replacement), and a filterable region × SKU matrix

Region and deployment-type links across the site open the Explorer pre-filtered. The former By Region and By SKU Type pages are now redirect stubs, so old links (e.g. `by-region/?region=East%20US`) land on the matching Explorer view.

Prices come from two public, unauthenticated sources. `python .region-watch/fetch_prices.py` writes `.region-watch/pricing.json`:
- The [Azure Retail Prices API](https://learn.microsoft.com/rest/api/cost-management/retail-prices/azure-retail-prices) gives USD list prices per 1M tokens for East US 2, by deployment type, plus PTU hourly and reservation prices. It also gives media meters (per image, megapixel, second of video, audio hour, 1M characters, page or query) from a curated meter table. Classic TTS and Whisper aren't sold in East US 2, so they fall back to North Central US.
- The Azure Marketplace catalog API (`catalogapi.azure.com`) gives prices for partner models billed through Marketplace (Anthropic, Cohere, Meta, Stability AI, Nixtla). Retail prices take precedence. If the Marketplace call fails, the previous Marketplace prices are kept.

The daily Region watch workflow runs the fetcher and only commits when a price changes. Models with no published pay-as-you-go price, such as the model router or partner models with no Marketplace offer, are listed on the Cost planner with the reason. Prices exclude tax and negotiated discounts.

Lifecycle data comes from Microsoft's [model retirement schedule](https://learn.microsoft.com/azure/foundry/openai/concepts/model-retirement-schedule). `python .region-watch/fetch_retirements.py` reads its source Markdown in [MicrosoftDocs/azure-ai-docs](https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/openai/includes/concepts-model-retirement-schedule-content.md) and writes `.region-watch/retirement_data.json`, covering every provider table (Azure OpenAI, Anthropic, DeepSeek, xAI, Meta, Mistral, Cohere, Fireworks, Microsoft and more) plus fine-tuned retirements. For each model version it records the published lifecycle (GA, Preview, Legacy, Deprecated or Retired), the retirement date and the named replacement, plus any alternates. The schedule has no deprecation-date column, so known deprecation dates are carried forward while they still agree with the published lifecycle. The daily workflow runs the fetcher, which leaves the file untouched if the source can't be fetched or parses to an implausibly short table.

The finder and explorer are backed by `docs/assets/model-index.json`, which `generate_docs.py` writes on every run, and the Cost planner by `docs/assets/pricing.json`. Lifecycle badges show a plain-language explanation on hover or focus.

Model names across the site carry a provider logo (catalog, Explorer, finder, dashboard and model pages). The logos live in `docs/assets/providers/<family-slug>.svg`, adapted from [LobeHub Icons](https://github.com/lobehub/lobe-icons) (MIT); see `docs/assets/providers/NOTICE.txt`. Providers without a logo fall back to `partner.svg`. To add one, drop in an SVG named after the family slug and add a matching `.pv--<slug>` rule in `docs/stylesheets/custom.css`.
### Notifications

When changes are detected, a GitHub issue is automatically created with:

- Summary of what changed
- List of added/removed regions per model
- Link to the website for full details

**Get Notified Automatically:**

To receive notifications when model availability changes:

1. Watch this repository (click "Watch" at the top)
2. Configure your notification settings to include "Issues"
3. You'll get notified whenever a new issue is created with the `region-watch` label

**Tag Specific Users:**

You can configure automatic mentions by setting the `ISSUE_ASSIGNEES` environment variable in the workflow:

```yaml
# In .github/workflows/region-watch.yml
- name: Notify via GitHub issue
  env:
    ISSUE_ASSIGNEES: "user1,user2,user3"  # Add this line
```

This will automatically assign and notify specific team members when changes are detected

## Key Files Explained

| File | Purpose |
|------|---------|
| `.region-watch/regions_snapshot.json` | **The source of truth** - Current state of all models |
| `.region-watch/diff_regions.py` | Fetches data from Azure and compares to snapshot |
| `generate_docs.py` | Reads JSON and creates markdown pages |
| `mkdocs.yml` | Configures the website theme and navigation |
| `.github/workflows/region-watch.yml` | Runs the monitoring every 6 hours |
| `.github/workflows/deploy-docs.yml` | Builds and publishes the website |
| `ADDING_NEW_MODELS.md` | Guide for adding support for additional model families |

## Supported Models

Currently tracking models from multiple Azure AI model families:

**OpenAI models:**
- GPT-4, GPT-4o, GPT-3.5 Turbo
- o1, o3, o4 series
- DALL-E 3, Whisper, TTS
- Text embeddings (ada-002, text-embedding-3)

**Foundry models:**
- Phi (Microsoft's small language models)
- Mistral (Mistral AI models)
- Qwen (Alibaba's models)
- gpt-oss (OpenAI's open-weight models)
- Other models from the Azure AI Foundry catalog

**Default behavior:** All models from all configured sources are included by default to provide comprehensive information in the mkdocs pages.

**Want to add more sources?** See [ADDING_NEW_MODELS.md](ADDING_NEW_MODELS.md) for instructions.

## Workflows

### Monitoring Workflow

**File**: `.github/workflows/region-watch.yml`

**When it runs:**

- Every 6 hours automatically
- Manually via GitHub Actions UI

**What it does:**

1. Fetch current model data from Azure
2. Compare to previous snapshot
3. Save new snapshot
4. Create GitHub issue if changes found
5. Trigger website rebuild

### Documentation Workflow

**File**: `.github/workflows/deploy-docs.yml`

**When it runs:**

- After monitoring workflow completes
- When you edit docs files
- Manually via GitHub Actions UI

**What it does:**

1. Run `generate_docs.py` to create pages
2. Build static site with MkDocs
3. Deploy to GitHub Pages

## Customization

### Change Monitoring Frequency

Edit `.github/workflows/region-watch.yml`:

```yaml
on:
  schedule:
    - cron: "23 */6 * * *"  # Change to your preferred schedule
```

### Modify Website Theme

Edit `mkdocs.yml` to change colors, features, or navigation.

### Add Custom Pages

Add your own markdown files to `docs/` and reference them in `mkdocs.yml` navigation.

## Why This Architecture?

**Separate data from presentation:**

- JSON files = reliable data storage
- Website = one way to view the data
- Could add other UIs (CLI tool, Slack bot, etc.) using the same data

**Automatic and hands-off:**

- GitHub Actions handles everything
- No servers to maintain
- Free hosting on GitHub Pages

**Transparent history:**

- All changes are committed to git
- Full audit trail of what changed when
- Can recreate website from any point in history
