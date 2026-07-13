def run_ocr(image_path: str, engine: str = "tesseract") -> str:
    """Exécute l'OCR sur une image et retourne le texte brut extrait.

    Args:
        image_path: chemin vers l'image (idéalement déjà prétraitée).
        engine: "tesseract" ou "easyocr".

    Returns:
        Le texte brut détecté sur l'image.
    """
    raise NotImplementedError("run_ocr n'est pas encore implémenté")