"""IPAM database models."""
import socket
import struct

from waylon.database import Column, CRUDMixin, PkModel, db


class IPAddress(PkModel, CRUDMixin):
    """An IP Address."""

    __tablename__ = "ip_addresses"

    ipv4_address = Column(db.String(15), unique=True, nullable=False)
    ipv4_cidr = Column(db.String(2), unique=True, nullable=False)
    device = Column(db.String(80), unique=True, nullable=False)
    location = Column(db.String(80), nullable=False)
    DHCP = Column(db.Boolean, default=False)
    MAC = Column(db.String(17), unique=True, nullable=True)

    def get_cidr(self):
        """Get CIDR."""
        cidr = f'{self.ipv4_address}/{self.ipv4_cidr}'
        return cidr

    def get_subnet(self):
        """Get netmask."""
        host_bits = 32 - int(self.ipv4_cidr)
        netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
        return netmask

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<IPAddress('{self.ipv4_address}/{self.ipv4_cidr}')>"
