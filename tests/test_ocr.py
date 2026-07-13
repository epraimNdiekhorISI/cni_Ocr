from app.ocr.ocr_engine import run_ocr


def test_ocr_extracts_non_empty_text(sample_image_path):
    text = run_ocr(sample_image_path, engine="tesseract")
    assert isinstance(text, str)
    assert len(text.strip()) > 0


def test_ocr_engine_switch_easyocr(sample_image_path):
    text = run_ocr(sample_image_path, engine="easyocr")
    assert isinstance(text, str)