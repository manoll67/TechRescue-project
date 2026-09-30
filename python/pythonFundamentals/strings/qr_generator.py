import qrcode
from pathlib import Path

print("=" * 45)
print("          QR CODE GENERATOR")
print("=" * 45)

content = input("Enter the link or text: ").strip()
file_name = input("File name [qr_code.png]: ").strip()

if not content:
    print("Error: no content was entered.")
    exit()

if not file_name:
    file_name = "qr_code.png"

if not file_name.lower().endswith(".png"):
    file_name += ".png"

try:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4
    )

    qr.add_data(content)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    path = Path(file_name)
    image.save(path)

    print("\nQR Code generated successfully.")
    print(f"File: {path.resolve()}")

except Exception as error:
    print(f"\nError during generation: {error}")
