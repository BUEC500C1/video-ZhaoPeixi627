from tweet import get_tweet

def test_get_tweet():
    assert get_tweet('DCBatman') != ''
    assert get_tweet('DCSuperman') != ''
    assert get_tweet('Eminem') != ''
    assert get_tweet('MikeBloomberg') != ''
