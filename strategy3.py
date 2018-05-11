from strategy import Package


def bike_deliver(self):
    print('The', self.package.content, 'is going to be delivered by Bike')
    print('The cost will be $10')
    print('The ETA is 20 days')


def truck_deliver(self):
    print('The', self.package.content, 'is going to be delivered by Truck')
    print('The cost will be $30')
    print('The ETA is 13d ays')


def plane_deliver(self):
    print('The', self.package.content, 'is going to be delivered by Plane')
    print('The cost will be $60')
    print('The ETA is 2 days')


def deliver_package(package):
    if package.urgency == 'low':
        deliver = bike_deliver
    if package.urgency == 'medium':
        deliver = truck_deliver
    if package.urgency == 'high':
        deliver = plane_deliver

    deliver(package)


package = Package('Notebook', 'low')
deliver_package(package)
