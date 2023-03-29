import requests
from bs4 import BeautifulSoup


class Temperatures:
    def __init__(self, address: str) -> None:
        """
        Initialiser of Temperatures class

        Parameters:
        address (str): URL to read data from
        """
        self.address = address

        pageResp = requests.get(address)
        self.soup = BeautifulSoup(pageResp.content, "html.parser")

    def update(self) -> None:
        """
        Updates the loaded beautifulsoup object self.soup
        """
        pageResp = requests.get(self.address)
        self.soup = BeautifulSoup(pageResp.content, "html.parser")

    def getTemps(self) -> tuple[float, float, float]:
        """
        Returns the temperatures of the Warm Base, Cold Chuck & Gripper BB

        Returns:
        (float, float, float): Warm Base temp, Cold Chich temp, Gripper BB temp
        """
        self.update()
        tempLines = self.soup.find_all(class_="temp")
        # 2, 8, 14 are the relevant postions of the temperatures in HTML
        return (
            float(tempLines[2].text),
            float(tempLines[8].text),
            float(tempLines[14].text),
        )

    def getUnits(self) -> tuple[str, str, str]:
        """
        Returns the units of the Warm Base, Cold Chuck & Gripper BB

        Returns:
        (str, str, str): Warm Base unit, Cold Chich unit, Gripper BB unit
        """
        self.update()
        tempLines = self.soup.find_all(class_="temp")
        # 3, 9, 15 are the relevant postions of the units in HTML
        return (
            tempLines[3].text,
            tempLines[9].text,
            tempLines[15].text,
        )
