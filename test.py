# encoding: utf-8

import base64;
from OpenSSL import crypto;
from Crypto.Util import number;
from cryptography.hazmat.primitives.asymmetric import rsa;

#
from share import share;
from share import math;


#
file_read = open("public_key_base64.txt", mode='r');
data = file_read.read();
file_read.close();

key_bytes = base64.b64decode(data);
key_bits = len(key_bytes) * 8;
print("key bits : " + str(key_bits));

#
num_n = int.from_bytes(key_bytes, byteorder = 'big');
print("n =  \n" + share.integer2hex_text(num_n, int(key_bits / 8), order = 'big'));
print("n is prime " + ("Yes" if number.isPrime(num_n) else "No"));

#
num_e = 0x10001;
print("e =  \n" + share.integer2hex_text(num_e, 3, order = 'big'));
print("e is prime " + ("Yes" if number.isPrime(num_e) else "No"));

num_g = math.gcd(num_n, num_e);
print("g = gcd(n, e) = " + str(num_g));
