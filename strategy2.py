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


class PackageDeliveryStretegy:

    def __init__(self, package):
        self.package = package

        if package.urgency == 'low':
            self.DeliverStrategy = BikeDelivery
        if package.urgency == 'medium':
            self.DeliverStrategy = TruckDelivery
        if package.urgency == 'high':
            self.DeliverStrategy = PlaneDelivery

    def deliver(self):
        strategy = self.DeliverStrategy(self.package)
        strategy.deliver()


def deliver_package(package):
    package_delivery = PackageDeliveryStretegy(package)
    package_delivery.deliver()


package = Package('Computer', 'low')
deliver_package(package)
