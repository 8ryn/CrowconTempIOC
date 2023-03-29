from argparse import ArgumentParser

import cothread
from softioc import builder, softioc

from CrowconTempIOC.temperatures import Temperatures

from . import __version__

__all__ = ["main"]


def main(args=None):
    parser = ArgumentParser()
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("-u", "--url", action="store", default="http://127.0.0.1:5000")
    args = parser.parse_args(args)

    url = args.url

    # logging.basicConfig(level=logging.DEBUG)

    # Load object to read from website
    tempReader = Temperatures(url)

    # Load units for inputs, not refreshed while running
    units = tempReader.getUnits()

    # Device prefix
    builder.SetDeviceName("B24ES")

    # Create PVs
    warmbaseI = builder.aIn("wbi", initial_value=-999.0, EGU=units[0])
    coldchuckI = builder.aIn("cci", initial_value=-999.0, EGU=units[1])
    gripperbbI = builder.aIn("gbi", initial_value=-999.0, EGU=units[2])

    # Get the IOC started
    builder.LoadDatabase()
    softioc.iocInit()

    def setTemps():
        while True:
            temps = tempReader.getTemps()
            warmbaseI.set(temps[0])
            coldchuckI.set(temps[1])
            gripperbbI.set(temps[2])
            cothread.Sleep(30)

    cothread.Spawn(setTemps)

    cothread.WaitForQuit()


if __name__ == "__main__":
    main()
