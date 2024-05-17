from multiprocessing import Pool
import logging

def worker_function(number):
    return number

def add_numbers(numbers: list) -> int:
    with Pool() as pool:
        result = sum(pool.map(worker_function, numbers))
    return result

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

setup_logging()
