# -*- coding: utf-8 -*-
"""Model unit tests."""

import pytest

from waylon.ipam.models import IPAddress

from .factories import IPAddressFactory


@pytest.mark.usefixtures("db")
class TestIPAddress:
    """IP Address tests."""

    def test_get_by_id(self):
        """Get IP Address by ID."""
        ip_address = IPAddress(
            ipv4_address="1.2.3.4",
            ipv4_cidr="24",
            device="device",
            location="location",
            DHCP=True,
            MAC="99:99:99:99:99:99",
        )
        ip_address.save()
        retrieved = IPAddress.get_by_id(ip_address.id)
        assert retrieved == ip_address

    def test_factory(self, db):
        """Test IP Address factory."""

        ip_address = IPAddressFactory(
            ipv4_address="1.2.3.4",
            ipv4_cidr="24",
            device="device",
            location="location",
            DHCP=True,
            MAC="99:99:99:99:99:99",
        )
        db.session.commit()
        assert bool(ip_address.ipv4_address)
        assert bool(ip_address.ipv4_cidr)
        assert bool(ip_address.device)
        assert bool(ip_address.location)
        assert bool(ip_address.DHCP)
        assert bool(ip_address.MAC)

    def test_get_cidr(self):
        """Get CIDR."""
        ip_address = IPAddress(
            ipv4_address="1.2.3.4",
            ipv4_cidr="24",
            device="device",
            location="location",
            DHCP=True,
            MAC="99:99:99:99:99:99",
        )
        assert ip_address.get_cidr() == "1.2.3.4/24"

    def test_get_netmask(self):
        """Get netmask."""
        ip_address = IPAddress(ipv4_address="1.2.3.4", ipv4_cidr="24")
        assert ip_address.get_netmask() == "255.255.255.0"

    def test_ip_address_repr(self):
        """Check __repr__ output for IP Address."""
        ip_address = IPAddress(ipv4_address="1.2.3.4", ipv4_cidr="24")
        assert ip_address.__repr__() == "<IPAddress('1.2.3.4/24')>"
