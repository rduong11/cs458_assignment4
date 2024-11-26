import hashlib

#takes a name and turns into hash using the library function
def compute_sha256(name):
    sha256_hash = hashlib.sha256(name.encode('utf-8')).hexdigest()
    return sha256_hash


name = input("Please enter your name: ")
print(compute_sha256(name))
