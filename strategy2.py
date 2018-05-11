from strategy import Package


class BikeDelivery:

    def __init__(self, package):
        self.package = package

    def deliver(self):
        print('The', self.package.content, 'is going to be delivered by Bike')
        print('The cost will be $10')
        print('The ETA is 20 days')


class TruckDelivery:

    def __init__(self, package):
        self.package = package

    def deliver(self):
        print('The', self.package.content, 'is going to be delivered by Truck')
        print('The cost will be $30')
        print('The ETA is 13d ays')


class PlaneDelivery:

    def __init__(self, package):
        self.package = package

    def deliver(self):
        print('The', self.package.content, 'is going to be delivered by Plane')
        print('The cost will be $60')
        print('The ETA is 2 days')


def deliver_package(package):
    if package.urgency == 'low':
        DeliverStrategy = BikeDelivery
    if package.urgency == 'medium':
        DeliverStrategy = TruckDelivery
    if package.urgency == 'high':
        DeliverStrategy = PlaneDelivery

    strategy = DeliverStrategy(package)
    strategy.deliver()


package = Package('Racket', 'low')
deliver_package(package)
