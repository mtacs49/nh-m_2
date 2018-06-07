import sha3
from ecdsa import SigningKey, SECP256k1

keccak = sha3.keccak_256()
private = SigningKey.generate(curve=SECP256k1)
public = private.get_verifying_key().to_string()
print ("Private Key: ")
print (private.to_string().hex())
keccak.update(public)
print ("\nPublic Key: ")
print (public.hex())
address = "0x{}".format(keccak.hexdigest()[24:])
print ("\nAddress: ")
print (address)
