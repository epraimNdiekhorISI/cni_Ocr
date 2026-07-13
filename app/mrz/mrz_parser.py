def parse_mrz(mrz_lines: list[str]) -> dict:
    """Parse les 3 lignes de la zone MRZ (format TD1) en champs structurés.

    Args:
        mrz_lines: liste de 3 chaînes de 30 caractères (norme ICAO 9303).

    Returns:
        Un dict avec au minimum : numero_document, date_naissance, sexe.
    """
    raise NotImplementedError("parse_mrz n'est pas encore implémenté")


def verify_checksum(mrz_lines: list[str]) -> bool:
    """Vérifie les chiffres de contrôle intégrés dans la MRZ.

    Returns:
        True si tous les checksums sont valides, False sinon.
    """
    raise NotImplementedError("verify_checksum n'est pas encore implémenté")