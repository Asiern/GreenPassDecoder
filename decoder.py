import base45
import cbor2
import zlib
from cose.messages import CoseMessage


def DecodeCert(encoded_cert):
    encoded_cert = encoded_cert.replace("HC1:", "")
    decoded = base45.b45decode(encoded_cert)
    decompressed = zlib.decompress(decoded)
    cose = CoseMessage.decode(decompressed)
    return cbor2.loads(cose.payload)


def main():

    # Open valid certificate
    valid_cert = open("valid-cert.txt", "r").read()
    # Decode valid certificate
    decoded = DecodeCert(valid_cert)

    print("GREEN PASS DECODER\n")
    print("Certificate ID: " + decoded[-260][1]["v"][0]["ci"])
    print("Country: " + decoded[-260][1]["v"][0]["co"])
    print("Number of Doses: " + str(decoded[-260][1]["v"][0]["dn"]))
    print("Vaccination Date: " + decoded[-260][1]["v"][0]["dt"])
    print("Cert issuer: " + decoded[-260][1]["v"][0]["is"])
    print("Manufacturer: " + decoded[-260][1]["v"][0]["ma"])
    print("Vaccine Product ID: " + decoded[-260][1]["v"][0]["mp"])
    print("Total Number of Doses: " + str(decoded[-260][1]["v"][0]["sd"]))
    print("Targeted Desease: " + decoded[-260][1]["v"][0]["tg"])
    print("Vaccine or Prophylaxis: " + decoded[-260][1]["v"][0]["vp"])
    print("Date of Birth: " + decoded[-260][1]["dob"])
    print("Family Name: " + decoded[-260][1]["nam"]["fn"])
    print("Name: " + decoded[-260][1]["nam"]["gn"])
    print("Version: " + decoded[-260][1]["ver"])
    print("")


if __name__ == "__main__":
    main()
