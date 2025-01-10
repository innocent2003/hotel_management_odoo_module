import logging

_logger = logging.getLogger(__name__)

def log_access_attempt(user_id, resource, action, success):
    _logger.info(f"User {user_id} attempted {action} on {resource}. Success: {success}")
