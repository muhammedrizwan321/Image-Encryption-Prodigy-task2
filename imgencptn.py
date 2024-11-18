from PIL import Image
import numpy as np


def encrypt_image(input_image_path, output_image_path, key):
    """
    Encrypts an image using pixel manipulation.
    Args:
        input_image_path (str): Path to the input image.
        output_image_path (str): Path to save the encrypted image.
        key (int): A numeric key for encryption.
    """
    # Open the image and convert to numpy array
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Apply encryption logic (example: add key modulo 256)
    encrypted_array = (image_array + key) % 256

    # Convert back to image and save
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")


def decrypt_image(input_image_path, output_image_path, key):
    """
    Decrypts an encrypted image using the same key used for encryption.
    Args:
        input_image_path (str): Path to the encrypted image.
        output_image_path (str): Path to save the decrypted image.
        key (int): A numeric key used for decryption.
    """
    # Open the encrypted image and convert to numpy array
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Apply decryption logic (reverse operation of encryption)
    decrypted_array = (image_array - key) % 256

    # Convert back to image and save
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")


# Example usage
if __name__ == "__main__":
    key = 50  # Example key for encryption and decryption
    encrypt_image("input.jpg", "encrypted.jpg", key)
    decrypt_image("encrypted.jpg", "decrypted.jpg", key)
