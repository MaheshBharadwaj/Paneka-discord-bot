class InvalidLimitException(Exception):
    """
    Invalid number of matches requested
    """
    pass

class InvalidLeagueCodeException(Exception):
    """
    The League code requested is either invalid or not supported
    """
    pass

class InvalidTeamCodeException(Exception):
    """
    The Team Code requested is invalid
    """
    pass


