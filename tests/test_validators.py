import re
from datetime import datetime


def is_valid_date(date_str: str) -> bool:
    """Vérifie qu'une chaîne représente une date réelle au format JJ/MM/AAAA."""
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def is_coherent_dates(date_delivrance: str, date_expiration: str) -> bool:
    """Vérifie que la date d'expiration est postérieure à la date de délivrance."""
    if not is_valid_date(date_delivrance) or not is_valid_date(date_expiration):
        return False

    delivrance = datetime.strptime(date_delivrance, "%d/%m/%Y")
    expiration = datetime.strptime(date_expiration, "%d/%m/%Y")
    return expiration > delivrance


def is_valid_sexe(sexe: str) -> bool:
    """Vérifie que la valeur est exactement 'M' ou 'F'."""
    return sexe in ("M", "F")


def is_valid_numero_cni(numero: str) -> bool:
    """Vérifie que le numéro de CNI respecte le format attendu (13 chiffres)."""
    return bool(re.fullmatch(r"\d{13}", numero))