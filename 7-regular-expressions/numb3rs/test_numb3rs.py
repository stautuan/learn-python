from numb3rs import validate

def test_validate():
    # Valid IP addresses
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True
    assert validate("192.168.1.1") == True

    # Invalid IP addresses
    assert validate("cat") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.") == False
    assert validate(".1.2.3.4") == False
    assert validate("1.2.3.4.") == False
    assert validate("256.1.2.3") == False
    assert validate("1.256.3.4") == False
    assert validate("1.2.256.4") == False
    assert validate("1.2.3.256") == False

    # Edge cases
    assert validate("01.02.03.04") == True  # Leading zeros are allowed
    assert validate("192.168.01.1") == True
    assert validate("192.168.1.01") == True
    assert validate(" 192.168.1.1 ") == False  # No leading/trailing spaces
    assert validate("192.168.1.1.") == False  # No trailing dot
    assert validate("192..168.1.1") == False  # No empty octets
    assert validate(".192.168.1.1") == False  # No leading dot
    assert validate("192.168.1") == False  # Must have 4 octets

    # Test each octet's range (0-255)
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.0.256") == False
