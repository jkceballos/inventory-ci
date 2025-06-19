from backend_app.app import get_items

def test_get_items_empty(monkeypatch):
    monkeypatch.setenv("POSTGRES_DB", "test")
    monkeypatch.setenv("POSTGRES_USER", "user")
    monkeypatch.setenv("POSTGRES_PASSWORD", "pass")
    monkeypatch.setenv("DB_HOST", "localhost")

    class Cur:
        def execute(self, q): pass
        def fetchall(self): return []

    class Conn:
        def cursor(self): return Cur()
        def close(self): pass

    monkeypatch.setattr("psycopg2.connect", lambda **kw: Conn())

    result = get_items()
    assert result == []
