"""Test IPAM module."""


def test_home_page_has_link_ipam(testapp):
    """Test IPAM home page."""
    response = testapp.get("/")
    assert 'href="/ipam/"' in response.text

def test_ipam_home_route_returns_success(testapp):
    """Test IPAM home page."""
    response = testapp.get("/ipam/")
    assert response.status_code == 200

def test_ipam_home_route_returns_proper_page(testapp):
    """test_ipam_home_route_returns_proper_page."""
    response = testapp.get("/ipam/")
    assert response.status_code == 200
    assert "<title>IPAM</title>" in response.text

def test_ipam_new_route_returns_success(testapp):
    """Test IPAM new page."""
    response = testapp.get("/ipam/new")
    assert response.status_code == 200

def test_new_ipam_route_returns_proper_page(testapp):
    """test_new_ipam_route_returns_proper_page."""
    response = testapp.get("/ipam/new")
    assert response.status_code == 200
    assert "<title>New IPAM Page</title>" in response.text

def test_ipam_new_page_displays_form(testapp):
    """Test IPAM new page."""
    response = testapp.get("/ipam/new")
    assert "<form" in response.text

def test_ipam_home_has_new_button(testapp):
    """Test IPAM home page."""
    response = testapp.get("/")
    assert 'href="/ipam/new"' in response.text