---
name: bruno-api-collections
description: Author, edit, and organize Git-friendly .bru API request collections and environments for Bruno. Use when creating REST/GraphQL endpoints, environment variables, or API test suites stored in a repository.
license: MIT
---

# Bruno API Collections (`.bru`)

Create and maintain plain-text `.bru` API collections that live cleanly inside Git repositories.

## Collection Structure

```text
bruno-collection/
├── bruno.json
├── environments/
│   ├── local.bru
│   └── staging.bru
└── users/
    └── get-profile.bru
```

## Example `bruno.json`

```json
{
  "version": "1",
  "name": "API Collection",
  "type": "collection"
}
```

## Example Request (`.bru`)

```bru
meta {
  name: Get Profile
  type: http
  seq: 1
}

get {
  url: {{baseUrl}}/api/v1/profile
  body: none
  auth: bearer
}

auth:bearer {
  token: {{authToken}}
}

tests {
  test("returns 200 OK", function () {
    expect(res.getStatus()).to.equal(200);
  });
}
```

## Running from CLI

If `@usebruno/cli` is available, run collections headlessly in CI or local terminals:

```zsh
npx @usebruno/cli run --env local
```
