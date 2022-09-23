"""Module representing invoice charge objects in PPMS."""

import logging
import json

LOG = logging.getLogger(__name__)


class PpmsInvoiceCharge:

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    """Object representing an invoice charge in PPMS.

    Attributes
    ----------
    accountnumber : str
        The invoice's account number
    amount : str
        The invoice amount
    """

    def __init__(self, accountnumber, amount):
        """Initialize the invoice charge object.

        Parameters
        ----------
        accountnumber : str
            The account number for the charge.
        amount : str
            The amount of the charge.
        """
        
        self.accountnumber = accountnumber
        self.amount = amount               

        LOG.debug(
            "PpmsInvoiceCharge initialized: accountnumber=[%s], amount=[%s] ",
            self.accountnumber,
            self.amount,
        )

    @property
    def details(self):
        """Generate a string with details on the invoice charge object."""
        return (
            f"accountnumber: {self.accountnumber}, "
            f"amount: {self.amount}"
        )

    def __str__(self):
        return str(self.accountnumber)
