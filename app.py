#Version 2.0-hotfix
def greet(name):
	return f"Hello, {name}!"

def main():
	print(greet("World"))

if __name__ == "__main__":
	main()

import logging

def setup_logging():
	logging.basicConfig(level=logging.INFO)
	logging.info("Logging initialized")

def test_logging():
	setup_logging()
	logging.info("Test message")

