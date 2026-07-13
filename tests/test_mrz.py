from app.mrz.mrz_parser import parse_mrz, verify_checksum


def test_parse_mrz_returns_expected_fields(sample_mrz_lines):
    data = parse_mrz(sample_mrz_lines)
    assert "numero_document" in data
    assert "date_naissance" in data
    assert "sexe" in data
    assert data["sexe"] in ("M", "F")


def test_mrz_checksum_valid(sample_mrz_lines):
    assert verify_checksum(sample_mrz_lines) is True


def test_mrz_checksum_invalid_detected():
    lignes_corrompues = [
        "IDSEN1234567890999<<<<<<<<<<<<<<<<",   # numéro modifié -> checksum cassé
        "9001019M3001017SEN<<<<<<<<<<<<<<<8",
        "DIOP<<FATOU<<<<<<<<<<<<<<<<<<<<<<<<",
    ]
    assert verify_checksum(lignes_corrompues) is False