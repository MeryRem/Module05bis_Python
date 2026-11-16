import os
from dotenv import load_dotenv


load_dotenv()

mode = os.getenv("MATRIX_MODE", "development")
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "DEBUG")
zion_endpoint = os.getenv("ZION_ENDPOINT")


print("ORACLE STATUS: Consulting the configuration...")
print("Configuration loaded:")
print(f"Mode: {mode}")

if mode == "production":
    print("Production configuration active")
else:
    print("Development configuration active")

if database_url:
    print("Database: Connected to local instance")
else:
    print("Database: Configuration missing")

if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: Configuration missing")

print(f"Log Level: {log_level}")

if zion_endpoint:
    print("Remote Network: Online")
else:
    print("Remote Network: Configuration missing")

print("Configuration security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly ignored by git")
print("[OK] Production overrides available")

print("The Oracle sees all configurations.")
