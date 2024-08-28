# Go Encryption Service

This project is a miniature HTTP web service that serves as an encryption engine. It allows users to encrypt strings over the internet using a secret key known only to the server. It also provides a way to decrypt secret messages, but only for authenticated users.

## Features (Planned)

- Encryption endpoint: Accepts a string and returns an encrypted version.
- Decryption endpoint: Accepts an encrypted string and returns the decrypted version (authenticated users only).
- Simple ping endpoint for service health checks.

## API Endpoints

1. `/ping`: Responds with a 200 status code to indicate the service is running.
2. `/encrypt`: Accepts a GET request with a JSON payload containing a message to encrypt.
3. `/decrypt`: Accepts a GET request with a JSON payload containing a message to decrypt (requires authentication).

## Technical Stack

- Language: Go
- Web Framework: Net/HTTP (standard library)
- Deployment: Docker (planned)

## Getting Started

### Prerequisites

- Go 1.16 or later
- Git

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/go-encryption-service.git
   ```
2. Navigate to the project directory:
   ```
   cd go-encryption-service
   ```
3. Run the server:
   ```
   go run main.go
   ```

The server will start on port 9090.

## Usage

(To be added as endpoints are implemented)

## Contributing

This project is currently in development. Contributions, ideas, and feedback are welcome.
