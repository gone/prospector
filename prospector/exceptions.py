# -*- coding: utf-8 -*-


class FatalProspectorException(Exception):

    """
    Exception used to indicate an internal prospector problem.
    Problems in prospector itself should raise this to notify
    the user directly. Errors in dependent tools which should
    be squashed and the user notified elegantly.
    """

    pass
