from importlib.metadata import version

__version__ = version("CrowconTempIOC")
del version

__all__ = ["__version__"]
