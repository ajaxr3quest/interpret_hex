import struct
import argparse
import re

def interpret_hex(hex_value):
    # Verificar que el input sea exactamente 8 caracteres hexadecimales
    if not re.fullmatch(r'[0-9A-Fa-f]{8}', hex_value):
        raise ValueError("❌ Error: Debes ingresar exactamente 4 bytes en formato hexadecimal (ejemplo: '3F800000').")

    # Convertir a decimal (Signed y Unsigned)
    int_signed = struct.unpack('!i', bytes.fromhex(hex_value))[0]   # Signed 32-bit integer
    int_unsigned = struct.unpack('!I', bytes.fromhex(hex_value))[0] # Unsigned 32-bit integer

    # Q16.16 (Fixed-Point)
    q16_16 = int_signed / 65536

    # Escalados por 10, 100, 1000, 10000
    scaled_10 = int_signed / 10
    scaled_100 = int_signed / 100
    scaled_1000 = int_signed / 1000
    scaled_10000 = int_signed / 10000

    # IEEE 754 (32-bit Float)
    float_ieee = struct.unpack('!f', bytes.fromhex(hex_value))[0]

    # Two's Complement (Si es negativo)
    def twos_complement(value, bits=32):
        if value < 0:
            value = (1 << bits) + value
        return value

    twos_comp = twos_complement(int_signed)

    # Imprimir resultados
    print(f"\n🔎 Interpretación de {hex_value.upper()}:")
    print(f"🔹 Signed 32-bit Integer  = {int_signed}")
    print(f"🔹 Unsigned 32-bit Integer = {int_unsigned}")
    print(f"🔹 Q16.16 Fixed-Point      = {q16_16}")
    print(f"🔹 Escalado /10            = {scaled_10}")
    print(f"🔹 Escalado /100           = {scaled_100}")
    print(f"🔹 Escalado /1000          = {scaled_1000}")
    print(f"🔹 Escalado /10000         = {scaled_10000}")
    print(f"🔹 IEEE 754 Float          = {float_ieee}")
    print(f"🔹 Two's Complement        = {bin(twos_comp)[2:].zfill(32)} (Binario)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interpretar un valor hexadecimal de 4 bytes.")
    parser.add_argument("hex_value", type=str, help="Valor hexadecimal de 4 bytes (ejemplo: 3F800000)")
    args = parser.parse_args()

    try:
        interpret_hex(args.hex_value)
    except ValueError as e:
        print(f"{e}")
