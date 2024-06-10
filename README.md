# Nonograms API

The Nonograms API provides access to a collection of nonogram boards cowardly stolen from the [Nonogram Database](https://github.com/mikix/nonogram-db).

## Demo

You can find a live demo on [Deta](https://nonogramapi-1-v4517841.deta.app/docs).

## API Overview

Explore the API using the [Swagger UI](https://nonogramapi-1-v4517841.deta.app/docs) or refer to the brief overview below:

### Endpoints

#### `/`: Get a list of available nonogram keys

**Response:**
```json
[
  "Ant",
  "Artist",
  "Bark Like a Tree and Get Out of Here",
  "Belle",
  "Big Hair"
]
```

#### `/random`: Get a random nonogram

**Response:**
```json
{
  "catalogue": "gnonograms blender.gno",
  "title": "Blender",
  "by": "Frederico Vera <dktcoding@gmail.com>",
  "copyright": "© 2010 Frederico Vera <dktcoding@gmail.com>",
  "license": "CC-BY-SA-4.0",
  "height": 5,
  "width": 5,
  "rows": [
    [3],
    [5],
    [4],
    [5],
    [5]
  ],
  "columns": [
    [2],
    [4],
    [5],
    [5],
    [1, 5]
  ],
  "goal": [
    [false, false, false, false, true],
    [false, false, false, true, false],
    [false, false, true, false, false],
    [false, true, false, false, false],
    [true, false, false, false, false]
  ]
}
```

#### `/{key}`: Get a nonogram by key (title)

**Response:**
```json
{
  "catalogue": "gnonograms blender.gno",
  "title": "Blender",
  "by": "Frederico Vera <dktcoding@gmail.com>",
  "copyright": "© 2010 Frederico Vera <dktcoding@gmail.com>",
  "license": "CC-BY-SA-4.0",
  "height": 5,
  "width": 5,
  "rows": [
    [3],
    [5],
    [4],
    [5],
    [5]
  ],
  "columns": [
    [2],
    [4],
    [5],
    [5],
    [1, 5]
  ],
  "goal": [
    [false, false, false, false, true],
    [false, false, false, true, false],
    [false, false, true, false, false],
    [false, true, false, false, false],
    [true, false, false, false, false]
  ]
}
```
