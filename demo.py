from us_visa_prediction.logger import logging
from us_visa_prediction.exception import USvisaException

#logging.info("Welcome to US Visa Prediction Project")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e, sys)