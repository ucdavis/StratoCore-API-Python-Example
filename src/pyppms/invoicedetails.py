"""Module representing invoice detail objects in PPMS."""

import logging
import json

from io import StringIO
import csv

LOG = logging.getLogger(__name__)


class PpmsInvoiceDetails:

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    """Object representing an invoice detail in PPMS.

    Attributes
    ----------
    reference : str
    user : str
    group : str
    project : str
    affiliation : str
    sessiontype : str
    systemtype : str
    system : str
    date  : str
    starttime : str
    durationbooked : str
    durationused : str
    usedbyothers : str
    bookedbyothers : str
    cancelled : str
    cancelleddate : str
    specialenv1 : str
    specialenv2 : str
    usercomments : str
    notes : str
    accountnumber : str
    accountnumbersubsidy : str
    rebate : str
    fee : str
    subsidy : str
    finalamount : str
    
    
    details for sessions: reference, user, group, project, affiliation, 
        session type, system type, system, date, start time, duration (booked), 
        duration (used), used by others, booked by others, cancelled, cancelled date, 
        special env. 1, special env. 2, user comments, notes, account number, 
        account number (subsidy), rebate, fee, subsidy, final amount.

    details for trainings: reference, user, group,, affiliation, session type, 
        system type, system, date, start time, duration,,,,,,,,,, account number, 
        account number (subsidy),,, subsidy, final amount.

    details for services/consumables : reference, user, group, project, 
        affiliation, type,,, date completed,,,,,,,,,,,, account number, 
        account number (subsidy),,, subsidy, final amount.
        
    details for subsidies : reference,,,,,type,,,,,,,,,,,,,,,account number
        ,,,,,final amount             
    """

    def __init__(self, response_line):
        """Initialize the invoice details object.

        Parameters
        ----------
        response_line : str
            The CSV formatted string of details
        """
        f = StringIO(response_line)
        reader = list(csv.reader(f, delimiter=',', quotechar='"'))
                
        values = reader[0]
        
        self.reference =  str(values[0])
        self.user =  str(values[1])
        self.group =  str(values[2])
        self.project =  str(values[3])
        self.affiliation =  str(values[4])
        self.sessiontype =  str(values[5])
        self.systemtype =  str(values[6])
        self.system =  str(values[7])        
        self.date = str(values[8])
        self.starttime = str(values[9])
        self.durationbooked = str(values[10])                        
        self.durationused =  str(values[11])
        self.usedbyothers =  str(values[12])         
        self.bookedbyothers =  str(values[13])    
        self.cancelled =  str(values[14])  
        self.cancelleddate =  str(values[15])  
        self.specialenv1 =  str(values[16])  
        self.specialenv2 =  str(values[17])  
        self.usercomments =  str(values[18])  
        self.notes =  str(values[19])  
        self.accountnumber =  str(values[20])  
        self.accountnumbersubsidy =  str(values[21])  
        self.rebate =  str(values[22])  
        self.fee =  str(values[23])  
        self.subsidy =  str(values[24])  
        self.finalamount =  str(values[25])  

        LOG.debug(
            "PpmsInvoiceDetails initialized: reference=[%s], user=[%s], group=[%s], project=[%s], affiliation=[%s], sessiontype=[%s], systemtype=[%s], system=[%s], date=[%s], starttime=[%s], durationbooked=[%s], durationused=[%s], usedbyothers=[%s], bookedbyothers=[%s], cancelled=[%s], cancelleddate=[%s], specialenv1=[%s], specialenv2=[%s], usercomments=[%s], notes=[%s], accountnumber=[%s], accountnumbersubsidy=[%s], rebate=[%s], fee=[%s], subsidy=[%s], finalamount=[%s]",
            self.reference,
            self.user,
            self.group,
            self.project,
            self.affiliation,
            self.sessiontype,
            self.systemtype,
            self.system,
            self.date,
            self.starttime,
            self.durationbooked,
            self.durationused,
            self.usedbyothers,
            self.bookedbyothers,
            self.cancelled,
            self.cancelleddate,
            self.specialenv1,
            self.specialenv2,
            self.usercomments,
            self.notes,
            self.accountnumber,
            self.accountnumbersubsidy,
            self.rebate,
            self.fee,
            self.subsidy,  
            self.finalamount
        )

    @property
    def details(self):
        """Generate a string with details on the invoice details object."""
        return (
            f"reference: {self.reference}, "
            f"user: {self.user}, "
            f"group: {self.group}, "
            f"project: {self.project}, "
            f"affiliation: {self.affiliation}, "
            f"sessiontype: {self.sessiontype}, "
            f"systemtype: {self.systemtype}, "
            f"system: {self.system}, "
            f"date: {self.date}, "
            f"starttime: {self.starttime}, "
            f"durationbooked: {self.durationbooked}, "
            f"durationused: {self.durationused}, "
            f"usedbyothers: {self.usedbyothers}, "
            f"bookedbyothers: {self.bookedbyothers}, "
            f"cancelled: {self.cancelled}, "
            f"cancelleddate: {self.cancelleddate}, "
            f"specialenv1: {self.specialenv1}, "
            f"specialenv2: {self.specialenv2}, "
            f"usercomments: {self.usercomments}, "
            f"notes: {self.notes}, "
            f"accountnumber: {self.accountnumber}, "
            f"accountnumbersubsidy: {self.accountnumbersubsidy}, "
            f"rebate: {self.rebate}, "
            f"fee: {self.fee}, "
            f"subsidy: {self.subsidy}, "
            f"finalamount: {self.finalamount}"
        )

    def __str__(self):
        return str(self.reference)
