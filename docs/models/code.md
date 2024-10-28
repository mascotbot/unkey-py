# Code

A machine readable code why the key is not valid.
Possible values are:
- VALID: the key is valid and you should proceed
- NOT_FOUND: the key does not exist or has expired
- FORBIDDEN: the key is not allowed to access the api
- USAGE_EXCEEDED: the key has exceeded its request limit
- RATE_LIMITED: the key has been ratelimited
- UNAUTHORIZED: the key is not authorized
- DISABLED: the key is disabled
- INSUFFICIENT_PERMISSIONS: you do not have the required permissions to perform this action
- EXPIRED: The key was only valid for a certain time and has expired.

These are validation codes, the HTTP status will be 200.



## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `VALID`                    | VALID                      |
| `NOT_FOUND`                | NOT_FOUND                  |
| `FORBIDDEN`                | FORBIDDEN                  |
| `USAGE_EXCEEDED`           | USAGE_EXCEEDED             |
| `RATE_LIMITED`             | RATE_LIMITED               |
| `UNAUTHORIZED`             | UNAUTHORIZED               |
| `DISABLED`                 | DISABLED                   |
| `INSUFFICIENT_PERMISSIONS` | INSUFFICIENT_PERMISSIONS   |
| `EXPIRED`                  | EXPIRED                    |