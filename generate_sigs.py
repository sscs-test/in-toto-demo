from cryptography.hazmat.primitives.asymmetric import rsa
from securesystemslib.signer import CryptoSigner

keys = []
members = [ "alice", "bob", "carl" ]

for i in range(len(members)):
    private_key_file = f"functionary_{members[i]}/{members[i]}"
    public_key_file = private_key_file + ".pub"

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=3072,
    )

    signer = CryptoSigner(private_key)

    # store private key securely
    with open (private_key_file, "wb") as f:
        f.write(signer.private_bytes)

    # store the public key
    pubkey = signer.public_key.to_dict()['keyval']['public']
    with open (public_key_file, "w") as f:
        f.write(pubkey)
    
    

