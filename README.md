# Traffic Analysis
__Python Module for Analyzing SSH traffic log__
 - Analyze SSH traffic logs produced by the journalctl command on Redhat machines
 - This module uses regular expressions to provide basic statistics about failed ssh attempts
	- Attempted user names, number of occurrences
	- Source IP Addresses, number of occurrences

__How to use__

    users_list = log_scraper.getUsers(fileName)
Returns a sorted list of tuples in the form of (Attempted username, number of attempts)

    address_list = log_scraper.getAddresses(fileName)
Returns a sorted list of tuples in the form of (Source of failed login attempt, number of attempts)

    user_list, address_list = log_scraper.getBoth(fileName)
Returns two sorted lists of tuples, in the forms listed above.
