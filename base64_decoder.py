import base64

#
string_codificada = 'VmluaWNpdXMgTWFyaW5oZWlybyBEZXY='
decodificar = base64.b64decode(string_codificada)

print('=========================')
print('VMRS DECODING . . .')

print('Decode: ',decodificar)

print('Programa finalizado.')
