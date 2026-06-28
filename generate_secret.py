import secrets
import string

print("=" * 60)
print("HealthAI Secret Generator")
print("=" * 60)

secret_key = secrets.token_hex(32)

alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_-+="
password = ''.join(secrets.choice(alphabet) for _ in range(20))

print("\nSECRET_KEY:")
print(secret_key)

print("\nRandom Password:")
print(password)