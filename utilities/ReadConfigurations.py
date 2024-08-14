import os
from configparser import ConfigParser, NoSectionError, NoOptionError


def read_configuration(category: str, key: str) -> str:
    """Reads a configuration value from a given category and key in the config.ini file.

    Args:
        category (str): The section of the configuration file.
        key (str): The key within the section whose value needs to be fetched.

    Returns:
        str: The value associated with the provided category and key.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        NoSectionError: If the specified section does not exist in the configuration file.
        NoOptionError: If the specified key does not exist in the section.
        Exception: For any other general errors.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(base_dir, '..', 'configurations', 'config.ini')

    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"The configuration file '{config_file_path}' was not found.")

    config = ConfigParser()
    try:
        config.read(config_file_path)
        return config.get(category, key)
    except NoSectionError:
        raise NoSectionError(f"The section '{category}' does not exist in the configuration file.")
    except NoOptionError:
        raise NoOptionError(f"The key '{key}' does not exist in the section '{category}'.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the configuration: {e}")
