# Limiter Python SDK

## Installation

```
pip install pylimiter
```

## Quick Usage

### Default Backend

Initialize SDK with the managed storage backend

```python
from pylimiter import limiter

opts = {
  'backend': 'Default',
  'api_token': 'api-token',
};
client = limiter.Client('project-id', opts);
```

### Available Methods

```python
# Bind user to a plan
client.bind('plan-name', 'user-id')

# Check if a feature is within limit
if client.feature('feature-name', 'user-id'):
  print('Pass')

# Increment usage
client.increment('feature-name', 'user-id', 1)

# Decrement usage
client.decrement('feature-name', 'user-id', 1)

# Set usage to some value
client.set('feature-name', 'user-id', 5)

# Get feature matrix for the project
feature_matrix = client.feature_matrix()

# Get user's usage data
usage = client.usage('user-id')
```
