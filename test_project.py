from project import get_info

def test_input():
    # Capture the SystemExit exception
    with pytest.raises(SystemExit) as exit:
        get_info()
    
    assert exit.value == "No link provided. Exiting..."