# Limiter Python SDK

## Installation

```
pip install py-limiter
```

## Quick Usage

### Default Backend

Initialize SDK with the managed storage backend

```python
from pylimiter import limiter

opts = {
  backend: 'Default',
  apiToken: 'api-token',
};
client = limiter.Client('project-id', opts);
```

### Available Methods

```python
# Bind user to a plan
client.bind('plan-name', 'user-id')

# Check if a feature is within limit
if client.feature('feature-name', 'user-id'):
  # Pass

# Increment usage by 1.
client.increment('feature-name', 'user-id')

# Decrement usage by 1.
client.decrement('feature-name', 'user-id')

# Set usage to some value.
client.set('feature-name', 'user-id', 5)

# Get feature matrix for the project
featureMatrix = client.feature_matrix()

# Get user's usage data
const usage = client.usage('user-id')
```
