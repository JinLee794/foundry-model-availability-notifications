# Foundry Model Availability Notifications

## System Flow

```mermaid
flowchart TD
    A[Initialize Baseline] --> B[Establish .region-watch/history]
    B --> C[GitHub Actions Scheduler]
    C --> D[Run diff_regions.py]
    D --> E{Changes Detected?}
    E -->|No Changes| F[Wait for Next Schedule]
    E -->|Changes Found| G[Update .region-watch/history]
    G --> H[Trigger Notification Pipeline]
    H --> I[Notify GitHub Repository Users]
    I --> J[Send Alerts/Issues/Discussions]
    F --> C
    J --> C
    
    style A fill:#e1f5fe
    style G fill:#fff3e0
    style H fill:#f3e5f5
    style I fill:#e8f5e8
```

## How It Works

1. **Establish Baseline**: Initialize the monitoring system with current model availability across regions
2. **Scheduled Monitoring**: GitHub Actions runs `diff_regions.py` on a regular schedule
3. **Change Detection**: Compare current state against historical data in `.region-watch/history`
4. **Notification Trigger**: When differences are detected, automatically notify repository users about model availability changes

This tool helps teams stay informed about Azure OpenAI model availability across different regions without manual monitoring.