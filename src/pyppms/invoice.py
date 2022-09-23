"""Module representing invoice objects in PPMS."""

import logging
from .invoicecharge import PpmsInvoiceCharge
from .invoicedetails import PpmsInvoiceDetails

LOG = logging.getLogger(__name__)


class PpmsInvoice:

    """Object representing an invoice in PPMS.

    Attributes
    ----------
    invoiceid : str
        The invoice's id 
    charges : array[PpmsInvoice]
        An array of charges for the invoice   
    invoicedetails : array[PpmsInvoiceDetails]
        The details from getinvoicedetails
    """

    def __init__(self, charge_text, detail_text, invoiceid):
        """Initialize the invoice object.

        Parameters
        ----------
        charge_text : str
            The text returned by a PUMAP `getinvoice` call.
        detail_text : str
            The text returned by a PUMAP `getinvoicedetails` call.
        invoiceid : str
            The id of the invoice.
        """
        
        splitcharges = charge_text.splitlines()    
        splitdetails = detail_text.splitlines()  
        
        self.charges = [None] * len(splitcharges)
        self.invoicedetails = [None] * len(splitdetails)
        
        counter = 0
        
        for line in splitcharges:
            values = line.split(",")
            self.invoiceid = invoiceid            
            charge =  PpmsInvoiceCharge(str(values[0].replace('"', '')), str(values[1]))   
            self.charges[counter] = charge    
            counter = counter + 1   
              
        counter = 0
        linenum = 0
        
        for line in splitdetails:
            linenum = linenum + 1
            
            if linenum > 3 : 
                invoicedetails =  PpmsInvoiceDetails(line)   
                
                if invoicedetails is not None :
                    self.invoicedetails[counter] = invoicedetails    
                    counter = counter + 1            

        LOG.debug(
            "PpmsInvoice initialized: invoiceid=[%s],charges=[%s],charges=[%s] ",
            self.invoiceid,
            self.charges,
            self.invoicedetails,
        )
    
    @property
    def details(self):
        """Generate a string with details on the invoice charge object."""
        charges = "[ "
        
        for i in self.charges:
            charges = charges + i.toJSON() + ","
        
        charges = charges[:-1] + " ]"
        
        details = str(len(self.invoicedetails))        
        
        details = "[ "
    
        for i in self.invoicedetails:
            if i is not None:
                details = details + i.toJSON() + ","
    
        details = details[:-1] + " ]"       
        
        return (
            f"accountnumber: {self.invoiceid}, "
            f"charges: {charges}, "
            f"invoicedetails: {details}"
        )
    def __str__(self):
        return str(self.invoiceid)
