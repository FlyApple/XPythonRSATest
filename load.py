# encoding: utf-8

import array
import time;
import datetime;
import base64;
from OpenSSL import crypto;

#
def bytes2hex_text(buffer, delim = ",", line = True) :
    result = "";
    n = 0;
    for i in range(0, len(buffer)) :
        #
        result += format("%02X"%buffer[i]);
        if len(buffer) > i + 1 :
            result += delim;
        #
        if line :
            n += 1;
            if n >= 0x10 :
                result += "\n";
                n = 0;
    #
    return result;
    #return delim.join(format("%02X"%x) for x in buffer);

#
file_read = open("ms_ca.cer", mode='r');
data = file_read.read();
file_read.close();
x509 = crypto.load_certificate(crypto.FILETYPE_PEM, data);

#
x509Names = x509.get_issuer().get_components();
x509_issuer_text = str(x509Names[0][0], encoding = "utf-8") +"="+ str(x509Names[0][1], encoding = "utf-8") + "," + str(x509Names[1][0], encoding = "utf-8") +"="+ str(x509Names[1][1], encoding = "utf-8") + "," + str(x509Names[2][0], encoding = "utf-8") +"="+ str(x509Names[2][1], encoding = "utf-8");
print("Issuer : " + x509_issuer_text);

x509Names = x509.get_subject().get_components();
x509_subject_text = str(x509Names[0][0], encoding = "utf-8") +"="+ str(x509Names[0][1], encoding = "utf-8") + "," + str(x509Names[1][0], encoding = "utf-8") +"="+ str(x509Names[1][1], encoding = "utf-8") + "," + str(x509Names[2][0], encoding = "utf-8") +"="+ str(x509Names[2][1], encoding = "utf-8");
print("Subject : " + x509_subject_text);

#
print("Expired : " + ("No" if not x509.has_expired() else "Yes"));

#
x509_tm_start = time.strptime(str(x509.get_notBefore(), encoding = "utf-8"), "%Y%m%d%H%M%SZ");
x509_tm_end = time.strptime(str(x509.get_notAfter(), encoding = "utf-8"), "%Y%m%d%H%M%SZ");

print("Start Date : " + time.strftime("%Y-%m-%d %H:%M:%S (%B,%A)", x509_tm_start));
print("End Date : " + time.strftime("%Y-%m-%d %H:%M:%S (%B,%A)", x509_tm_end));

#
print("Version : " + str(x509.get_version() + 1));

#
x509_serial_number = int.to_bytes(x509.get_serial_number(), length = 0x10, byteorder='big');
print("Serial Number : " + bytes2hex_text(x509_serial_number));

#
x509_signature_algorithm = str(x509.get_signature_algorithm(), encoding = "utf-8");
print("Signature Algorithm : " + x509_signature_algorithm);

#
x509_extension_count = x509.get_extension_count();
print("Extension (" + str(x509_extension_count) + "):")
for n in range(0, x509_extension_count) :
    extension = x509.get_extension(n);
    print("  " + str(extension.get_short_name(), encoding = "utf-8") + " :");
    value = extension.get_data();
    print("   " + bytes2hex_text(value));

#
x509_public_key = x509.get_pubkey();
print("Public Key Bits :" + str(x509_public_key.bits()));
print("Public Key Type :" + str(x509_public_key.type()));

key = x509_public_key.to_cryptography_key();
print("  Exponent : " + format("%X"%key.public_numbers().e));
key_bytes = int.to_bytes(key.public_numbers().n, length = 512, byteorder='big');
print("  Modulus : \n" + bytes2hex_text(key_bytes));

#save public key to file:
file_write = open("public_key.txt", mode='w');
file_write.write(bytes2hex_text(key_bytes));
file_write.close();

data = base64.b64encode(key_bytes);
file_write = open("public_key_base64.txt", mode='w');
file_write.write(str(data, encoding = "utf-8"));
file_write.close();
