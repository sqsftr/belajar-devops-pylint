"""Contoh kode yang memenuhi standar Pylint."""


def calculate_result(first_value, second_value):
    """Menghitung penjumlahan dua angka.

    Args:
        first_value: Angka pertama.
        second_value: Angka kedua.

    Returns:
        Hasil penjumlahan kedua angka.
    """
    return first_value + second_value


def main():
    """Menjalankan program utama."""
    result = calculate_result(10, 20)
    print(result)


if __name__ == "__main__":
    main()
