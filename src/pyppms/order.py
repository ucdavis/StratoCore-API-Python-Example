"""Module representing order objects in PPMS."""

import logging
from io import StringIO
import csv

LOG = logging.getLogger(__name__)


class PpmsOrder:

    """Object representing an order in PPMS.

    Attributes
    ----------
    corefacility : str  
    orderref : str
    user : str
    group : str
    projectref : str
    quoteddate : str
    ordereddate : str
    completeddate : str
    status : str
    invoiced : str
    """

    def __init__(self, order_line):
        """Initialize the order object.

        Parameters
        ----------
        order_line : str
            The text line returned by a PUMAP `getorders` call.
        """
        
        f = StringIO(order_line)
        reader = list(csv.reader(f, delimiter=',', quotechar='"'))
                
        values = reader[0]
        
        self.corefacility =  str(values[0])
        self.orderref =  str(values[1])
        self.user =  str(values[2])
        self.group =  str(values[3])
        self.projectref =  str(values[4])        
        self.quoteddate = str(values[5])
        self.ordereddate = str(values[6])
        self.completeddate = str(values[7])                        
        self.status =  str(values[8])
        self.invoiced =  str(values[9])  
        self.orderlines = None

        LOG.debug(
            "PpmsOrder initialized: corefacility=[%s],orderref=[%s],user=[%s],group=[%s],projectref=[%s],quoteddate=[%s],ordereddate=[%s],completeddate=[%s],status=[%s],invoiced=[%s] ",
            self.corefacility,
            self.orderref,
            self.user,
            self.group,
            self.projectref,
            self.quoteddate,
            self.ordereddate,
            self.completeddate,
            self.status,
            self.invoiced,
        )
    
    @property
    def details(self):
        """Generate a string with details on the order object."""
        
        lines = None
        
        if self.orderlines is not None:
            lines = "[ "
        
            for i in self.orderlines:
                lines = lines + i.toJSON() + ","
        
            lines = lines[:-1] + " ]"        
        
        return (
            f"corefacility: {self.corefacility}, "
            f"orderref: {self.orderref}, "
            f"user: {self.user}, "
            f"group: {self.group}, "
            f"projectref: {self.projectref}, "
            f"quoteddate: {self.quoteddate}, "
            f"ordereddate: {self.ordereddate}, "
            f"completeddate: {self.completeddate}, "
            f"status: {self.status}, "
            f"invoiced: {self.invoiced}, "
            f"orderlines: {lines}"
        )
    def __str__(self):
        return str(self.orderref)
