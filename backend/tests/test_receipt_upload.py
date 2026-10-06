from pathlib import Path

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_upload_receipt_saves_valid_image(tmp_path, monkeypatch):
    upload_dir = tmp_path / "receipts"
    monkeypatch.setattr("main.UPLOAD_DIR", upload_dir)

    response = client.post(
        "/upload-receipt",
        files={"file": ("receipt.png", b"fake-image-bytes", "image/png")},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "uploaded"
    assert payload["filename"] == "receipt.png"
    assert (upload_dir / "receipt.png").exists()


def test_upload_receipt_rejects_non_image(monkeypatch, tmp_path):
    upload_dir = tmp_path / "receipts"
    monkeypatch.setattr("main.UPLOAD_DIR", upload_dir)

    response = client.post(
        "/upload-receipt",
        files={"file": ("receipt.txt", b"not an image", "text/plain")},
    )

    assert response.status_code == 400
    assert "image" in response.json()["detail"].lower()
