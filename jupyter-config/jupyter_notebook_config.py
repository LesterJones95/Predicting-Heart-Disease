# Jupyter Notebook Configuration for Secure Server (Jupyter Server 2.0+)
import os
import sys

# Server settings
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.ServerApp.allow_root = True
c.ServerApp.allow_remote_access = True

# Set working directory to home (so you can see all your files)
c.ServerApp.root_dir = '/app'

# Check for password hash
password_hash = os.environ.get('JUPYTER_PASSWORD_HASH', '')
password_hash = password_hash.strip()

if password_hash:
    # Use password authentication
    c.ServerApp.password = password_hash
    c.PasswordIdentityProvider.hashed_password = password_hash
    c.PasswordIdentityProvider.password_required = True
    
    # Disable token when using password
    c.ServerApp.token = ''
    c.IdentityProvider.token = ''
    
    print("✓ Password authentication enabled", file=sys.stderr)
    print(f"✓ Using password hash: {password_hash[:25]}...", file=sys.stderr)
else:
    # Fall back to default token-based authentication
    print("⚠ No password hash set - using default token authentication", file=sys.stderr)
    print("⚠ Check the startup logs for the access token URL", file=sys.stderr)
    # Leave token settings at default (Jupyter will generate one)

# SSL/HTTPS Configuration
cert_file = '/home/jovyan/.jupyter/jupyter_cert.pem'
key_file = '/home/jovyan/.jupyter/jupyter_key.key'

if os.path.exists(cert_file) and os.path.exists(key_file):
    c.ServerApp.certfile = cert_file
    c.ServerApp.keyfile = key_file
    print("✓ SSL/HTTPS enabled", file=sys.stderr)
else:
    print("⚠ WARNING: SSL certificates not found. Running without HTTPS!", file=sys.stderr)