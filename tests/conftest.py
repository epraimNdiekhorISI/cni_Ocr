import os
import pytest


@pytest.fixture
def sample_image_path():
    """Chemin vers une image de test anonymisée du recto de la CNI."""
    return os.path.join(os.path.dirname(__file__), "images", "recto_sample_01.jpg")


@pytest.fixture
def sample_mrz_lines():
    """Trois lignes MRZ fictives, syntaxiquement valides (checksums corrects),
    pour tester le parsing MRZ indépendamment de la qualité de l'OCR."""
    return [
        "IDSEN1234567890123<<<<<<<<<<<<<<<<",
        "9001019M3001017SEN<<<<<<<<<<<<<<<8",
        "DIOP<<FATOU<<<<<<<<<<<<<<<<<<<<<<<<",
    ]