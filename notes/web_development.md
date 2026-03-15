# Web Development Notes

## HTTP Methods
- GET: Retrieve data (idempotent, cacheable)
- POST: Create new resource
- PUT: Update entire resource (idempotent)
- PATCH: Partially update resource
- DELETE: Remove resource

## HTTP Status Codes
- 200 OK, 201 Created, 204 No Content
- 301 Moved Permanently, 302 Found
- 400 Bad Request, 401 Unauthorized, 403 Forbidden
- 404 Not Found, 409 Conflict, 422 Unprocessable Entity
- 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable

## REST API Design
```
GET    /api/users          # List users
POST   /api/users          # Create user
GET    /api/users/:id      # Get user
PUT    /api/users/:id      # Update user
DELETE /api/users/:id      # Delete user
```

## Authentication Patterns
- JWT: Stateless, contains claims, signed
- Session: Server-side storage, cookie-based
- OAuth 2.0: Delegated authorization
- API Keys: Simple, for server-to-server
