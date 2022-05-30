import base64

#
string_codificada = 'VHVkbyBxdWUgdm9jw6ogdsOqIGRlbnRybyBkZXN0ZSBhcXVpIHRlIGxldmEgYSBjcmVyIHF1ZSB2b2PDqiBlc3TDoSBuYXZlZ2FuZG8gZW0gdW0gYXJxdWl2byAucGRmLCBwb3LDqW0gc2UgbXVkw6EtbG8gcGFyYSAudHh0IGlyw6EgcGVyY2ViZXIgcXVlIGjDoSBtYWlzIGluZm9ybWHDp8O1ZXMgYWzDqW0gZG8gcXVlIGVzdGEgdmVuZG8u'
decodificar = base64.b64decode(string_codificada)

print('=========================')
print('VMRS DECODING . . .')

print('Decode: ',decodificar)

print('Programa finalizado.')