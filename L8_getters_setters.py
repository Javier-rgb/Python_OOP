class VotationBox:
    def __init__(self, id, country):
        self._id = id
        self._country = country
        self._region = None

    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, region):
        if region in self._country:
            self._region = region
        else:
            raise ValueError(f'{region} is not valid in {self._country}')


if __name__ == '__main__':
    person = VotationBox(108679, "Mexico")
    person.region = "Mexico"

    print(person._region)
