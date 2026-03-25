from storage import StorageManager
from models import Animal


def test_save_mock(monkeypatch):

    def fake_open(*args, **kwargs):
        class FakeFile:
            def write(self, x): pass
            def __enter__(self): return self
            def __exit__(self, *args): pass
        return FakeFile()

    monkeypatch.setattr("builtins.open", fake_open)

    storage = StorageManager()
    storage.save([], [])
