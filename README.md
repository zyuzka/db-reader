# DB reader

Simplify pyramid application for reading and testing DB connection.

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

You can provide configuration with specific ENV's variables:

|Variable name|Description|Default value|
|---|---|---|
|APP_PORT|Application port|6543|
|DB_ENGINE|DB engine (pgsql or mysql) |pgsql|
|DB_HOST|DB host|127.0.0.1|
|DB_PORT|DB port|5432|
|DB_NAME|DB name(require)||
|DB_USERNAME|DB username(require)||
|DB_PASSWORD|DB password(require)||

### Prerequisites

| |Version|
|---|---|
|python| 3 |
|pip| 3 |