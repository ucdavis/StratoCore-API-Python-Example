"""Module representing order line objects in PPMS."""

import logging
import json
from io import StringIO
import csv

LOG = logging.getLogger(__name__)


class PpmsOrderLine:

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    """Object representing an order line in PPMS.

    Attributes
    ----------
    corefacility : str  
    orderref : str 
    orderid : str
    serviceid : str
    quantity : str
    user : str
    group : str
    projectref : str
    quoteddate : str
    ordereddate : str
    completeddate : str
    status : str
    invoiced : str
    """

    def __init__(self, response_line):
        """Initialize the order line object.

        Parameters
        ----------
        response_line : str
            The text line returned by a PUMAP `getorderlines` call.
        """
        
        f = StringIO(response_line)
        reader = list(csv.reader(f, delimiter=',', quotechar='"'))
                
        values = reader[0]
        
        self.corefacility =  str(values[0])
        self.orderref =  str(values[1])
        self.orderid =  str(values[2])
        self.serviceid =  str(values[3])
        self.quantity =  str(values[4])
        self.user =  str(values[5])
        self.group =  str(values[6])
        self.projectref =  str(values[7])
        
        self.quoteddate = str(values[8])
        self.ordereddate = str(values[9])
        self.completeddate = str(values[10])
                        
        self.status =  str(values[11])
        self.invoiced =  str(values[12])  

        LOG.debug(
            "PpmsOrder initialized: corefacility=[%s],orderref=[%s],orderid=[%s],serviceid=[%s],quantity=[%s],user=[%s],group=[%s],projectref=[%s],quoteddate=[%s],ordereddate=[%s],completeddate=[%s],status=[%s],invoiced=[%s] ",
            self.corefacility,
            self.orderref,
            self.orderid,
            self.serviceid,
            self.quantity,
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
        """Generate a string with details on the order line object."""

        return (
            f"corefacility: {self.corefacility}, "
            f"orderref: {self.orderref}, "
            f"orderid: {self.orderid}, "
            f"serviceid: {self.serviceid}, "
            f"quantity: {self.quantity}, "
            f"user: {self.user}, "
            f"group: {self.group}, "
            f"projectref: {self.projectref}, "
            f"quoteddate: {self.quoteddate}, "
            f"ordereddate: {self.ordereddate}, "
            f"completeddate: {self.completeddate}, "
            f"status: {self.status}, "
            f"invoiced: {self.invoiced}"
        )
    def __str__(self):
        return str(self.orderref)
