from app import count_keys, summarise


def test_count_keys():
    assert count_keys({"a": 1, "b": 2}) == 2


def test_summarise_mentions_count():
    assert "2 top-level keys" in summarise({"a": 1, "b": 2})


def test_summarise_handles_empty():
    assert "0 top-level keys" in summarise({})
