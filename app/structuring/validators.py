def is_valid_date(date_str: str) -> bool:
    """Vérifie qu'une chaîne représente une date réelle au format JJ/MM/AAAA."""
    raise NotImplementedError("is_valid_date n'est pas encore implémenté")


def is_coherent_dates(date_delivrance: str, date_expiration: str) -> bool:
    """Vérifie que la date d'expiration est postérieure à la date de délivrance."""
    raise NotImplementedError("is_coherent_dates n'est pas encore implémenté")


def is_valid_sexe(sexe: str) -> bool:
    """Vérifie que la valeur est exactement 'M' ou 'F'."""
    raise NotImplementedError("is_valid_sexe n'est pas encore implémenté")


def is_valid_numero_cni(numero: str) -> bool:
    """Vérifie que le numéro de CNI respecte le format attendu."""
    raise NotImplementedError("is_valid_numero_cni n'est pas encore implémenté")